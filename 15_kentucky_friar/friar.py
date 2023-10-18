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
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

def fry(word):
    if re.match('[yY]ou', word):
        return word[0]+"'all"
    if re.search('(.+)ing$', word):
        match = re.search('(.+)ing$', word)
        if re.search('[aeuioAEUIO]', match.group(1)):
            return match.group(1)+"in'"
        return match.group(1)+"ing"


def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == 'swing'



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        words = []

        for word in re.split(r'(\W+)', line.rstrip()):
            words.append(fry(word))
        print("".join(words))


# --------------------------------------------------
if __name__ == '__main__':
    main()
