#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import re



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"

def word2num(vals):
    vals = re.sub('[^a-zA-Z0-9]', '', vals)
    vals_value = str(sum([ord(i) for i in vals]))
    return vals_value




# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    for line in args.text.splitlines():
        word_list=[]
        for word in line.split():
            word_list.append(word2num(word))
        print(' '.join(word_list))





# --------------------------------------------------
if __name__ == '__main__':
    main()
