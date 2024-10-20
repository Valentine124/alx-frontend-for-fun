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
    with open(argv[1], 'r') as file:
        for f in file:
            syntax = f[0:f.index(' ')]
            content = f[f.index(' ') + 1:-1]
            size = len(syntax)
            with open(argv[2], 'a') as out:
                if syntax == '#' * size:
                    out.write(f'<h{size}>{content}</h{size}>')
                    out.write('\n')
    exit(0)