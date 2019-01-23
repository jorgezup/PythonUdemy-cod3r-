import tkinter as tk

class Application:
    def __init__(self, master=None):
        self.widget1 = tk.Frame(master)
        self.widget1.pack(side=tk.RIGHT)
        self.msg = tk.Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "12")
        self.msg.pack()
        self.sair = tk.Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack(side=tk.RIGHT)

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro wirdget"

root = tk.Tk()
Application(root)
root.mainloop()