import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics
import seaborn as sns

from matplotlib.collections import EllipseCollection


def draw_ellipses(w, mu, C, nsigmas=2, color='lightgray', axis=None):
    """Draw a collection of ellipses.
    Uses the low-level EllipseCollection to efficiently draw a large number
    of ellipses. Useful to visualize the results of a GMM fit via
    GMM_pairplot() defined below.
    Parameters
    ----------
    w : array
        1D array of K relative weights for each ellipse. Must sum to one.
        Ellipses with smaller weights are rended with greater transparency.
    mu : array
        Array of shape (K, 2) giving the 2-dimensional centroids of
        each ellipse.
    C : array
        Array of shape (K, 2, 2) giving the 2 x 2 covariance matrix for
        each ellipse.
    axis : matplotlib axis or None
        Plot axis where the ellipse collection should be drawn. Uses the
        current default axis when None.
    """
    # Calculate the ellipse angles and bounding boxes using SVD.
    U, s, _ = np.linalg.svd(C)
    angles = np.degrees(np.arctan2(U[:, 1, 0], U[:, 0, 0]))
    widths, heights = 2 * nsigmas * np.sqrt(s.T)
    # Data limits must already be defined for axis.transData to be valid.
    axis = axis or plt.gca()
    axis.add_collection(EllipseCollection(
        widths, heights, angles, units='xy', offsets=mu, linewidths=4,
        transOffset=axis.transData, facecolors='none', edgecolors='k'))
    axis.add_collection(EllipseCollection(
        widths, heights, angles, units='xy', offsets=mu, linewidths=2.5,
        transOffset=axis.transData, facecolors='none', edgecolors='w'))


def display_gmm(data, fit, xsize=10, ysize=10, ax=None):
    ax = ax or plt.gca()
    n_components = len(np.unique(fit.weights_))
    # Pick good colors to distinguish the different clusters.
    import matplotlib.colors
    cmap = matplotlib.colors.ListedColormap(
        sns.color_palette('husl', n_components).as_hex())
    # Look up the relative probability that each sample belongs to each cluster.
    prob = fit.predict_proba(data)
    # Assign each sample to its most probable cluster.
    labels = np.argmax(prob, axis=1)
    color = cmap(labels)
    if n_components > 1:
        # Calculate the relative entropy (0-1) as a measure of cluster assignment ambiguity.
        relative_entropy = -np.sum(prob * np.log(prob), axis=1) / np.log(n_components)
        color[:, :3] *= (1 - relative_entropy).reshape(-1, 1)
    ax.scatter(data.iloc[:, 0], data.iloc[:, 1], s=10, c=color, cmap=cmap)
    draw_ellipses(fit.weights_, fit.means_, fit.covariances_, axis=ax)
    # Use standard axes to match the plot above.
    ax.set_xlim(-xsize, +xsize)
    ax.set_ylim(-ysize, +ysize)
    ax.set_aspect(1.)


def plot_image(data, size=16, ax=None, label=None,
               pos_cmap='viridis', neg_cmap='pink'):
    """Plot a single image of binned data.

    Use a sqrt scaling for the pixel colors to improve the dynamic range.

    Positive and negative values use different colormaps.

    Parameters
    ----------
    data : array
        Array containing pixel data.  Will be reshaped to (size, size).
    size : int
        Number of pixels along each side.
    ax : matplotlib axis or None
        Use the specified axis or the default axis when None.
    label : string or None
        Optional label to display centered at the bottom of the image.
    pos_cmap : matplotlib colormap
        Colormap to use for pixel values >= 0.
    neg_cmap : matplotlib colormap
        Colormap to use for pixel values < 0.
    """
    ax = ax or plt.gca()
    image = data.reshape(size, size)
    sqrt_image = np.sqrt(np.abs(image))
    vmax = np.max(sqrt_image)
    pos_image = sqrt_image.copy()
    pos_image[image < 0] = -np.inf
    ax.imshow(pos_image, cmap=pos_cmap, origin='lower', interpolation='none',
              extent=(-0.5 * size, 0.5 * size, -0.5 * size, 0.5 * size),
              vmin=0, vmax=vmax)
    if np.any(image < 0):
        neg_image = sqrt_image.copy()
        neg_image[image >= 0] = -np.inf
        ax.imshow(neg_image, cmap=neg_cmap, origin='lower',
                  interpolation='none', vmin=0, vmax=vmax,
                  extent=(-0.5 * size, 0.5 * size, -0.5 * size, 0.5 * size))
    ax.axis('off')
    if label:
        ax.text(0., -0.45 * size, label, horizontalalignment='center',
                color='w', fontsize=14)


def plot_classification(nsrc_predict, nsrc_true, n_max=4, label=''):
    """Summary plot of classification performance.
    """
    bins = np.linspace(0.5, n_max + 0.5, n_max + 1)
    fig, axes = plt.subplots(1, n_max, sharex=True, sharey=True,
                             figsize=(3 * n_max, 3))
    for n in range(1, n_max + 1):
        sel = (nsrc_true == n)
        ax = axes[n - 1]
        f, _, _ = ax.hist(nsrc_predict[sel], bins, histtype='stepfilled',
                          lw=2, density=True)
        ax.axvline(n, c='r', ls='--')
        ax.text(0.83, 0.9, f'{label}{100 * f[n - 1]:.1f}%',
                horizontalalignment='right', color='r', fontsize=14,
                transform=ax.transAxes)
    plt.tight_layout()


def scan_misclassified(nsrc_predict, nsrc_true, df, n_max=4):
    """Scan some examples of misclassified images.
    """
    c = sklearn.metrics.confusion_matrix(nsrc_true, nsrc_predict)
    fig, axes = plt.subplots(1, n_max, sharex=True, sharey=True,
                             figsize=(3 * n_max, 3))
    for n in range(1, n_max + 1):
        # Find the most common failure.
        c[n - 1, n - 1] = 0
        n_bad = np.argmax(c[n - 1]) + 1
        if c[n - 1, n_bad - 1] == 0:
            print(f'No wrong classifications for nsrc_true = {n}')
            continue
        sel = (nsrc_true == n) & (nsrc_predict == n_bad)
        idx = np.where(sel)[0][0]
        plot_image(df.iloc[idx].values, ax=axes[n - 1],
                   label=f'true={n}, pred={n_bad}')
    plt.tight_layout()


def plot_regression(e_predict, e_true, ax=None, label='', e_max=0.5):
    """Summary plot of regression performance.
    """
    ax = ax or plt.gca()
    ax.scatter(e_true, e_predict, lw=0, alpha=0.5, s=10)
    ax.set_xlabel('True shear')
    ax.set_ylabel('Predicted shear')
    ax.set_xlim(0, e_max)
    ax.set_ylim(0, e_max)
    ax.plot([0, e_max], [0, e_max], 'r--')
    R2 = sklearn.metrics.r2_score(e_true, e_predict)
    ax.text(0.05, 0.9, f'{label}$R^2 = {R2:.2f}$',
            transform=ax.transAxes, fontsize=16, color='r')
