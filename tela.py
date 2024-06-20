from tkinter import *
from sorteador import *
import os

class Tela:

    def __init__(self):
        self.tela = Tk()
        
        self.config()
        
        self.carregar_fundo()
        self.tela_sorteador()
        
        self.tela.mainloop()
        
    def config(self):
        
        self.tela.geometry('630x630')
    
    def carregar_fundo(self):
        
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, 'junina.png')
        self.img = PhotoImage(file=image_path)
    
    
    def tela_sorteador(self):
        self.sorteador = Frame(self.tela, bg='red')
        self.sorteador.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        
        img_fundo = Label(self.sorteador, image=self.img)
        img_fundo.place(relx=0, rely=0)
        
        
        self.num_sorteado = Label(self.sorteador, text=sortear_numero(), font=('Arial', 100))
        self.num_sorteado.place(relx=0.3, rely=0.38)
        
        botao_sortear = Button(self.sorteador, text='Sortear', font=('Arial', 24), command=self.atualizar_num)
        botao_sortear.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.1)
    
    def atualizar_num(self):
        self.num_sorteado.config(text=sortear_numero())
        