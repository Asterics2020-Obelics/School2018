#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Example with non-optional arguments')

parser.add_argument('count', type=int)
parser.add_argument('units')

print(parser.parse_args())
