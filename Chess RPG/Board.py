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

def is_blocked(board, pos1, pos2):
    for piece in board:
        pos3 = piece.position
        if (pos2[1]-pos1[1])*(pos3[0]-pos2[0]) == (pos3[1]-pos2[1])*(pos2[0]-pos1[0]):
            return True
    return False