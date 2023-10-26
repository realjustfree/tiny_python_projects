#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        type = argparse.FileType('rt'),
                        metavar='FILE',
                        help='Input file')

    parser.add_argument('-i',
                        '--input',
                        help='Inputs (for testing)',
                        nargs='*',
                        type=str,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    text = args.FILE.read()

    match = re.findall('(<([^<>])+>)', text)

    if not match:
        print(f'"{args.FILE.name}" has no placeholders.')
        sys.exit(1)

    for i in args.input:
        text=re.sub('<[^<>]+>', i, text, count=1)

    print(''.join(text).strip())










# --------------------------------------------------
if __name__ == '__main__':
    main()
