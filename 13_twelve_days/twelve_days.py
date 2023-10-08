#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import sys



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)


    args = parser.parse_args()

    if args.num <0 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')


    return args

def verse(num):

    verse_dict={1: "first",
                2: "second",
                3: "third",
                4: "fourth",
                5: "fifth",
                6: "sixth",
                7: "seventh",
                8: "eighth",
                9: "ninth",
                10: "tenth",
                11: "eleventh",
                12: "twelfth"
                }

    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]



    if num == 1:
        verse = [f"On the {verse_dict[num]} day of Christmas,", f"My true love gave to me,"]
        verse.append(f'{gifts[num-1]}')


    else:
        verse = [f"\nOn the {verse_dict[num]} day of Christmas,", f"My true love gave to me,"]
        for i in reversed(range(1, num+1)):
            if i == 1:
                verse.append('And a partridge in a pear tree.')
            else:
                verse.append(f'{gifts[i-1]}')

    return "\n".join(verse)




# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    for day in range(1, args.num+1):
        print(verse(day), file=args.outfile)


def test_verse():
    assert verse(1) == 'On the first day of Christmas,'
    assert verse(2) == 'On the second day of Christmas,'






# --------------------------------------------------
if __name__ == '__main__':
    main()
