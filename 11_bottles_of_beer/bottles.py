#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import random
import hashlib
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')




    return parser.parse_args()

def verse(bottle):
    """sing a verse"""
    return '\n'.join([
        f'{bottle} bottle of beer on the wall,' if bottle == 1 else f'{bottle} bottles of beer on the wall,',
        f'{bottle} bottle of beer,' if bottle == 1 else f'{bottle} bottles of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!' if bottle == 1 else f'{bottle-1} bottle of beer on the wall!\n'
    ])

# def test_verse():
#     """test verse"""
#     last_verse = verse(1)
#
#     assert last_verse == '\n'.join([
#     '1 bottle of beer on the wall,', '1 bottle of beer,',
#         'Take one down, pass it around,',
#         'No more bottles of beer on the wall!'
#     ])
#
#     two_bottles = verse(2)
#     assert two_bottles == '\n'.join([
#         '2 bottles of beer on the wall,', '2 bottles of beer,',
#         'Take one down, pass it around,', '1 bottle of beer on the wall!'
#     ])

def test_random():
    """Random number"""

    sums = dict(
        map(lambda x: x.split('\t'),
            open('sums.txt').read().splitlines()))

    print("=======test_random=====")

    for n in random.choices(list(sums.keys()), k=10):

        rand_number = random.choice([0,1])
        flag = '-n' if rand_number == 1 else '--num'
        print(f'rand_number : {rand_number:<10}, flag :{flag}')
        print(f' n : {n:<10}')
        print(f'type : {type(n)}')
        out =""
        for i in range(int(n), 0,-1):
            out+='\n'
            out+=verse(i)
        out += '\n'  # because the last newline is removed

        print(f'out : \n{out}')
        print(f'hash : {hashlib.md5(out.encode("utf-8")).hexdigest()}')
        print(f'sums : {sums[n]}')





# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()



    # for i in range(args.num,0,-1):
    #     print(verse(i))


    test_random()





# --------------------------------------------------
if __name__ == '__main__':
    main()
