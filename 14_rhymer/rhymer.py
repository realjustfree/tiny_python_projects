#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        type=str,
                        metavar='str',
                        help='A word to rhyme')
    args = parser.parse_args()

    if os.path.isfile(args.word):
        args.word = open(args.word).read().rstrip()

    return args


# --------------------------------------------------
def stemmer(word):
    """Return leading consonats (if any), and 'stem' of word"""
    consonants = ''.join([c for c in string.ascii_lowercase if not c in "aeiou"])

    match = re.match(f'([{consonants}]+)?([aeiuo])(.*)', word.lower(), re.IGNORECASE)

    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1,p2,p3)
    else:
        return (word,'')


def change_consonants(word):
    """change consonants"""
    consonants = [c for c in string.ascii_lowercase if not c in "aeiou"]
    add_consonants = ["bl","br","ch","cl","cr", "dr","fl","fr","gl", "gr", "pl", "pr", "sc", "sh",
                      "sk", "sl", "sm", "sn", "sp", "st", "sw", "th", "tr", "tw", "thw", "wh", "wr",
                      "sch","scr", "shr", "sph", "spl", "spr", "squ", "str", "thr"]

    consonants += add_consonants

    word = list(word)

    if len(word) == 2:
        return 'err'

    new_word = []

    for c in consonants:
        if word[0] != c:
            word[0] = c
            new_word.append(''.join(word))

    return new_word



def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer("RDNZL") == ('rdnzl', '')
    assert stemmer('123') == ('123', "")


def main():
    """Make a jazz noise here"""

    args = get_args()
    stem_consonants=stemmer(args.word)
    last_consonants = change_consonants(stem_consonants)

    if last_consonants == 'err':
        print(f'Cannot rhyme "{args.word}"')
    else:

        for c in last_consonants:
            print(c)






# --------------------------------------------------
if __name__ == '__main__':
    main()
