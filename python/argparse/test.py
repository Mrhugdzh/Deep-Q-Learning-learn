import argparse

parse=argparse.ArgumentParser()

parse.add_argument('-o', '--output', action='store_true', help='show output')

args=parse.parse_args()

if args.output:
    print('this is some output')

# parse=argparse.ArgumentParser()

# parse.add_argument('-v', type=int, required=True, metavar='value', help='ssss')

# args=parse.parse_args()

# print(args)

# val=args.v

# print(val*val*val)

parser=argparse.ArgumentParser()
parser.add_argument('--name', required=True)

args=parser.parse_args()
print(f'Hello ', args.name)