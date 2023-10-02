#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')


    parser.add_argument('-v',
                    '--vowel',
                        type=str,
                    choices=["a","e","i","o","u"],
                    help='The vowel to substitute',
                    default="a")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text
    vowel_arg = args.vowel

    if vowel_arg:
        for char in "aeiou":
            text_arg= text_arg.replace(char, vowel_arg)
        for char in "AEIOU":
            text_arg = text_arg.replace(char, vowel_arg.upper())

    else:
        for char in "aeiou":
            text_arg= text_arg.replace(char, "a")
        for char in "AEIOU":
            text_arg = text_arg.replace(char, "a".upper())

    print(f'{text_arg}')





# --------------------------------------------------
if __name__ == '__main__':
    main()
