# School2018
2nd ASTERICS-OBELICS International School


[![School indico](https://indico.in2p3.fr/event/16864/logo-841635696.png)](https://indico.in2p3.fr/event/16864/)

This repository contains all the material needed for the [2st
ASTERICS-OBELICS International
School](https://indico.in2p3.fr/event/16864/) on "Advanced software
programming for astrophysics and astroparticle physics".

# Table on content

- [Get a copy of this repository with `git`](#repo)
- [Recommendation for Python install](#python)
    - [Linux](#linux)
    - [Mac](#mac)
    - [Windows](#windows)
    - [Library requirements](#python-req)
- [Jupyter](#jupyter)    
- [IDE: PyCharm](#pycharm)
- [Chat room](#chat)
- [Tutors](#tutors)
- [Help](#help)
- [Ressources](#ressources)


# Get a copy of this repository with `git` <a name="repo"></a>

Clone this repository on your personal computer.

      git clone https://github.com/Asterics2020-Obelics/School2018.git

You will need it before the school to install the different tools, and
during the school while attending the hands-on. For Windows, see [below](#windows).

# Recommendation for Python install <a name="python"></a> 

You must install Python 3.6 and a few Python libraries. The
recommended way to do so is to use
[Anaconda](https://www.continuum.io/downloads). The procedures described bellow will help you install what is needed for the school.
If you already have Anaconda installed, you may skip to the [Library requirements section](#req).

## Linux <a name="linux"></a>

1. Install required distribution packages :
    - Ubuntu: `sudo apt-get install -y git bzip2 wget`
    - Fedora 25: `sudo dnf install -y git wget bzip2`
    - CERN Scientific Linux 6: `sudo yum install -y git tar bzip2 wget`
    - CERN CentOS 7: `sudo yum install -y git bzip2 wget`

1. [Download](https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh)
the Linux `Anaconda` installer for Python 3.6.

1. Run the following command line:

		bash Anaconda3-5.1.0-Linux-x86_64.sh

1. Accept the License by pressing `<Enter>`, then scrolling down to the bottom using `<space>` and writing `yes`

1. Choose the install location, we recommend `~/.local/anaconda3` instead of `~/anaconda3` to not mess up you home too much.

1. After the installation, you are asked if you want to add conda to the `PATH`. Answer `no`.

    ```
    Do you wish the installer to prepend the Anaconda3 install location
    to PATH in your /home/username/.bashrc ? [yes|no]
    [no] >>> no
    ```

1. Edit your `.bashrc` to include the first or both of the following two lines  you `.bashrc`. The first line should always be added and makes the `conda` command available. The second command will make `anaconda` your default `python` in the shell, you might want to leave it out, if you use another python installation regularly.

    ```
    . "$HOME/.local/anaconda3/etc/profile.d/conda.sh"
    conda activate
    ```

Set the correct path to your anaconda installation. If you do not include the second command, you need to run `conda activate` before using python for this workshop.


See next section for extra Python libraries requirements (if any).

## Mac <a name="mac"></a>

1. [Download](https://repo.anaconda.com/archive/Anaconda3-5.1.0-MacOSX-x86_64.sh)
the Mac `Anaconda` installer for Python 3.6.

1. Run the following command line:

		bash Anaconda3-5.1.0-MacOSX-x86_64.sh

1. Accept the License by pressing `<Enter>`, then scrolling down to the bottom using `<space>` and writing `yes`

1. Choose the install location, we recommend `~/.local/anaconda3` instead of `~/anaconda3` to not mess up your home too much.

1. After the installation, you are asked if you want to add conda to the `PATH`. Answer `no`.
```
Do you wish the installer to prepend the Anaconda3 install location
to PATH in your /home/username/.bashrc ? [yes|no]
[no] >>> no
```

1. Edit your `.bash_profile` to include the first or both of the following two lines  you `.bash_profile`. The first line should always be added and makes the `conda` command available. The second command will make `anaconda` your default `python` in the shell, you might want to leave it out, if you use another python installation regularly.
```
. "$HOME/.local/anaconda3/etc/profile.d/conda.sh"
    conda activate
```             
Set the correct path to your anaconda installation. If you do not include the second command, you need to run `conda activate` before using python for this workshop.


See next section for extra Python libraries requirements (if any).

## Windows <a name="windows"></a>

Instruction for Windows can be found
[here](https://www.continuum.io/downloads#windows) for the installation of Anaconda. Once installed, you can run `Anaconda navigator`. To run Jupyter, on the main page of the Anaconda navigator, click on `Launch` on the Jupyter notebook box. This will open your favorite browser. From there, you can either load a notebook (e.g. from the Git folder) or create a new notebook by clicking `new -> Python 3`.

You can also install a Git tool for Windows: [Git for Windows](https://git-for-windows.github.io/). Launch `Git GUI` or `Git bash` to get started.

## Library requirements <a name="req"></a>

We will use a common environment all along the school.
First of all, update conda to be able to use the latest features:
```
conda update conda
```
To create it, you just need to run:
```
conda env create -f environment.yml
```

If after the creation the file environment.yml was updated, you could update your installation with:
```
conda env update -f environment.yml
```

Once the environment has been created and all dependencies installed, you may activate it with (you will need to do that every time you want to use this environment):
```
conda activate school18
```

> Note that if you haven't followed the [Anaconda installation](#python) or have an Anaconda version < 4.4, you will have to run
```
source activate school18
```


# Jupyter <a name="jupyter"></a>

To launch a Jupyter notebook, simply run the following command:

`jupyter notebook`

On Windows, see in the [above](#windows).

# IDE: PyCharm <a name="pycharm"></a>

We recommend to use pycharm. Free Community Edition: [Download PyCharm](https://www.jetbrains.com/pycharm/download) or opt for a free copy of the Professional Edition under [Student License](https://www.jetbrains.com/student/).

# Chat rooms <a name="chat"></a>

[Slack chat rooms](https://obelics-school2018.slack.com/) are available before, during and after the school (you should have received an email with an invitation). If you need to talk to each other during a session, share information, ask questions, you can use the corresponding chat rooms to do so. These chat rooms can also be used by the different tutors to give information or advices before or during the hands-on sessions. You can also start one-to-one chat rooms.

Several channels are available, like *General* for all discussion/questions about the school, lectures, hands-on, etc. There is also a channel *Social* to help you to get out together during the evening.

You can get the slack app directly on your phone: [Android](https://play.google.com/store/apps/details?id=com.Slack) or [Apple](https://itunes.apple.com/fr/app/slack/id618783545?mt=8). You can also get it for Windows, Mac, or Linux [here](https://slack.com).

# Tutors <a name="tutors"></a>

The full list of tutors is available [here](https://indico.in2p3.fr/event/16864/page/1846-list-of-tutors).

Here is the list of tutors for the hands-on sessions, with the additional tutors that would circulate to help participants during the exercises and hands-on.

| Hands-on               | Main tutor(s)              | Additional tutors                                                    |
| ---------------------- |----------------------------|----------------------------------------------------------------------|
| Efficient code design  | Tammo Jan Dijkema, Zheng Meyer|                                                                   |
| Git                    | Kai Bruegge, Maximilian Nöthe|                                                                    |
| Numpy                  | Tamas Gal                  | Frederic Gillardo                                                    |
| Pandas                 | Tamas Gal                  | Frederic Gillardo                                                    |
| Scipy                  | Kai Bruegge, Maximilian Nöthe|                                                                    |
| PyVO                   | Hendrik Heinl              |                                                                      |
| Debugging & Profiling  | Christoph Deil             |                                                                      |
| Astropy                | Axel Donath, Christoph Deil |                                                                     |
| Machine learning       | David Kirkby               | Kai Bruegge, Thomas Vuillaume, Mikaël Jacquemont                     |

# Help <a name="help"></a>

Please create a [new
issue](https://github.com/Asterics2020-Obelics/School2018/issues) (you
will need a github account) for each question you may have before or
during the school about software install and/or about one of the
classes. Of course, you should first check the existing list of issues
to see if your question has already been asked and answered before
creating a new one.

Alternatively, use the [chat rooms](#chat).

# Ressources <a name="ressources"></a>

2017 edition of the school: [program](https://indico.in2p3.fr/event/14227/timetable/#20170606) and [github](https://github.com/Asterics2020-Obelics/School2017)

Complete Python tutorials:
 * [Python for Scientific Computing](http://bender.astro.sunysb.edu/classes/python-science/)
 * [A Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
 * [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)

 Workshops:
 * [Python for Astronomers and Particle Physicists](https://www.ice.csic.es/indico/event/5/overview) ([github](https://github.com/Python4AstronomersAndParticlePhysicists/PythonWorkshop-ICE))
