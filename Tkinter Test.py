import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import font as tkfont


def selectCSV():
    global file_path
    file_path = filedialog.askopenfilename()
    filename = file_path.split("/")
    print(filename[len(filename) - 1])
    return filename[len(filename) - 1]

class BaseWindow(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PlotPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome!")
        label.pack(side="top",fill="x",pady=10)
        selectFile = tk.Button(self, text="Select CSV File", command=selectCSV)
        selectFile.pack()

        nextPage = tk.Button(self,text="Next Scene", command=lambda: controller.show_frame("PlotPage"))
        nextPage.pack()

class PlotPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="Plot Page!")
        label.pack(side="top",fill="x", pady=10)

        backButton = tk.Button(self,text="Home", command=lambda: controller.show_frame("StartPage"))
        backButton.pack()

if __name__ == "__main__":
    app = BaseWindow()
    app.mainloop()

'''
class BaseWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Upload CSV")
        self.pack(fill=BOTH, expand = 1)

        selectFile = Button(self, text="Select File", command=self.selectCSV)
        selectFile.place(x=88,y=110)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=100,y=150)

    def client_exit(self):
        exit()

    def selectCSV(self):
        global file_path
        file_path = filedialog.askopenfilename()
        filename = file_path.split("/")
        print(filename[len(filename) - 1])


class plotPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Inside Plot Page").pack(side="top", fill="x", pady=10)
'''