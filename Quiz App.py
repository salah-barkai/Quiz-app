import tkinter 
from tkinter import *
import random

def reponse1():
 reponse_eleve=entré1.get()
 reponse_machine="est un appeille electronique"
 if reponse_eleve==reponse_machine:
     entré1.delete(0,END)
     entré1.insert(str("bien jouer!"))

 else:
         entré1.insert(0,str("wooh mal jouer!"))

def reponse2():
 reponse_eleve=entré2.get()
 reponse_machine="est un appeille electronique"
 if reponse_eleve==reponse_machine:
     entré2.delete(str(END))
     entré2.insert(str("bien jouer!"))

 else:
         entré2.insert(0,str("wooh mal jouer!"))

         





def reponse5():
 reponse_eleve=entré5.get()
 reponse_machine="est un appeille electronique"
 if reponse_eleve==reponse_machine:
     entré5.delete(0,END)
     entré5.insert(str("bien jouer!"))

 else:
         entré5.insert(0,str("wooh mal jouer!"))


def reponse6():
 reponse_eleve=entré6.get()
 reponse_machine="est un appeille electronique"
 if reponse_eleve==reponse_machine:
     entré6.delete(0,END)
     entré6.insert(str("bien jouer!"))

 else:
         entré6.insert(0,str("wooh mal jouer!"))



window= Tk()
window.title("App Quiz")
window.config(bg="black")

label=Label(text="Question pour un Champion",font=30)
label.pack(padx=50,pady=20,)
label.config(bg="purple")


question=Label(text="Que ce qu'un Ordinateur ?", font=20)
question.pack(padx=50,pady=20,)
question.config(bg="orange")



question2=Label(text="Quelle est le language de l'ordinateur?",font=20)
question.pack(padx=50,pady=20,)
question2.config(bg="orange")

entré1=Entry()
entré1.config()
entré1.pack(padx=50,pady=5)

button1=Button(text="ok",font=10,command=reponse1)
button1.pack(padx=5,pady=5)
button1.config(bg="white")





question3=Label(text="Qui a Crée le language python?" ,font=20)
question3.pack(padx=50,pady=20,)
question3.config(bg="orange")

entré2=Entry()
entré2.config()
entré2.pack(padx=50,pady=5)

button2=Button(text="ok",font=10,command=reponse2)
button2.pack(padx=5,pady=5)
button2.config(bg="white")



question6=Label(text="Qui a crée Apple?", font=20)
question6.pack(padx=50,pady=20,)
question6.config(bg="orange")

entré5=Entry()
entré5.config()
entré5.pack(padx=50,pady=5)

button5=Button(text="ok",font=10,command=reponse5)
button5.pack(padx=5,pady=5)
button5.config(bg="white")

question7=Label(text="Qui est Bill Gate?",font=20)
question7.pack(padx=50,pady=20,)
question7.config(bg="orange")

entré6=Entry()
entré6.config()
entré6.pack(padx=50,pady=5)

button6=Button(text="ok",font=10,command=reponse6)
button6.pack(padx=5,pady=5)
button6.config(bg="white")


bonnechance=Label(text="Les questionnaires sont trés simple Bonne Chance",font=20)
bonnechance.pack(padx=50,pady=20,)
bonnechance.config(bg="purple")


window.mainloop()