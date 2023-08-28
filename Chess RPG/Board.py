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
    p1 = ChessPiece.rook("white")
    p1.put([0, 0])
    board.append(p1)
    p2 = ChessPiece.rook("white")
    p2.put([0, 7])
    board.append(p2)
    p3 = ChessPiece.bishop("white")
    p3.put([0, 2])
    board.append(p3)
    p4 = ChessPiece.bishop("white")
    p4.put([0, 5])
    board.append(p4)
    p5 = ChessPiece.knight("white")
    p5.put([0, 1])
    board.append(p5)
    p6 = ChessPiece.knight("white")
    p6.put([0, 6])
    board.append(p6)
    p7 = ChessPiece.king("white")
    p7.put([0, 4])
    board.append(p7)
    p8 = ChessPiece.queen("white")
    p8.put([0, 3])
    board.append(p8)
    p9 = ChessPiece.pawn("white")
    p9.put([1, 0])
    board.append(p9)
    p11 = ChessPiece.pawn("white")
    p11.put([1, 1])
    board.append(p11)
    p22 = ChessPiece.pawn("white")
    p22.put([1, 2])
    board.append(p22)
    p33 = ChessPiece.pawn("white")
    p33.put([1, 3])
    board.append(p33)
    p44 = ChessPiece.pawn("white")
    p44.put([1, 4])
    board.append(p44)
    p55 = ChessPiece.pawn("white")
    p55.put([1, 5])
    board.append(p55)
    p66 = ChessPiece.pawn("white")
    p66.put([1, 6])
    board.append(p66)
    p77 = ChessPiece.pawn("white")
    p77.put([1, 7])
    board.append(p77)
    p88 = ChessPiece.pawn("black")
    p88.put([6, 0])
    board.append(p88)
    p99 = ChessPiece.pawn("black")
    p99.put([6, 1])
    board.append(p99)
    p00 = ChessPiece.pawn("black")
    p00.put([6, 2])
    board.append(p00)
    p111 = ChessPiece.pawn("black")
    p111.put([6, 3])
    board.append(p111)
    p222 = ChessPiece.pawn("black")
    p222.put([6, 4])
    board.append(p222)
    p333 = ChessPiece.pawn("black")
    p333.put([6, 5])
    board.append(p333)
    p444 = ChessPiece.pawn("black")
    p444.put([6, 6])
    board.append(p444)
    p555 = ChessPiece.pawn("black")
    p555.put([6, 7])
    board.append(p555)
    p666 = ChessPiece.rook("black")
    p666.put([7, 7])
    board.append(p666)
    p777 = ChessPiece.rook("black")
    p777.put([7, 0])
    board.append(p777)
    p888 = ChessPiece.bishop("black")
    p888.put([7, 2])
    board.append(p888)
    p999 = ChessPiece.bishop("black")
    p999.put([7, 5])
    board.append(p999)
    p000 = ChessPiece.knight("black")
    p000.put([7, 6])
    board.append(p000)
    p12 = ChessPiece.knight("black")
    p12.put([7, 1])
    board.append(p12)
    p13 = ChessPiece.king("black")
    p13.put([7, 4])
    board.append(p13)
    p14 = ChessPiece.queen("black")
    p14.put([7, 3])
    board.append(p14)

    return board


