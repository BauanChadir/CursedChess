from ChessPiece import *
from Board import*


piece1 = banner("white")
piece2 = king("white")

board = [piece1, piece2]
Board.sync_pieces(board)

piece1.put((5, 4))
piece2.put((5, 5))

board = Board.move(board, piece1, (2, 0))

board = Board.move(board, piece2, (7, 7))
board = Board.move(board, piece2, (6, 6))
board = Board.move(board, piece2, (6, 5))
board = Board.move(board, piece2, (6, 4))
board = Board.move(board, piece2, (7, 9))
board = Board.move(board, piece2, (8, 4))

print(piece1.position)
print(piece2.position)
