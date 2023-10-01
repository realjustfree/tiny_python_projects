#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    parser.add_argument('-t',
                        '--text',
                        help='change to text',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.str
    text_arg = args.text

    trance_dial = {'1':'9', '2':'8', '3':'7','4':'6',
                   '5':'0', '6':'4', '7':'3', '8':'2',
                   '9':'1', '0':'5'}

    trance_text = {'1':'One', '2':'two', '3':'three','4':'four',
                   '5':'five', '6':'six', '7':'seven', '8':'eight',
                   '9':'nine', '0':'zero'}

    number=""
    number2=[]

    if text_arg:
        print(str_arg.translate(str.maketrans(trance_text)))

    else:
        for char in str_arg:
            if trance_dial.get(char):
                print(trance_dial[char], end="")
            else :
                print(char, end="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
