from Tkinter.Usuarios import Usuarios
import tkinter as tk


class Application:
    def __init__(self, master=None):
        self.fonte = ("Arial", "15")

        self.container1 = tk.Frame(master)
        self.container1["pady"] = 20
        self.container1.pack()
        self.container2 = tk.Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = tk.Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = tk.Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = tk.Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = tk.Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = tk.Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = tk.Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = tk.Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = tk.Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Arial", "13", "bold")
        self.titulo.pack()

        self.lblidusuario = tk.Label(self.container2, text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=tk.LEFT)

        self.txtidusuario = tk.Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=tk.LEFT)

        self.btnBuscar = tk.Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=tk.RIGHT)

        self.lblnome = tk.Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=tk.LEFT)

        self.txtnome = tk.Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=tk.LEFT)

        self.lbltelefone = tk.Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=tk.LEFT)

        self.txttelefone = tk.Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=tk.LEFT)

        self.lblemail = tk.Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=tk.LEFT)

        self.txtemail = tk.Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=tk.LEFT)

        self.lblusuario = tk.Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=tk.LEFT)

        self.txtusuario = tk.Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=tk.LEFT)

        self.lblsenha = tk.Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=tk.LEFT)

        self.txtsenha = tk.Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=tk.LEFT)

        self.buntInsert = tk.Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.buntInsert["command"] = self.inserirUsuario
        self.buntInsert.pack(side=tk.LEFT)

        self.buntAlterar = tk.Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.buntAlterar["command"] = self.alterarUsuario
        self.buntAlterar.pack(side=tk.LEFT)

        self.buntExcluir = tk.Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.buntExcluir["command"] = self.excluirUsuario
        self.buntExcluir.pack(side=tk.LEFT)

        self.lblmsg = tk.Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirUsuario(self):
        user = Usuarios()

        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, tk.END)
        self.txtnome.delete(0, tk.END)
        self.txttelefone.delete(0, tk.END)
        self.txtemail.delete(0, tk.END)
        self.txtusuario.delete(0, tk.END)
        self.txtsenha.delete(0, tk.END)

    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, tk.END)
        self.txtnome.delete(0, tk.END)
        self.txttelefone.delete(0, tk.END)
        self.txtemail.delete(0, tk.END)
        self.txtusuario.delete(0, tk.END)
        self.txtsenha.delete(0, tk.END)

    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, tk.END)
        self.txtnome.delete(0, tk.END)
        self.txttelefone.delete(0, tk.END)
        self.txtemail.delete(0, tk.END)
        self.txtusuario.delete(0, tk.END)
        self.txtsenha.delete(0, tk.END)

    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, tk.END)
        self.txtidusuario.insert(tk.INSERT, user.idusuario)

        self.txtnome.delete(0, tk.END)
        self.txtnome.insert(tk.INSERT, user.nome)

        self.txttelefone.delete(0, tk.END)
        self.txttelefone.insert(tk.INSERT, user.telefone)

        self.txtemail.delete(0, tk.END)
        self.txtemail.insert(tk.INSERT, user.email)

        self.txtusuario.delete(0, tk.END)
        self.txtusuario.insert(tk.INSERT, user.usuario)

        self.txtsenha.delete(0, tk.END)
        self.txtsenha.insert(tk.INSERT, user.senha)


root = tk.Tk()
Application(root)
root.mainloop()