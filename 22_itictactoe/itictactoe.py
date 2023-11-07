import random
from typing import List, NamedTuple, Optional

class State(NamedTuple):
    board: List[str] = list('.'*9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None

def format_board():
    pass

def find_winner():
    pass
def main():


if __name__ == '__main__':
    main()