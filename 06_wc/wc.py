#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('FILE',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.FILE


    num_line=0
    num_word=0
    num_byte=0

    total_num_line, total_num_word, total_num_byte = 0, 0, 0

    for fh in file_arg:
        num_line, num_word, num_byte = 0, 0, 0

        for line in fh:
            num_line += 1
            num_word += len(line.split())
            num_byte += len(line)

        print(f"{num_line:8}", end="")
        print(f'{num_word:8}', end="")
        print(f"{num_byte:8}", end=" ")
        print(f"{fh.name:8}")

        total_num_line += num_line
        total_num_word += num_word
        total_num_byte += num_byte


    if len(file_arg) > 1:
        print(f"{total_num_line:8}{total_num_word:8}{total_num_byte:8} total")





# --------------------------------------------------
if __name__ == '__main__':
    main()
