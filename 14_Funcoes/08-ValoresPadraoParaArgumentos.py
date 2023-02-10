from tkinter import *

def padronizar_cod(lista_cod, padrao='a'):
    for i, codigo in enumerate(lista_cod):
        codigo = codigo.strip()
        if padrao == 'a':
            codigo = codigo.casefold()
        elif padrao == 'A':
            codigo = codigo.upper()
        lista_cod[i] = codigo
    return lista_cod


produtos = ['ABC123', 'abc909', 'AbG9204', 'asjdaj898']
print(padronizar_cod(produtos, 'A'))


# Tk inter interface
class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()


root = Tk()
Application(root)
root.mainloop()
