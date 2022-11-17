from tkinter import *
import random

class Main_Window:
    def __init__(self,tk):

        self.cor = ['red','green','blue','yellow','pink','black','white']
        self.pontos = 0
        self.txtPontos = f'   Pontos:    {self.pontos:}'

        self.fr1 = Frame(tk)
        self.fr1.pack()
        self.fr2 = Frame(tk)
        self.fr2.pack(pady=20)
        self.fr3 = Frame(tk).pack(padx=5)

        self.btnStart = Button(self.fr1, text='Clique para iniciar', width=15, command=self.start)
        self.btnStart.pack(pady=10,padx=10)

        self.btn1Red = Button(self.fr2,padx=6, bg='red', command=self.pontuacao('red'))
        self.btn1Red.pack(side=LEFT,padx=5)
        
        self.btn2Green = Button(self.fr2,padx=6,bg = 'green', command=self.pontuacao('green'))
        self.btn2Green.pack(side=LEFT,padx=5)
        
        self.btn3Blue = Button(self.fr2,padx=6, bg = 'blue', command=self.pontuacao('blue'))
        self.btn3Blue.pack(side=LEFT,padx=5)
        
        self.btn4Yellow = Button(self.fr2,padx=6,bg = 'yellow', command=self.pontuacao('yellow'))
        self.btn4Yellow.pack(side=LEFT,padx=5)
        
        self.btn5Pink = Button(self.fr2,padx=6,bg = 'pink', command=self.pontuacao('pink'))
        self.btn5Pink.pack(side=LEFT,padx=5)
        
        self.btn6Black = Button(self.fr2,padx=6,bg = 'black', command=self.pontuacao('black'))
        self.btn6Black.pack(side=LEFT,padx=5)
        
        self.btn7White = Button(self.fr2,padx=6,bg = 'white', command=self.pontuacao('white'))
        self.btn7White.pack(side=LEFT,padx=5)

        self.lbPontos = Label(self.fr3,text=self.txtPontos)
        self.lbPontos.pack(side=LEFT)


    def start(self):
        self.btnStart['bg'] = self.cor[random.randint(0,6)]
        if self.btnStart['bg'] =='black':
            self.btnStart['fg'] = 'white'
            self.btnStart['text'] = self.cor[random.randint(0,6)]
        else: 
            self.btnStart['fg'] = 'black'
            self.btnStart['text'] = self.cor[random.randint(0,6)]
    def pontuacao(self, cor):
        if self.btnStart['text'] == cor:
            self.pontos += 1
            self.lbPontos['text'] = self.txtPontos

root = Tk()
root.geometry('250x150')
Main_Window(root)
root.title('Colors')
root.mainloop()
