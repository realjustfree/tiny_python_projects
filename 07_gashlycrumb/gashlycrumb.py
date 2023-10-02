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
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("letter", metavar="letter", help="Letter(s)", nargs="+")

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letter_arg = args.letter
    file_arg = args.file

    text_dict={}
    for line in file_arg:
        line_temp = []
        line_temp = line.split()
        text_dict[line_temp[0]] = " ".join(line_temp)

    for char in letter_arg:
        if not char.upper() in text_dict.keys():
            print(f'I do not know \"{char}\".')
        else:
            print(f'{text_dict[char.upper()]}')




# --------------------------------------------------
if __name__ == "__main__":
    main()
