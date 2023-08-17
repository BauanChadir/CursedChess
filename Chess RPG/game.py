from ChessPiece import *
from Board import*


piece1 = rook("white")
piece2 = rook("white")

board = [piece1, piece2]

piece2.move(board, [0,4])

print(piece1.is_valid_move(board, (0, 6)))
