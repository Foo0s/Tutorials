import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import stylecss

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calture")
        self.setFixedSize(400, 500)
        self.setStyleSheet(stylecss.QMainWindow)

        # Добавление кнопок.
        self.button_0 = QPushButton(self)
        self.button_0.setText("0")
        self.button_0.setGeometry(0, 430, 100, 70)
        self.button_0.setStyleSheet(stylecss.QPushButton)
        self.button_0.setFont(QFont("Comic Sans MS", 18))


        self.button_1 = QPushButton(self)
        self.button_1.setText("1")
        self.button_1.setGeometry(100, 430, 100, 70)
        self.button_1.setStyleSheet(stylecss.QPushButton)
        self.button_1.setFont(QFont("Comic Sans MS", 18))


        self.button_2 = QPushButton(self)
        self.button_2.setText("3")
        self.button_2.setGeometry(200, 430, 100, 70)
        self.button_2.setStyleSheet(stylecss.QPushButton)
        self.button_2.setFont(QFont("Comic Sans MS", 18))


        self.button_3 = QPushButton(self)
        self.button_3.setText("4")
        self.button_3.setGeometry(300, 430, 100, 70)
        self.button_3.setStyleSheet(stylecss.QPushButton)
        self.button_3.setFont(QFont("Comic Sans MS", 18))


        self.button_4 = QPushButton(self)
        self.button_4.setText("5")
        self.button_4.setGeometry(0, 360, 100, 70)
        self.button_4.setStyleSheet(stylecss.QPushButton)
        self.button_4.setFont(QFont("Comic Sans MS", 18))


        self.button_5 = QPushButton(self)
        self.button_5.setText("6")
        self.button_5.setGeometry(100, 360, 100, 70)
        self.button_5.setStyleSheet(stylecss.QPushButton)
        self.button_5.setFont(QFont("Comic Sans MS", 18))


        self.button_6 = QPushButton(self)
        self.button_6.setText("7")
        self.button_6.setGeometry(200, 360, 100, 70)
        self.button_6.setStyleSheet(stylecss.QPushButton)
        self.button_6.setFont(QFont("Comic Sans MS", 18))


        self.button_7 = QPushButton(self)
        self.button_7.setText("8")
        self.button_7.setGeometry(300, 360, 100, 70)
        self.button_7.setStyleSheet(stylecss.QPushButton)
        self.button_7.setFont(QFont("Comic Sans MS", 18))


        self.button_8 = QPushButton(self)
        self.button_8.setText("9")
        self.button_8.setGeometry(0, 290, 200, 70)
        self.button_8.setStyleSheet(stylecss.QPushButton)
        self.button_8.setFont(QFont("Comic Sans MS", 18))


        self.button_ans = QPushButton(self)
        self.button_ans.setText("=")
        self.button_ans.setGeometry(200, 290, 200, 70)
        self.button_ans.setStyleSheet(stylecss.QPushButton)
        self.button_ans.setFont(QFont("Comic Sans MS", 18))


        # Текст.
        self.label_text = QLabel(self)
        self.label_text.setText("Python Calture")
        self.label_text.setGeometry(140, 0, 100, 30)
        self.label_text.setFixedWidth(200)
        self.label_text.setStyleSheet(stylecss.QLabelText)
        self.label_text.setFont(QFont("Comic Sans MS", 17))

        # Кнопки действий.
        self.button_plus = QPushButton(self)
        self.button_plus.setText("+")
        self.button_plus.setGeometry(0, 220, 200, 70)
        self.button_plus.setStyleSheet(stylecss.QPushButton)
        self.button_plus.setFont(QFont("Comic Sans MS", 18))


        self.button_otr = QPushButton(self)
        self.button_otr.setText("-")
        self.button_otr.setGeometry(200, 220, 200, 70)
        self.button_otr.setStyleSheet(stylecss.QPushButton)
        self.button_otr.setFont(QFont("Comic Sans MS", 18))

        self.button_ym = QPushButton(self)
        self.button_ym.setText("*")
        self.button_ym.setGeometry(0, 150, 200, 70)
        self.button_ym.setStyleSheet(stylecss.QPushButton)
        self.button_ym.setFont(QFont("Comic Sans MS", 18))


        self.button_del = QPushButton(self)
        self.button_del.setText("/")
        self.button_del.setGeometry(200, 150, 200, 70)
        self.button_del.setStyleSheet(stylecss.QPushButton)
        self.button_del.setFont(QFont("Comic Sans MS", 18))


        # Установление LineEdit,
        self.line_edit = QLineEdit(self)
        self.line_edit.setText("0")
        self.line_edit.setGeometry(0, 30, 400, 120)
        self.line_edit.setStyleSheet(stylecss.QLineEdit)
        self.line_edit.setFont(QFont("Comic Sans MS", 24))

        # Клик кнопки.
        self.button_ans.clicked.connect(self.click_answer)

        # Операции.
        self.button_0.clicked.connect(lambda x: self.click_operations("0"))
        self.button_1.clicked.connect(lambda x: self.click_operations("1"))
        self.button_2.clicked.connect(lambda x: self.click_operations("3"))
        self.button_3.clicked.connect(lambda x: self.click_operations("4"))
        self.button_4.clicked.connect(lambda x: self.click_operations("5"))
        self.button_5.clicked.connect(lambda x: self.click_operations("6"))
        self.button_6.clicked.connect(lambda x: self.click_operations("7"))
        self.button_7.clicked.connect(lambda x: self.click_operations("8"))
        self.button_8.clicked.connect(lambda x: self.click_operations("9"))
        self.button_ym.clicked.connect(lambda x: self.click_operations("*"))
        self.button_plus.clicked.connect(lambda x: self.click_operations("+"))
        self.button_del.clicked.connect(lambda x: self.click_operations("/"))
        self.button_otr.clicked.connect(lambda x: self.click_operations("-"))

    def click_answer(self):
        result = eval(self.line_edit.text())
        self.line_edit.setText(str(result))

    def click_operations(self, text):
        if self.line_edit.text() != "0":
            self.line_edit.setText(self.line_edit.text() + text)
        else:
            self.line_edit.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
