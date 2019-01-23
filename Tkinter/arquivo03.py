import tkinter as tk

class Application:
    def __init__(self, master=None):
        self.widget1 = tk.Frame(master)
        self.widget1.pack()
        self.msg = tk.Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "12")
        self.msg.pack()
        self.sair = tk.Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["command"] = self.widget1.quit
        self.sair.pack()

root = tk.Tk()
Application(root)
root.mainloop()