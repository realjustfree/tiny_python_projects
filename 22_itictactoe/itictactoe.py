import random
import re
from typing import List, NamedTuple, Optional

class State(NamedTuple):
    board: List[str] = list('.'*9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None

def format_board(board):

    cells = [str(i) if j=='.' else j for i, j in enumerate(board, start=1)]

    line = "-"*13
    board_tmpl = '| {} | {} | {} |'

    return '\n'.join([
        line,
        board_tmpl.format(*cells[:3]),
        line,
        board_tmpl.format(*cells[3:6]),
        line,
        board_tmpl.format(*cells[6:]),
        line
    ])


def find_winner(board):
    winning = [
        [0,1,2],[3,4,5], [6,7,8],
        [0,3,6],[1,4,7], [2,5,8],
        [0,4,8],[2,4,6]]

    for player in 'OX':
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player


def main():
    state = State()

    while True:
        board_now = state.board

        print(format_board(board_now))
        board_num = input(f'Player {state.player}, what is your move? [q to quit] : ')

        if board_num == 'q':
            break
        if re.search('[0-9]', board_num):
            board_now[int(board_num)-1] = state.player

            state = state._replace(board=board_now, player=change_player(state.player))


def change_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'






if __name__ == '__main__':
    main()