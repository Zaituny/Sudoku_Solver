from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('Sudoku_GUI.ui', self)
        self.my_board = [[0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0]]
        self.Solve_Button.clicked.connect(self.Solved_Board)

    def inRow(self, dummy_board, token, row):
        for i in range(0, 9):
            if dummy_board[row][i] == token:
                return True
        return False

    def inCol(self, dummy_board, token, col):
        for i in range(0, 9):
            if dummy_board[i][col] == token:
                return True
        return False

    def inBox(self, dummy_board, token, row, col):
        local_row = row  - row %3
        local_col = col  - col %3
        for i in range(local_row, local_row + 3):
            for j in range(local_col, local_col + 3):
                if dummy_board[i][j] == token:
                    return True
        return False

    def isValid(self, dummy_board, token, row, col):
        return not self.inRow(dummy_board, token, row) and not self.inCol(dummy_board, token, col) and not self.inBox(dummy_board, token, row, col)

    def SolveBoard(self):                
        for i in range(0, 9):
            for j in range(0, 9):
                if self.my_board[i][j] == 0:
                    for k in range(1, 10):
                        if self.isValid(self.my_board, k, i, j):
                            self.my_board[i][j] = k
                            if self.SolveBoard():
                                return True
                            else:
                                self.my_board[i][j] = 0
                    return False
        return True

    def set_values(self):
        counter = 1
        for i in range(0,9):
            for j in range(0,9):
                self.my_board[i][j] = eval("self.spinBox_" + str(counter) + ".value()")
                counter += 1
    
    def Solved_Board(self):
        counter = 1
        self.set_values()
        if self.SolveBoard():
            for i in range(0, 9):
                for j in range(0, 9):
                    eval("self.spinBox_" + str(counter) + ".setValue(" + str(self.my_board[i][j]) + ")")
                    counter += 1

        
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
sys.exit(app.exec_())
