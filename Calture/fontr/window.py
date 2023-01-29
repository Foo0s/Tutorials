from parameters.params import Params
import tkinter as tk
import sys

class Mane_Window:
    def __init__(self):
        self.screen = Params


    def main(self):
        while True:
            root = tk.Tk()
            greet = tk.Label(text="Hello world!")
            greet.pack()
            root.mainloop()
            if sys.exit():
                pass


if __name__ == "__main__":
    start = Mane_Window()
    start.main()

