#Импортирование библиотек и файлов.

from parameters.params import Params
import tkinter as tk
import sys

class Mane_Window:
    #Установка значений из другого класса.
    def __init__(self):
        self.settings = Params()

    #Основное окно GUI-приложения.
    def dop_main(self):
        self.root = tk.Tk()
        self.root.title(self.settings.text())
        self.root.geometry(self.settings.screen)
        self.root.resizable(width=False, height=False)
        self.root.iconbitmap(self.settings.logo())
        self.root.config(bg=self.settings.color_fon)
        text = tk.Label(text="123")
        text.pack()
        self.root.mainloop()

    #Задаёт цвет.
    def color_main(self):
        pass

    #Реакция на выход из приложения.
    def exit(self):
        if sys.exit():
            sys.exit()

    #Запуск программы. Основная функция.
    def main(self):
        while True:
            self.dop_main()
            self.root.mainloop()
            self.exit()



#Вызов класса.
if __name__ == "__main__":
    start = Mane_Window()
    start.main()

