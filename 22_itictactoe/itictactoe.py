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

    #check_not_empty = [1 if i=='.' else 0 for i in board]

    #if sum(check_not_empty) == 0:
    #    return "full"



    for player in 'OX':
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player


def main():
    state = State()

    while True:
        board_now = state.board

        print("\033[H\033[J") # terminal 화면 초기화
        print(format_board(board_now))

        if find_winner(board_now):
            #if find_winner(board_now) == 'full':
            #    print("Draw")
            #    break

            print(f'{find_winner(board_now)} has won!')
            break


        board_num = input(f'Player {state.player}, what is your move? [q to '
                          f'quit] : ')


        if board_num == 'q':
            break
        if re.search('^[0-9]{1}$', board_num):
            if board_now[int(board_num)-1] in 'OX':
                print(f'Cell "{board_num}" already taken.')
            else:
                board_now[int(board_num)-1] = state.player
                state = state._replace(board=board_now, player=change_player(state.player))
        else:
            print(f'Invalid cell "{board_num}", please use 1-9')









def change_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'






if __name__ == '__main__':
    main()