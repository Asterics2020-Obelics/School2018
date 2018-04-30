# Python debugging and profiling

This directory contains all materials for the Python
debugging and profiling tutorial by [Christoph Deil](https://github.com/cdeil).

## Introduction

Python is usually known and loved for it's simplicity.
Languages like C, C++ and Java with their static types can be tedious,
while other languages like Perl, Javascript or Ruby with dynamic types
often take things too far and invite you to shoot yourself in the foot
(see [wat](https://www.destroyallsoftware.com/talks/wat) by Gary Bernhardt ).

But, if we're honest, Python is at the core also a complex dynamic language with plenty
of room to write code that doesn't do what it's supposed to do or runs
very slowly. In this tutorial, we will introduce some common tools for
**debugging** and **profiling** Python code, i.e. techniques that
will help you interactively figure out wat is going on.

We will do a series of short segments, where I always first explain and demo
something, and then you try it out. The level will be very basic, I assume
you have written and run Python code before, but never used a debugger or profiler.
There is not enough time to go into details, so the goal here is rather to
show very simple examples involving Python functions that process lists, dicts and Numpy arrays,
and to introduce the most common ways to debug and profile such code.


## Prepare

To prepare, please come with your laptop and the following installed:
Python 3.6, Numpy, IPython terminal, Jupyter notebook, PyCharm,
[line_profiler](https://github.com/rkern/line_profiler)
[memory_profiler](https://github.com/pythonprofilers/memory_profiler),
[snakeviz](https://github.com/jiffyclub/snakeviz),
[psrecord](https://github.com/astrofrog/psrecord)

Generally, a good understanding of how Python itself and the data structures you use work are often helpful or even
required to be able to debug or profile and optimise a piece of Python code.

If you're new to Python or Numpy and want to prepare for this tutorial, I'd recommend you start by
reading the section on [Python built-in data structures](http://nbviewer.jupyter.org/github/jakevdp/WhirlwindTourOfPython/blob/master/06-Built-in-Data-Structures.ipynb)
from the [Whirlwind tour or Python](http://nbviewer.jupyter.org/github/jakevdp/WhirlwindTourOfPython/blob/master/Index.ipynb)
by Jake VanderPlas. The sections on [understanding data types](https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html)
and [basics of Numpy arrays](https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html)
from the [Python data science handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake are also excellent.
In the tutorial, I will assume that you know about Python functions, dict, list and Numpy arrays and use those in the debugging and profiling examples.
If you want to learn in detail how Python variables, functions and classes work, the 
[Python epiphanies](https://nbviewer.jupyter.org/github/oreillymedia/python_epiphanies/blob/master/Python-Epiphanies-All.ipynb)
notebook by Stuart Williams is a nice resource.

Another good resource is the slides on
[debugging](https://github.com/Asterics2020-Obelics/School2017/blob/master/talks/d1-03-Debugging-KarlKosack.pdf)
and [profiling](https://github.com/Asterics2020-Obelics/School2017/blob/master/talks/d1-04-ProfilingAndOptimization-KarlKosack.pdf)
as well as the corresponding [hand-on materials](https://github.com/Asterics2020-Obelics/School2017/tree/master/profiling_debugging)
by Karl Kosack from the 2017 school. The tutorial this year (2018) will be more focused on the basics,
targeted to people that have never debugged or profiled Python before. Given that we only have two hours
in total, we will also not cover how to optimise code using Cython or Numba.


## Tutorial

I will develop and put materials for this tutorial here before the school.
At the moment, this is just some notes for myself ...

Roughly, the plan is to do one hour on debugging first, and then one hour on profiling.

For debugging, we'll start with the [Python built-in tools for debugging and profiling]
(https://docs.python.org/3/library/debug.html) and use `pdb` to learn about stack frames
and tracebacks. We'll then move on how debug with `ipython`, `jupyter` and finally `PyCharm`.

For profiling, we will start with [psrecord](https://github.com/astrofrog/psrecord) to see
how much time and memory a given script needs, and then explore the tools that allow you
to drill down and find the performance bottlenecks, using `timeit`, `profile`, `snakeviz`,
`line_profiler` and a little bit of memory profiling.

As example data, we will use simple event list tabular data as it is found in high-level
gamma-ray astronomy (read via Astropy Table), and represent it using Python lists, dicts and Numpy arrays.
