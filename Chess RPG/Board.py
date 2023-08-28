import math
import ChessPiece

board_size_x = 8
board_size_y = board_size_x

def has_obstacle(board, pos):
    for piece in board:
        if piece.position == pos:
            return True
    return False

def get(board, pos):
    for piece in board:
        if piece.position == pos:
            return piece
        return None

def are_touching(piece1, piece2):
    position1 = piece1.position
    position2 = piece2.position
    if (position1[0]-1 <= position2[0] <= position1[0]+1) and (position1[1]-1 <= position2[1] <= position1[1]+1):
        return True
    return False

def are_touching_othogonally(board, piece1, piece2):
    position1 = piece1.position
    position2 = piece2.position
    if (position1[0]-1 <= position2[0] <= position1[0]+1) != (position1[1]-1 <= position2[1] <= position1[1]+1):
        return True
    return False

def move(board, piece, endpos):

    can_because_of_buff = False

    for buff in piece.movement_buff:
        if buff.piece.is_valid_move(board, endpos):
            can_because_of_buff = True

    if (not piece.is_valid_move(board, endpos)) and (not can_because_of_buff):
        print("Move from " + str(piece.position) + " to " + str(endpos) + " is not valid for " + str(piece.type))
        return board

    board = piece.on_move(board, endpos)

    for potentually_captured_piece in board:
        if potentually_captured_piece.position == endpos:
            board.remove(potentually_captured_piece)
            break

    piece.position = endpos
    return board

def get_names(board):
    l = []
    for x in board:
        l.append(x.type)
    return l

def is_blocked(board, pos1, pos2):
    for piece in board:
        pos3 = piece.position
        dist1 = pythagoras(pos1[0] - pos2[0], pos1[1] - pos2[1])
        dist2 = pythagoras(pos1[0] - pos3[0], pos1[1] - pos3[1])

        is_on_a_line = (pos2[1]-pos1[1])*(pos3[0]-pos2[0]) == (pos3[1]-pos2[1])*(pos2[0]-pos1[0])
        is_closer = dist1 > dist2
        not_start_or_target = pos3 != pos1 and pos3 != pos2

        if (not_start_or_target and is_closer and is_on_a_line):
            return True
    return False

def pythagoras(x,y):
    return math.sqrt(x**2 + y**2)

def defaultSetup():
    board = []
    board.append(ChessPiece.rook("white").put([0, 0]))
    board.append(ChessPiece.rook("white").put([7, 0]))
    board.append(ChessPiece.bishop("white").put([2, 0]))
    board.append(ChessPiece.bishop("white").put([5, 0]))
    board.append(ChessPiece.knight("white").put([1, 0]))
    board.append(ChessPiece.knight("white").put([6, 0]))
    board.append(ChessPiece.king("white").put([4, 0]))
    board.append(ChessPiece.queen("white").put([3, 0]))

    board.append(ChessPiece.pawn("white").put([0, 1]))
    board.append(ChessPiece.pawn("white").put([1, 1]))
    board.append(ChessPiece.pawn("white").put([2, 1]))
    board.append(ChessPiece.pawn("white").put([3, 1]))
    board.append(ChessPiece.pawn("white").put([4, 1]))
    board.append(ChessPiece.pawn("white").put([5, 1]))
    board.append(ChessPiece.pawn("white").put([6, 1]))
    board.append(ChessPiece.pawn("white").put([7, 1]))

    board.append(ChessPiece.pawn("black").put([0, 6]))
    board.append(ChessPiece.pawn("black").put([1, 6]))
    board.append(ChessPiece.pawn("black").put([2, 6]))
    board.append(ChessPiece.pawn("black").put([3, 6]))
    board.append(ChessPiece.pawn("black").put([4, 6]))
    board.append(ChessPiece.pawn("black").put([5, 6]))
    board.append(ChessPiece.pawn("black").put([6, 6]))
    board.append(ChessPiece.pawn("black").put([7, 6]))

    board.append(ChessPiece.rook("black").put([7, 7]))
    board.append(ChessPiece.rook("black").put([0, 7]))
    board.append(ChessPiece.bishop("black").put([2, 7]))
    board.append(ChessPiece.bishop("black").put([5, 7]))
    board.append(ChessPiece.knight("black").put([6, 7]))
    board.append(ChessPiece.knight("black").put([1, 7]))
    board.append(ChessPiece.king("black").put([4, 7]))
    board.append(ChessPiece.queen("black").put([3, 7]))

    return board


