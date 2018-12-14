import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--degree', default = 2, type = 'int')

args = parser.parse_args()

def deg(x):
    return (x**int(args.degree))
    
main()
x = int(input())
print(deg(x))
