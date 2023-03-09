import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QLineEdit, QDateEdit, QMessageBox
from register_apps import database


class Application_register(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 500) #Расширение.
        self.setWindowTitle("Register_Apps") #Название программы.

        #Создание текста,кнопок.
        self.label_register = QLabel(self)
        self.label_register.setText("Регистрация")
        self.label_register.setGeometry(270, 90, 90, 20)

        self.layout_1 = QLineEdit(self)
        self.layout_1.setPlaceholderText("Эл. почта.") #Теневой текст.
        self.layout_1.setGeometry(230, 160, 190, 30)

        self.layout_2 = QLineEdit(self)
        self.layout_2.setPlaceholderText("Пароль.")
        self.layout_2.setGeometry(230, 200, 190, 30)

        #Кнопка.
        self.push_reg_button = QPushButton(self)
        self.push_reg_button.setText("Вход")
        self.push_reg_button.setGeometry(230, 280, 90, 40)
        self.push_reg_button.clicked.connect(lambda x: self.reg_butt("1"))

        self.push_reg_button_2 = QPushButton(self)
        self.push_reg_button_2.setText("Регистрация")
        self.push_reg_button_2.setGeometry(330, 280, 90, 40)
        self.push_reg_button_2.clicked.connect(lambda x: self.reg_butt("2"))

        #Установка времени.
        self.date = QDateEdit(self)
        self.date.setGeometry(230, 240, 190, 30)


    def reg_butt(self, name):
        if name == "2":
            if self.layout_1.text() != "" and self.layout_2.text() != "":
                database.check_users(self.layout_1.text(), self.layout_2.text(), self.date.text())
            else:
                print("Error")
        else:
            if self.layout_1.text() != "" and self.layout_2.text() != "":
                database.check_users(self.layout_1.text(), self.layout_2.text(), self.date.text())
            else:
                print("Error")

    def answer_user(self):
        #Уведомление - окно сообщения.
        mess_box = QMessageBox()
        mess_box.setIcon(QMessageBox.Icon.Information)
        mess_box.setWindowTitle("Ошибка входа регистрации.")
        mess_box.setText("Ошибка регистрации. Данный пользователь уже зарегестрированн.")
        
        push_button = QPushButton()
        push_button.setText("Ok")
        #Добавление действий.
        mess_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        result = mess_box.exec()
        if result == QMessageBox.StandardButton.Ok:
            print("Замечательно")
        else:
            print("01101")
        



if __name__ == "__main__":
    apps = QApplication(sys.argv)
    window = Application_register()
    window.show()
    apps.exec()