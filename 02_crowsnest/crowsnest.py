#!/usr/bin/env python3
"""
Author : lhs <lhs@localhost>
Date   : 2023-09-26
Purpose: Rock the Casbah

log
    2023-09-26 19:38 : 책 2.1.8 부터 다시
    2023-09-27 19:44 : 2.4 going further 해야함.
        test 를 다시써야하는데 구조를 아직 모르겠음.
        일단 넘어갈 것



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

#    pre = "a"
#    if word[0].lower() in 'aeiou':
#        pre = "an"

    pre = 'an' if word[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {pre} {word} off the larboard bow!')



# --------------------------------------------------
if __name__ == '__main__':
    main()
