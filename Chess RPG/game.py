from ChessPiece import *
from Board import*


piece1 = checkers("white")
piece2 = bishop("white")

board = [piece1, piece2]

piece2.put((1, 1))

board = Board.move(board, piece1, (2, 3))

print(piece1.position)
print(Board.get_names(board))
