#!/usr/bin/env python

import numpy as np

# h5py with numpy >= 1.14 prints an error message on importing, suppress it
np.warnings.filterwarnings('ignore')
import h5py
import sys
import argparse


def print_node(node, indent=4):
    """Print string representation of a node of a tree

    Args:
        node: path in a tree
        indent: the number of spaces to indent with each level

    Returns:
        string representation of this path

    Examples:
        >>> print_node("a/b/c")
                c
        >>> print_node("a/b")
            b
        >>> print_node("c")
        c
    """
    *path, name = str(node).split('/')
    print(' ' * indent * len(path) + name)


def print_h5(h5filename, *, indent=4):
    """Print the contents of an HDF5 file"""
    h5file = h5py.File(h5filename)
    h5file.visit(lambda node: print_node(node, indent=indent))


def main():
    parser = argparse.ArgumentParser(description="Print contents of an HDF5 file.")
    parser.add_argument("filename", help="HDF5 file name")
    parser.add_argument("-i", "--indent", help="Indentation level",
                        default=4, type=int)
    args = parser.parse_args()

    print_h5(args.filename, indent=args.indent)


if __name__ == '__main__':
    a = 42
    "a is {:42}".format(a)
    main()
