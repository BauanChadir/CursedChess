from ChessPiece import *
from Board import*


piece1 = queen("white")
piece2 = bishop("white")

board = [piece1, piece2]

piece1.put((4, 4))

board = Board.move(board, piece1, (3,6))

print(piece1.position)
print(board.get_names)