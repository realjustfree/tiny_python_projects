#!/usr/bin/env python3
"""
Author : lhs <lhs@localhost>
Date   : 2023-09-30
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')


    parser.add_argument('items',
                        metavar='str',
                        type=str,
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-o',
                        '--oxfordcomma',
                        help = "Option for Oxford comma",
                        action='store_false')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items_arg = args.items
    sort_arg = args.sorted
    oxfordcomma_arg = args.oxfordcomma

    # print(f'items_arg = "{items_arg}"')
    # print(f'sort_arg = "{sort_arg}"')


    if sort_arg:
        items_arg=sorted(items_arg)

    print(f'You are bringing ',end="")


    if len(items_arg) >= 3:
        # print(f'{oxfordcomma_arg}')
        items_arg[-1] = "and " + items_arg[-1]
        if oxfordcomma_arg:
            print(f'{", ".join(items_arg)}.')
        else:
            print(f'{", ".join(items_arg[:-1])} {items_arg[-1]}.')

    elif len(items_arg) >= 2:
        items_arg[-1] = "and "+items_arg[-1]
        " ".join(items_arg)
        print(f'{" ".join(items_arg)}.')

    else:
        print(f'{items_arg[-1]}')

    # for i in items_arg:
    #     if i == items_arg[-1]:
    #         print(f'and {i}.')
    #     else:
    #         print(f'{i}, ', end="")



# --------------------------------------------------
if __name__ == '__main__':
    main()
