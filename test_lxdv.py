import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--degree', default = '2')

FLAGS = parser.parse_args()

def deg(x):
    return (x**int(FLAGS.degree))
    

if __name__ == "__main__":
    print('Server is started with following params:\n \
    degree: {0}\n \
    '.format(FLAGS.degree))
    x = int(input())
    print(deg(x))
