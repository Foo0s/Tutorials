import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow, QVBoxLayout, QGroupBox, QLineEdit
from PyQt6.QtCore import Qt, QCoreApplication
from PyQt6.QtGui import QFont, QIcon
from options_apps import Options
import styles
from weather import weather


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.options = Options()
        self.setWindowTitle("GUI - Погода")  # Название программы
        self.setFixedSize(self.options.width, self.options.height)  # Установка размера экрана.
        self.move(500, 150)  # Положение окна.
        self.setStyleSheet(styles.QMainWindow)
        self.setWindowIcon(QIcon("image/pngwing.com.png"))

        # Установка текста.
        self.label_apps_name = QLabel(self)
        self.label_apps_name.setText("Прогноз погоды")  # Название текста.
        self.label_apps_name.setStyleSheet(styles.Label_apps_name)

        self.label_apps_name.move(200, 10)  # Его место положение.
        self.label_apps_name.setFixedWidth(230)  # Увеличение ширины объекта.
        self.label_apps_name.setFont(QFont("Arial", 22))  # setFont - задает шрифт метки.

        # Установка ячеек.
        self.label_now_day = QLabel(self)
        self.label_now_day.setText("Сегодня")
        self.label_now_day.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_now_day.setFixedWidth(180)
        self.label_now_day.setStyleSheet(styles.Label_names)
        self.label_now_day.move(40, 70)

        self.label_tomorrow = QLabel(self)
        self.label_tomorrow.setText("Завтра")
        self.label_tomorrow.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_tomorrow.setFixedWidth(180)
        self.label_tomorrow.setStyleSheet(styles.Label_names)
        self.label_tomorrow.move(370, 70)

        # Кнопка запуска.
        self.start_button = QPushButton(self)
        self.start_button.setText("Узнать")
        self.start_button.setStyleSheet(styles.QPush_button)
        self.start_button.setGeometry(210, 400, 180, 80)

        # Подробная информация.
        self.label_now_day_1 = QLabel(self)
        self.label_now_day_1.setGeometry(100, 130, 90, 30)
        self.label_now_day_1.setText("Градусы")
        self.label_now_day_1.setStyleSheet(styles.QLabel)
        self.linedit_1 = QLineEdit(self)
        self.linedit_1.setGeometry(80, 160, 100, 20)
        self.linedit_1.setStyleSheet(styles.QLineEdit)

        self.label_now_day_2 = QLabel(self)
        self.label_now_day_2.setGeometry(100, 190, 90, 30)
        self.label_now_day_2.setText("Тип погоды")
        self.label_now_day_2.setStyleSheet(styles.QLabel)
        self.linedit_2 = QLineEdit(self)
        self.linedit_2.setGeometry(80, 220, 100, 20)
        self.linedit_2.setStyleSheet(styles.QLineEdit)

        self.label_now_day_3 = QLabel(self)
        self.label_now_day_3.setGeometry(100, 250, 100, 30)
        self.label_now_day_3.setText("Время")
        self.label_now_day_3.setStyleSheet(styles.QLabel)
        self.linedit_3 = QLineEdit(self)
        self.linedit_3.setGeometry(80, 280, 100, 20)
        self.linedit_3.setStyleSheet(styles.QLineEdit)

        self.label_now_day_4 = QLabel(self)
        self.label_now_day_4.setGeometry(85, 310, 90, 30)
        self.label_now_day_4.setText("Градусы ночью")
        self.label_now_day_4.setStyleSheet(styles.QLabel)
        self.linedit_4 = QLineEdit(self)
        self.linedit_4.setGeometry(80, 340, 100, 20)
        self.linedit_4.setStyleSheet(styles.QLineEdit)

        self.label_now_day_5 = QLabel(self)
        self.label_now_day_5.setGeometry(425, 130, 170, 30)
        self.label_now_day_5.setText("Градусы")
        self.label_now_day_5.setStyleSheet(styles.QLabel)
        self.linedit_5 = QLineEdit(self)
        self.linedit_5.setGeometry(405, 160, 100, 20)
        self.linedit_5.setStyleSheet(styles.QLineEdit)

        self.label_now_day_6 = QLabel(self)
        self.label_now_day_6.setGeometry(425, 190, 170, 30)
        self.label_now_day_6.setText("Тип погоды")
        self.label_now_day_6.setStyleSheet(styles.QLabel)
        self.linedit_6 = QLineEdit(self)
        self.linedit_6.setGeometry(405, 220, 100, 20)
        self.linedit_6.setStyleSheet(styles.QLineEdit)

        self.label_now_day_7 = QLabel(self)
        self.label_now_day_7.setGeometry(425, 250, 170, 30)
        self.label_now_day_7.setText("Время")
        self.label_now_day_7.setStyleSheet(styles.QLabel)
        self.linedit_7 = QLineEdit(self)
        self.linedit_7.setGeometry(405, 280, 100, 20)
        self.linedit_7.setStyleSheet(styles.QLineEdit)

        self.label_now_day_8 = QLabel(self)
        self.label_now_day_8.setGeometry(410, 310, 170, 30)
        self.label_now_day_8.setText("Градусы ночью")
        self.label_now_day_8.setStyleSheet(styles.QLabel)
        self.linedit_8 = QLineEdit(self)
        self.linedit_8.setGeometry(405, 340, 100, 20)
        self.linedit_8.setStyleSheet(styles.QLineEdit)

        # Реакция на кнопку.
        self.start_button.clicked.connect(lambda: weather(self))


app = QApplication(sys.argv)  # Передача настроек,хар.
window = MainWindow()  # Инициализация класса.
window.show()  # Вывод результата.
app.exec()  # Вых.
