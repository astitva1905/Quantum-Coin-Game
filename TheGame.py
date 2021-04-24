from tkinter import * 
from tkinter import messagebox
import random
from qiskit import *
import numpy as np
import qiskit.tools.jupyter
import matplotlib.pyplot as plt
import math
from pylatexenc import *

root = Tk(className = "Coin Game!")
root.geometry("700x500")
coin = 0
k = 7
#set window color
root.configure(bg='#856ff8')

def qb1():
	global coin
	global k
	coin = 0
	k = 7
	f = ""
	qW = Toplevel(root)
	qW.title("Quantum Coin Game")  
	qW.geometry("600x600")
	qW.configure(bg='#856ff8')
	Label(qW,text="Quantum Coin Game!",font=("Arial", 25),bg="#856ff8",fg="white").place(x=20,y=0)
	Label(qW,text="Moves 1,3,5,7 are Computer moves.\nMoves 2,4,6 are your moves.",font=("Arial", 20),bg="#856ff8",fg="white").place(x=20,y = 100)
	l21 = Label(qW, text = "",bg="#856ff8",fg="white",font=("Arial", 12))
	l21.place(x=20,y=300)
	e = Entry(qW,width = 15,borderwidth = 2)
	e.place(x=400,y=300)

	#print(coin)
	arr = []
	qcoin = QuantumCircuit(1,1)

	qcoin.h(0)
	k-=1
	arr.append("mix -> (0+1)")

	l21.configure(text="Move number = "+str(7-k+1)+" i.e. Your move: \n[Enter Y for Flipping the coin, and N for not Flipping it.]\nThen Click Submit")


	def qb11():
		global coin
		global k

		f = e.get()
		if f=="Y":
			qcoin.x(0)
			k-=1
		else:
			k-=1
			pass
		arr.append("mix -> (0+1)")
		
		if k==1:
			qcoin.h(0)
			k-=1
			arr.append("0")
		else:
			k-=1
			pass
			arr.append("mix -> (0+1)")
		l21.configure(text="Move number = "+str(7-k+1)+" i.e. Your move:")


		if k==0:
			#b11.configure(state="disabled")
			qcoin.measure(0,0)
			job = execute(qcoin, Aer.get_backend('qasm_simulator'), shots=1, memory=True)
			coin = int(job.result().get_memory()[0])

			if coin==0:
				l21.configure(text="COMPUTER WINS!\nPLease click X to quit.")
			elif coin==1:
				l21.configure(text="YOU WIN!!!\nPlease click X to quit.")
			def qb12():
				l22 = Label(qW, text = "The coin states in successive moves were\n"+", ".join(arr),bg="#856ff8",fg="white",font=("Arial", 12))
				l22.place(x=300,y=300)
			b22 = Button(qW,text="Analyse game",font=("Arial", 15),padx=20,pady=20,bg="white",command= qb12)
			b22.place(x= 400, y=500)

	b21 = Button(qW,text="Submit",font=("Arial", 15),padx=20,pady=20,bg="white",command= qb11)
	b21.place(x= 100, y=500)


def cb2():
	global coin
	global k
	coin = 0
	k = 7
	f = ""
	cW = Toplevel(root)
	cW.title("Classical Coin Game")  
	cW.geometry("600x600")
	cW.configure(bg='#856ff8')
	Label(cW,text="Classical Coin Game!",font=("Arial", 25),bg="#856ff8",fg="white").place(x=20,y=0)
	Label(cW,text="Moves 1,3,5,7 are Computer moves.\nMoves 2,4,6 are your moves.",font=("Arial", 20),bg="#856ff8",fg="white").place(x=20,y = 100)
	l11 = Label(cW, text = "",bg="#856ff8",fg="white",font=("Arial", 12))
	l11.place(x=20,y=300)
	e = Entry(cW,width = 15,borderwidth = 2)
	e.place(x=400,y=300)
	
	
	#print(coin)
	arr = []

	f = random.randint(0,1)
	if f==0:
		coin= int(not(coin))
		k-=1
	else:
		k-=1
		pass
	arr.append(str(coin))

	l11.configure(text="Move number = "+str(7-k+1)+" i.e. Your move: \n[Enter Y for Flipping the coin, and N for not Flipping it.]\nThen Click Submit")
	def cb11():
		global coin
		global k

		f = e.get()
		if f=="Y":
			coin = int(not(coin))
			k-=1
		else:
			k-=1
			pass
		arr.append(str(coin))
		f = random.randint(0,1)
		if f==0:
			coin= int(not(coin))
			k-=1
		else:
			k-=1
			pass
		arr.append(str(coin))
		l11.configure(text="Move number = "+str(7-k+1)+" i.e. Your move:")


		if k==0:
			#b11.configure(state="disabled")
			if coin==0:
				l11.configure(text="COMPUTER WINS!\nPLease click X to quit.")
			elif coin==1:
				l11.configure(text="YOU WIN!!!\nPlease click X to quit.")
			def cb12():
				l12 = Label(cW, text = "The coin states in successive moves were\n"+", ".join(arr),bg="#856ff8",fg="white",font=("Arial", 12))
				l12.place(x=300,y=300)
			b12 = Button(cW,text="Analyse game",font=("Arial", 15),padx=20,pady=20,bg="white",command= cb12)
			b12.place(x= 400, y=500)

	b11 = Button(cW,text="Submit",font=("Arial", 15),padx=20,pady=20,bg="white",command= cb11)
	b11.place(x= 100, y=500)


	#------------------------------
	
def cb3():
	game = "1.This game has 2 players, the computer and you. \n2.The game consists of 7 moves, the first move by the computer and the next by you, and so on.\n3.The game starts with the coin in the Heads position. \n4.In each move, a player can either choose to flip the coin, or let it stay the same way.\n5.A player cannot see any moves done by the other player.\n6.None of the players can see the state of the coin during the game.\n7.The state of the coin is revealed after all the 7 moves.\n8.If in the end, the coin is Heads, then the computer wins. If it is tails, You win. "
	messagebox.showinfo("How to play?",game)

Label(root, text = "Coin Game!",bg="#856ff8",fg="white",font=("Arial", 25)).place(x= 270, y=0)
intro = "Welcome! \n This is a small educational project that explains a key difference between classical and quantum computers through a small game.\n Please press the Quantum button if you wish to experience the Quantum version of the game , and the Classical button if you wish to play the Classical version of the game."
w = Text(root,width=50,height=8,bg ="#856ff8",fg="white",font=("Arial", 12),wrap=WORD)
w.insert(INSERT,intro)
w.place(x= 50, y=50)

b1 = Button(root,text="Quantum",font=("Arial", 15),padx=20,pady=20,bg="white",command=qb1)
b1.place(x= 100, y=300)
b2= Button(root,text = "Classical",font=("Arial", 15),padx=20,pady = 20,bg="white",command=cb2)
b2.place(x= 400, y=300)
b3 = Button(root,text="How to play",font=("Arial", 15),padx=10,pady=10,bg="white",command=cb3)
b3.place(x=250,y=410)
root.mainloop()
