import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cursed Chess")
        self.setGeometry(100, 100, 800, 800)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.create_board()

    def create_board(self):
        layout = QGridLayout()
        self.central_widget.setLayout(layout)

        piece_labels = ["R", "N", "B", "Q", "K", "B", "N", "R"]

        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                square = QLabel(self)
                square.setAlignment(Qt.AlignCenter)
                square.setFixedSize(80, 80)
                square.setStyleSheet(f"background-color: {color};")
                layout.addWidget(square, row, col)

                if row == 0 or row == 7:
                    label = QLabel(piece_labels[col], self)
                    label.setAlignment(Qt.AlignCenter)
                    label.setFont(QFont("Arial", 20, QFont.Bold))
                    if color == "black":
                        label.setStyleSheet("color: white;")
                    layout.addWidget(label, row, col)

                if row == 1 or row == 6:
                    pawn_label = QLabel("P", self)
                    pawn_label.setAlignment(Qt.AlignCenter)
                    pawn_label.setFont(QFont("Arial", 20, QFont.Bold))
                    if color == "black":
                        pawn_label.setStyleSheet("color: white;")
                    layout.addWidget(pawn_label, row, col)

    def run(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chess_app = ChessGUI()
    chess_app.run()
    sys.exit(app.exec())
