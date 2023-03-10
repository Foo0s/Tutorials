import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QLineEdit, QDateEdit, QMessageBox
from register_apps import database
from PyQt6.QtGui import QPixmap, QIcon
import styles


class Application_register(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 500) #Расширение.
        self.setWindowTitle("AU_REG") #Название программы.
        self.setStyleSheet("background-image: url(image/1614131065_1-p-zadnii-fon-v-minimalizme-1.jpg)") #Фон.
        #Иконка.
        self.setWindowIcon(QIcon(QPixmap("image/pngwing.com.png")))

        #Создание текста,кнопок.
        self.label_register = QLabel(self)
        self.label_register.setText("Регистрация")
        self.label_register.setGeometry(260, 90, 130, 40)
        self.label_register.setStyleSheet(styles.QLabel)

        self.layout_1 = QLineEdit(self)
        self.layout_1.setPlaceholderText("Эл. почта.") #Теневой текст.
        self.layout_1.setGeometry(230, 160, 190, 30)
        self.layout_1.setStyleSheet(styles.QLineEdit)

        self.layout_2 = QLineEdit(self)
        self.layout_2.setPlaceholderText("Пароль.")
        self.layout_2.setGeometry(230, 200, 190, 30)
        self.layout_2.setStyleSheet(styles.QLineEdit)

        #Кнопка.
        self.push_reg_button = QPushButton(self)
        self.push_reg_button.setText("Вход")
        self.push_reg_button.setGeometry(230, 280, 90, 40)
        self.push_reg_button.clicked.connect(lambda x: self.reg_butt("1"))
        self.push_reg_button.setStyleSheet(styles.QPushButton)

        self.push_reg_button_2 = QPushButton(self)
        self.push_reg_button_2.setText("Регистрация")
        self.push_reg_button_2.setGeometry(330, 280, 90, 40)
        self.push_reg_button_2.clicked.connect(lambda x: self.reg_butt("2"))
        self.push_reg_button_2.setStyleSheet(styles.QPushButton)

        #Установка времени.
        self.date = QDateEdit(self)
        self.date.setGeometry(230, 240, 190, 30)
        self.date.setStyleSheet(styles.QDateTime)


    def reg_butt(self, name):
        if name == "2":
            if self.layout_1.text() != "" and self.layout_2.text() != "":
                database.check_users(self.layout_1.text(), self.layout_2.text(), self.date.text())
            else:
                print("Error")
        elif name == "1":
            if self.layout_1.text() != "" and self.layout_2.text() != "":
                database.reg_users(self.layout_1.text(), self.layout_2.text(), self.date.text())
            else:
                print("Error")

    def answer_user(self):
        while True:
            #Уведомление - окно сообщения.
            mess_box = QMessageBox()
            mess_box.setIcon(QMessageBox.Icon.Information)
            mess_box.setWindowTitle("Ошибка")
            mess_box.setText("Ошибка регистрации. Данный пользователь уже зарегестрированн.")

            #Добавление действий.
            mess_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            result = mess_box.exec()
            if result == QMessageBox.StandardButton.Ok:
                break
            else:
                continue

    def hello_user(self):
        box_mes = QMessageBox()
        box_mes.setIcon(QMessageBox.Icon.Information)
        box_mes.setWindowTitle("Активно")
        box_mes.setText("Добро пожаловать!")
        box_mes.exec()


    def answer_mistake_for_user(self):
        while True:
            message = QMessageBox()
            message.setIcon(QMessageBox.Icon.Warning)
            message.setWindowTitle("Ошибка")
            message.setText("Ошибка Входа. Данного пользователя нет в БД.")
            message.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            result = message.exec()
            if result == QMessageBox.StandardButton.Ok:
                break
            else:
                continue

        



if __name__ == "__main__":
    apps = QApplication(sys.argv)
    window = Application_register()
    window.show()
    apps.exec()