data = open("y21\\Day4\\input.txt", "r").read()

import numpy as np

def main(input):
    part1 = 0
    part2 = 0
    # Parse
    wins, *boards = input.split("\n\n")
    wins = [int(w) for w in wins.split(",")]
    boards = [np.array([[int(x) for x in l.split(" ") if x] for l in bingo.split("\n") if l]) for bingo in boards if bingo]
    print(boards)
    # Part 2
    def part2(boards):
        winningboard = None
        winnumber = 0
        for win in wins:
            print([b is None for b in boards])
            boards = [b for b in boards if b is not None]
            for i, board in enumerate(boards):
                p = np.where(board == win)
                if p[0].size > 0:
                    p = next(zip(p[0],p[1]))
                    board[p] = 0
                    if np.any(board.sum(axis=0) == 0) or np.any(board.sum(axis=1) == 0):
                        winnumber = win
                        winningboard = board
                        boards[i] = None
        return winnumber * winningboard.flatten().sum()
    return part2(boards)


print(main(data))