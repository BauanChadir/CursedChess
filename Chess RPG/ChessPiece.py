import Board

class ChessPiece:

    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.position = (0, 0)
        self.movement_buffs = []

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def is_valid_move(self, board, new_position):
        if not (0 <= new_position[0] < Board.board_size_x or 0 <= new_position[1] < Board.board_size_y) or (new_position == self.position):
            return False
        if self.is_valid_move_inner(board, new_position):
            return True
        else:
            for buff in self.movement_buffs:
                if buff(board, new_position, self.position):
                    return True
        return False

    def is_valid_move_start_to_end(self, board, new_position, starting_pos):
        saved_pos = self.position
        self.position = starting_pos
        to_return = self.is_valid_move(board, new_position)
        self.position = saved_pos
        return to_return

    def is_valid_move_inner(self, board, new_position):
        return (0 <= new_position[0] < Board.board_size_x and 0 <= new_position[1] < Board.board_size_y) and not (new_position == self.position)

    def on_move(self, board, target_pos):
        return board

    def put(self, new_position):
        self.position = new_position

    def generate_buff(self):
        return lambda board, starting_position, new_position: self.is_valid_move_start_to_end(board, new_position, starting_position)

    def sync(self, board):
        return

class HybridPiece(ChessPiece):
    def __init__(self, color, name, *pieces):
        super().__init__(color, name)
        self.pieces = pieces


    def is_valid_move_inner(self, board, new_position):
        for piece in self.pieces:
            if piece.is_valid_move_start_to_end(board, new_position, self.position):
                return True
        return False


class rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "Rook")

    def is_valid_move_inner(self, board, new_position):
        if (new_position[0] == self.position[0] or new_position[1] == self.position[1]) and not Board.is_blocked(board, self.position, new_position):
            return True
        return False

class knight(ChessPiece):
    def __init__(self,color):
        super().__init__(color, "Knight")
        
    def is_valid_move_inner(self, board, new_position):
        if abs(new_position[0] - self.position[0]) == 2 and abs(new_position[1]-self.position[1]) == 1:
            return True
        elif abs(new_position[0]-self.position[0]) == 1 and abs(new_position[1] - self.position[1]) == 2:
            return True
        return False
    
class bishop(ChessPiece):
    def __init__ (self, color):
        super().__init__(color, "Bishop")
    
    def is_valid_move_inner(self, board, new_position):
        delta_x = new_position[0] - self.position[0]
        delta_y = new_position[1] - self.position[1]
        
        steps = abs(delta_x)
        if steps != abs(delta_y) or Board.is_blocked(board, self.position, new_position):
            return False
        return True

class king(ChessPiece):
    def __init__ (self, color):
        super().__init__(color, "King")

    def is_valid_move_inner(self, board, new_position):
        if (self.position[0]-1 <= new_position[0] <= self.position[0]+1) and (self.position[1]-1 <= new_position[1] <= self.position[1]+1):
            return True
        return False

class pawn(ChessPiece):
    def __init__(self,color):
        super().__init__(color, "Pawn")
    
    def is_valid_move_inner(self, board, new_position):
        if self.color == "white":
            if not Board.has_obstacle(new_position):
                if new_position[0] == self.position[0] + 1 and new_position[1] == self.position[1]:
                    return True
                if self.position[0] == 1 and new_position[0] == self.position[0]+2 and new_position[1] == self.position[1]:
                    return True
            if abs(new_position[1] - self.position[1]) == 1:
                return True
        return False
    
class queen(HybridPiece):
    def __init__(self, color):
        super().__init__(color, "Queen", rook(color), bishop(color))

class checkers(ChessPiece):
    def __init__(self,color):
        super().__init__(color, "Checkers")
    
    def is_valid_move_inner(self, board, new_position):
        target1 = (self.position[0] + 2, self.position[1] + 2) 
        target2 = (self.position[0] - 2, self.position[1] - 2) 
        target3 = (self.position[0] + 1, self.position[1] + 1) 
        target4 = (self.position[0] - 1, self.position[1] - 1) 
        if (new_position == target1 and Board.has_obstacle(board, target3)) or (new_position == target2 and Board.has_obstacle(board, target4)):
            return True
        if (new_position == target3 and not Board.has_obstacle(board, target3)) or (new_position == target4 and not Board.has_obstacle(board, target4)):
            return True
        return False

class banner(HybridPiece):
    def __init__(self, color):
        self.buff = queen(color).generate_buff()
        super().__init__(color, "banner", king(color))
        
    def sync(self, board):
        for piece in board:
            if Board.are_touching(self, piece):
                piece.movement_buffs.append(self.buff)
            

        return board