#Класс с параметрами для приложения.
class Params:
    def __init__(self):
        #Размер экрана.
        self.screen = "350x400"

        #Цвета.
        self.color_fon = "yellow"
        self.color_text = "orange"

    #Функция хранящая в себе название программы
    def text(self):
        self.name_program = "Calculator"
        return self.name_program

    #Иконки
    def logo(self):
        self.icon = "C:/Users/USER/Desktop/Calture/images/icon.ico"
        return self.icon