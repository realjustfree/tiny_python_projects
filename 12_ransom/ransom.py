#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def choose(char):
    return char.upper() if random.choice([False,True]) else char.lower()


def test_chose():
    state = random.getstate()
    random.seed(1)

    assert choose("a") == 'a'
    assert choose("b") == 'b'
    assert choose("c") == 'C'
    assert choose("d") == 'd'

    random.setstate(state)
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)


# for ver.
#     new_word = ""
#     for i in args.text:
#         new_word += choose(i)
#
# # list comprehension ver.
#     new_word = "".join(choose(i) for i in args.text)
#

# map() ver.
    new_word= map(choose, args.text)

    print("".join(new_word))




# --------------------------------------------------
if __name__ == '__main__':
    main()
