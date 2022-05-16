import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pyautogui as pag


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AirDrop")
        self.root.attributes("-topmost", 1)
        self.root.geometry("200x30+0+0")
        self.labeltest = StringVar()
        self.w = tk.Label(self.root, textvariable = self.labeltest)
        self.w.pack()
        self.run()
        self.refresh_data()
        self.root.mainloop()

    def interface(self):
        """界面编写位置"""
        x, y = pag.position()
        Label(self.root, text='{}, {}'.format(x,y), font='华文新魏').pack()
        pass
    def refresh_data(self):
        x, y = pag.position()
        self.labeltest.set('{}, {}'.format(x, y))
        #Label(self.root, text='{}, {}'.format(x, y), font='华文新魏').pack()
        print('{}, {}'.format(x, y))
        self.root.after(100, self.refresh_data)

    def run(self):
        pass


if __name__ == '__main__':
    mygui = GUI()