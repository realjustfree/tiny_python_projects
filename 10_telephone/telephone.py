#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type = str,
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if not (args.mutations <= 1 and args.mutations >= 0):
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    num_mutation = round(len(args.text) * args.mutations)
    alpha = "".join(sorted(string.ascii_letters + string.punctuation))

    """text 변환"""
    len_text = len(args.text)
    num_rand = random.sample(range(len_text), num_mutation)
    trans_text = args.text

    for i in num_rand:
        rand_alpha = random.choice(alpha)

        if trans_text[i] == rand_alpha:
            rand_alpha = random.choice(alpha)

        if trans_text[i] == " ":
            i += 1

        trans_text = trans_text[:i] + rand_alpha + trans_text[i+1:]


    print(f'You said: "{args.text}"')
    print(f'I heard : "{trans_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
