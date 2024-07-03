import tkinter as tk
from math import *
from random import randint
(Hauteur,Largeur) = (1000,1000)
root = tk.Tk()
root.title("Snake")
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg='white')
Dessin.pack()

largeur_case=50

def mouvement(a,L):
    L.pop(0)
    L.append(a)
    return L

def carre(i,j,c):
    p=(i*largeur_case,j*largeur_case)
    q=(i*largeur_case+largeur_case,j*largeur_case+largeur_case)
    Dessin.create_rectangle(p,q,fill=c)

def suivant(p):
    (i,j)=p
    N=Hauteur//largeur_case
    if etat.direction=='N':
        return (i,(j-1)%N)
    elif etat.direction=='S':
        return (i,(j+1)%N)
    elif etat.direction=='O':
        return ((i-1)%N,j)
    elif etat.direction=='E':
        return((i+1)%N,j)

def position_aleatoire():
    return (randint(0,Largeur//largeur_case-1), randint(0,Hauteur//largeur_case-1))

class Etat:
    
    def __init__(self):
        self.direction='E'
        self.pomme=position_aleatoire()
        (i,j)=(Hauteur//(2*largeur_case), Largeur//(2*largeur_case))
        self.L=[(i-1,j), (i,j), (i+1,j)]
        self.affichage()
    
    def affichage(self):
        Dessin.delete('all')
        carre(self.pomme[0], self.pomme[1], 'red') # Pomme
        # Serpent
        for p in self.L[:-1]:
            (i,j)=p
            carre(i,j,'green')
        (i,j)=self.L[-1]
        carre(i,j,'black')
    
    def avance(self):
        p=suivant(self.L[-1])
        if p in self.L:
            raise ValueError("Perdu")
        if p==self.pomme:
            self.L.append(p)
            self.pomme=position_aleatoire()
        else:
            mouvement(p,self.L)
    
    def mange(self):
        p=suivant(self.L[-1])
        self.L.append(p)

etat=Etat()

def haut(event):
    etat.direction='N'
def bas(event):
    etat.direction='S'
def gauche(event):
    etat.direction='O'
def droite(event):
    etat.direction='E'
    
root.bind('<Up>',haut)
root.bind('<Down>',bas)
root.bind('<Left>',gauche)
root.bind('<Right>',droite)

def temps():
    global etat
    try:
        etat.avance()
    except:
        etat=Etat()
    etat.affichage()
    Dessin.after(100,temps)
    
temps()

root.mainloop()