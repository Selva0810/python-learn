
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

'''
import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = ['1','2','3','4','5','6','7','8','9','.']

        for row in range(9):
            for col in range(9):
                if board[row][col] not in check:
                    return False

                for r1 in range(row+1,9):
                    if board[row][col] == board[r1][col] and board[row][col] != '.':
                       # print ("1")
                       # print (board[row][col] ,board[r1][col])
                        return False

                for c1 in range(row+1,9):
                    if board[col][row] == board[col][c1] and board[col][row] != '.':
                       # print ("2")

                        #print (board[col][row] ,board[col][c1])
                        return False

                start_row = row - row % 3
                start_col = col - col % 3

                for r in range(0, 3):
                    for c in range(0, 3):

                       # print(row, col, r + start_row, c + start_col)
                        curr = board[r + start_row][c + start_col]

                        if board[row][col] == curr and board[row][col] != '.' and not (row == r + start_row) and not (
                                col == c + start_col):
                            #print("3")

                           # print(row, col, r + start_row, c + start_col)
                            return False

        return True

    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c, j), (i, c), (i // 3, j // 3, c)]
        return len(seen) == len(set(seen))

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        cubes = collections.defaultdict(set)

        def validLine(i):
            numset = set()
            line = board[i]
            for j, c in enumerate(line):
                if c == '.':
                    continue
                if c in numset:
                    return False
                numset.add(c)
            return True

        def validColumn(j):
            numset = set()
            for i in range(len(board)):
                c = board[i][j]
                if c == '.':
                    continue
                if c in numset:
                    return False
                numset.add(c)
            return True

        def validCube(i, j):
            n = 3 * (i // 3) + (j // 3)
            print (n)
            c = board[i][j]
            if c in cubes[n]:
                return False
            cubes[n].add(c)
            print (cubes)
            return True

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == '.':
                    continue
                if not validLine(x) or not validColumn(y) or not validCube(x, y):
                    return False
        return True

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","9",".",".","2"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]


s = Solution()
print(s.isValidSudoku(board))

print(s.isValidSudoku1(board))

print(s.isValidSudoku2(board))
