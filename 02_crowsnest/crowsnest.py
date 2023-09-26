#!/usr/bin/env python3
"""
Author : lhs <lhs@localhost>
Date   : 2023-09-26
Purpose: Rock the Casbah

log
2023-09-26 19:38 : 책 2.1.8 부터 다시

"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct aritcle",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word

    print(f'Ahoy, Captain, a {word} off the larboard bow!')



# --------------------------------------------------
if __name__ == '__main__':
    main()
