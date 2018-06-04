import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b')
parser.add_argument('-c', type=int)

print(parser.parse_args())
