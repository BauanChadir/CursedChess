import Board

class ChessPiece:
    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.position = (0, 0)
        self.movement_buff = []

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def is_valid_move(self, board, new_position):
        return (0 <= new_position[0] < Board.board_size_x and 0 <= new_position[1] < Board.board_size_y) and not (new_position == self.position)

    def on_move(board, target_pos):
        return board

    def put(self, new_position):
        self.position = new_position

class HybridPiece(ChessPiece):
    def __init__(self, color, *pieces):
        super().__init__(color, "rook")
        self.pieces = pieces


    def is_valid_move(self, board, new_position):
        for piece in self.pieces:
            if piece.is_valid_move(board, new_position):
                return True
        return False


class rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "rook")

    def is_valid_move(self, board, new_position):

        if not super().is_valid_move(board, new_position):
            return False

        if (new_position[0] == self.position[0] or new_position[1] == self.position[1]) and not Board.is_blocked(board, self.position, new_position):
            return True
        return False

class knight(ChessPiece):
    def __init__(self,color):
        super().__init__(color, "knight")
        
    def is_valid_move(self, board, new_position):
        if not super().is_valid_move(board,new_position):
            return False
        
        if abs(new_position[0] - self.position[0]) == 2 and abs(new_position[1]-self.position[1]) == 1:
            return True
        elif abs(new_position[0]-self.position[0]) == 1 and abs(new_position[1] - self.position[1]) == 2:
            return True
        return False
    
class bishop(ChessPiece):
    def __init__ (self, color):
        super().__init__(color, "bishop")
    
    def is_valid_move(self, board, new_position):
        if not super().is_valid_move(board,new_position):
            return False
        delta_x = new_position[0] - self.position[0]
        delta_y = new_position[1] - self.position[1]
        
        steps = abs(delta_x)
        if steps != abs(delta_y) or Board.is_blocked(board, self.position, new_position):
            return False
        return True

class king(ChessPiece):
    def __init__ (self, color):
        super().__init__(color, "king")

    def is_valid_move(self, board, new_position):
        if not super().is_valid_move(board,new_position):
            return False
        if (self.position[0]-1 <= new_position[0] <= self.position[0]+1) and (self.position[1]-1 <= new_position[1] <= self.position[1]+1):
            return True
        return False

class pawn(ChessPiece):
    def __init__(self,color):
        super().__init__(color, "pawn")
    
    def is_valid_move(self, board, new_position):
        if not super().is_valid_move(board,new_position):
            return False
        
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
        super().__init__(color, rook(color), bishop(color))

class checkers(ChessPiece):
    def __init__(self,color):
        super().__init__(color, "pawn")
    
    def is_valid_move(self, board, new_position):
        if not super().is_valid_move(board,new_position):
            return False

        target1 = (self.position[0] + 2, self.position[1] + 2) 
        target2 = (self.position[0] - 2, self.position[1] - 2) 
        target3 = (self.position[0] + 1, self.position[1] + 1) 
        target4 = (self.position[0] - 1, self.position[1] - 1) 
        if (new_position == target1 and Board.has_obstacle(board, target3)) or (new_position == target2 and Board.has_obstacle(board, target4)):
            return True
        return False

class banner(HybridPiece):
    def __init__(self,color):
        self.buff = queen(color)
        super().__init__(color, "pawn", king(color))
    
    def is_valid_move(self, board, new_position):
        if not super().is_valid_move(board,new_position):
            return False
        
    def on_move(self, board, target_pos):
        for piece in board:
            next_to_start = Board.touches(self, piece)
            

        return board