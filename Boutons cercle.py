from tkinter import *
from random import *
from math import *

def drawcircle1():
    global x1,x2,y1,y2
    coul='white'
    x1=0
    y1=60
    x2=60
    y2=0
    "Tracé du cercle"
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
def drawcircle2():
    global x1,x2,y1,y2
    coul='white'
    x1=60
    y1=125
    x2=125
    y2=60
    "Tracé du cercle"
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
def drawcircle3():
    global x1,x2,y1,y2
    coul='white'
    x1=120
    y1=185
    x2=185
    y2=120
    "Tracé du cercle"
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
def drawcircle4():
    global x1,x2,y1,y2
    coul='white'
    x1=180
    y1=245
    x2=245
    y2=180
    "Tracé du cercle"
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)
def drawcircle5():
    global x1,x2,y1,y2
    coul='white'
    x1=230
    y1=280
    x2=280
    y2=230
    "Tracé du cercle"
    can1.create_oval(x1,x2,y1,y2,width=2,fill=coul)





    
#Programme principal
#creation du widget principal
fen1=Tk()
#Creation des widgets esclaves
can1=Canvas(fen1,bg='dark grey',height=300,width=300)
can1.pack(side=RIGHT)
bou1=Button(fen1,text='QUITTER', command=fen1.destroy)
bou1.pack(side=BOTTOM)
bou2=Button(fen1,text='Tracer un cercle 1',command=drawcircle1)
bou2.pack()
bou3=Button(fen1,text='Tracer un cercle 2',command=drawcircle2)
bou3.pack()
bou4=Button(fen1,text='Tracer un cercle 3',command=drawcircle3)
bou4.pack()
bou5=Button(fen1,text='Tracer un cercle 4',command=drawcircle4)
bou5.pack()
bou6=Button(fen1,text='Tracer un cercle 5',command=drawcircle5)
bou6.pack()
fen1.mainloop()  #demarrage du receptionnaire d'evenements
  #destruction/fermeture de la fenetre

