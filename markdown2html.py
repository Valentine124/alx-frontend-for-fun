#!/usr/bin/python3
"""Script for HTML markdown"""


if __name__ == '__main__':
    from sys import argv, exit, stderr
    from os.path import exists

    if len(argv) < 2:
        print(f'Usage: {argv[0]} README.md README.html', file=stderr)
        exit(1)
    if not(exists(argv[1])):
        print(f'Missing {argv[1]}')
        exit(1)
    with open(argv[2], 'w') as file:
        pass
    exit(0)