import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cursed Chess")
        self.setGeometry(100,100,800,800)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.create_board()
    
    def create_board(self):
        layout = QGridLayout()
        self.central_widget.setLayout(layout)
        
        for row in range(8):
            for col in range(8):
                color = "white" if (row+col) % 2 == 0 else "black"
                square = QLabel(self)
                square.setAlignment(Qt.AlignCenter)
                square.setFixedSize(80,80)
                square.setStyleSheet(f"background-color: {color};")
                layout.addWidget(square, row, col)
        
        piece_labels = ["R","N","B","Q","K","B","N","R"]
        for col, label_text in enumerate(piece_labels):
            label = QLabel(label_text, self)
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont("Arial", 20, QFont.Bold))
            layout.addWidget(label,7,col)
    
    def run(self):
        self.show()
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    chess_app = ChessGUI()
    chess_app.run()
    sys.exit(app.exec())