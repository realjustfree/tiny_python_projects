#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import random
import sys
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input files(s)',
                        metavar='FILE',
                        nargs="+",
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    args = parser.parse_args()

    if args.num <= 0:
        sys.exit()

    return args

def clean(word):
    return re.sub('[^A-Za-z0-9]',"",word)

def ransom(word):
    return ''.join([char.upper() if random.choice([0,1]) else char.lower() for char in word])

def l33t(word):
    jump = {"a":"@", "A":"4", "O":"0", "t":"+", "E":"3", "I":"1","S":"5"}

    new_word= ''.join([ransom(char) for char in word])

    return ''.join([jump.get(char) if jump.get(char) else char for char in new_word])+random.choice(string.punctuation)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len


    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.title().split())):
                words.add(word)

    words = sorted(words)

    for _ in range(args.num):
        random_word = random.sample(words, args.num_words)
        random_word_list = [ransom(word) for word in random_word]

        if args.l33t:
            random_word_list_l33t = [l33t(word) for word in random_word]

            print(''.join(random_word_list_l33t))


        else: print(''.join(random_word_list))






# --------------------------------------------------
if __name__ == '__main__':
    main()
