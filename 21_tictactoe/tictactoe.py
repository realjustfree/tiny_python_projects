#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-b",
                        "--board",
                        help="A named string argument",
                        metavar="str",
                        type=str,
                        default="........."    )

    parser.add_argument('-c',
                        '--cell',
                        help='A named string argument',
                        metavar='int',
                        choices=range(1,10),
                        type=int)

    parser.add_argument('-p',
                        '--player',
                        help='player',
                        metavar='str',
                        type=str,
                        default=None,
                        choices="XO")

    args = parser.parse_args()


    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both --player and --cell')

    if len(args.board) != 9 or re.search('[^OX.]', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')
    if args.player and re.search('[^OX.]', args.player):
        parser.error("must be 9 charactoer of ., X, O")

    if args.board and args.cell and args.board[args.cell-1] in 'OX':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.cell:
        temp_board = list(args.board)
        temp_board[args.cell-1] = args.player
        args.board = ''.join(temp_board)



    winner = find_winner(args.board)

    if winner:
        winner_print = f'{winner} has won!'
    else:
        winner_print = "No winner."

    print(f'''
{format_board(args.board)}
{winner_print} 
    '''.strip())

    return f'''
{format_board(args.board)}
{winner_print} 
    '''.strip()




def format_board(board):

    v=list(range(1,10))

    for i in range(9):
        if board[i] in 'OX':
            v[i] = board[i]


    board = f"""
-------------
| {v[0]} | {v[1]} | {v[2]} |
-------------
| {v[3]} | {v[4]} | {v[5]} |
-------------
| {v[6]} | {v[7]} | {v[8]} |
-------------
""".strip()

    return board


def find_winner(board):
    """winner or no winner"""

    v=list(range(1,10))

    for i in range(9):
        if board[i] in 'OX':
            v[i] = board[i]


    # 승리 8개 순서 가능
    num = [0,3,6]

    winner_value = None

    for i in num:
        if v[i] == v[i+1] == v[i+2]:
            winner_value = str(v[i])

    num = [0,1,2]
    for i in num:
        if v[i] == v[i+3] == v[i+6]:
            winner_value = str(v[i])

    if v[0] == v[4] == v[8]:
        winner_value = str(v[0])

    if v[2] == v[4] == v[6]:
        winner_value = str(v[2])

    return winner_value


# --------------------------------------------------
if __name__ == '__main__':
    main()
