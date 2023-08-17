from Board import *

class ChessPiece:
    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.position = (0, 0)

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def is_valid_move(self, board, new_position):
        return (0 <= new_position[0] < 8 and 0 <= new_position[1] < 8) and not (new_position == self.position)

    def move(self, board, new_position):
        self.position = new_position

class rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "rook")

    def is_valid_move(self, board, new_position):

        if not super().is_valid_move(board, new_position):
            return False

        if new_position[0] == self.position[0] or new_position[1] == self.position[1] and not board.is_blocked(new_position, self.position):
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
        if steps != abs(delta_y):
            return False
        
        if (0 <= new_position[0] > 8 and 0 <= new_position[1] > 8):
            return False

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
            if new_position[0] == self.position[0] + 1 and new_position[1] == self.position[1] ==self.position[1]:
                return True
            if self.position[0] == 1 and new_position[0] == self.position[0]+2 and new_position[1] == self.position[1]:
                return True
            if abs(new_position[1] - self.position[1]) == 1:
                return True
        return False
    
class queen(ChessPiece):
    def __init__(self,color):
        super().__init__(color,"queen")
            
    def is_valid_move(self, board, new_position):
        if not super().is_valid_move(board,new_position):
            return False
        return queen.is_valid_move(self,board,new_position) or bishop.is_valid_move(self,board,new_position)