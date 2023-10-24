#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args



def scramble(word):
    """scramble a word"""

    if len(word) > 3 and re.match(r'\w+', word):
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0]+''.join(middle) +word[-1]
    return word


    # if len(word) == 1 or word=="":
    #     return word
    #
    # for word in splitter.split(word):
    #     word = list(word)
    #
    #     word_shuffle = word[1:-1]
    #     random.shuffle(word_shuffle)
    #     word_shuffle = ''.join(word_shuffle)
    #     return word[0]+word_shuffle+word[-1]

def test_scramble():
    """test scramble"""
    state = random.getstate()
    random.seed(1)

    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"

    random.setstate(state)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    for line in args.text.splitlines():
        print(''.join(map(scramble, splitter.split(line))))






# --------------------------------------------------
if __name__ == '__main__':
    main()
