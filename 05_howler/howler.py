#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os.path


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Inputs string of file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text
    outfile_arg = args.outfile

    if outfile_arg:
        if os.path.isfile(text_arg):
            old_file = open(text_arg).read().upper()
            new_file = open(outfile_arg,'wt')
            new_file.write(old_file)
            new_file.close()
        else:
            new_file = open(outfile_arg, "wt")
            new_file.write(text_arg.upper())
            new_file.close()
    else:
        if os.path.isfile(text_arg):
            open(text_arg).read().upper()
        else:
            print(text_arg.upper())




# --------------------------------------------------
if __name__ == '__main__':
    main()
