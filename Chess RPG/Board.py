import math

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

def are_touching(board, piece1, piece2):
    piece1.position = position1
    piece2.position = position2
    if (position1[0]-1 <= position2[0] <= position1[0]+1) and (position1[1]-1 <= position2[1] <= position1[1]+1):
        return True
    return False

def are_touching_othogonally(board, piece1, piece2):
    piece1.position = position1
    piece2.position = position2
    if (position1[0]-1 <= position2[0] <= position1[0]+1) != (position1[1]-1 <= position2[1] <= position1[1]+1):
        return True
    return False

def move(board, piece, endpos):

    can_because_of_buff = False

    for buff in piece.movement_buff:
        if buff.piece.is_valid_move(board, endpos):
            can_because_of_buff = True

    if (not piece.is_valid_move(board, endpos)) and (not can_because_of_buff):
        print("Move from " + str(piece.position) + " to " + str(endpos) + " is not valid for " + str(piece.name))
        return

    board = piece.on_move(board, endpos)

    for potentually_captured_piece in board:
        if potentually_captured_piece.position == endpos:
            board.remove(potentually_captured_piece)
            break

    piece.position = endpos
    return board

def get_names(board):
    l = []
    for piece in board:
        l.add(piece.name)
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