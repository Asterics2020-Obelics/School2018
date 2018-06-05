import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 1, 1000)
f = 10

plt.figure()
plt.plot(t, np.sin(2 * np.pi * f * t))
plt.xlabel('$t / \mathrm{s}$')
plt.ylabel('$U / \mathrm{V}$')

plt.text(
    0.5, 1.05,
    r'$U(t) = \sin(2 \pi \nu t)$',
    va='bottom',
    ha='center'
)
plt.ylim(-1.1, 1.2)

plt.tight_layout(pad=0)
plt.savefig('plot.pdf')
