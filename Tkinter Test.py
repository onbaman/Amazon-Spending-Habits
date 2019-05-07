from tkinter import *
from tkinter import filedialog

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Upload CSV File")
        self.pack(fill=BOTH, expand = 1)

        selectFile = Button(self, text="Select File", command=self.selectCSV)
        selectFile.place(x=68,y=110)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=80,y=150)

    def client_exit(self):
        exit()

    def selectCSV(self):
        global folder_path
        filename = filedialog.askopenfile()
        folder_path.set(filename)
        print(filename)

root = Tk()
root.geometry("200x200")
folder_path = StringVar()
app = Window(root)
root.mainloop()