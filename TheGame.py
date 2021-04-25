from tkinter import * 
from tkinter import messagebox
import random
from qiskit import *
import numpy as np
import qiskit.tools.jupyter
import matplotlib.pyplot as plt
import math
from pylatexenc import *


expl = "If you're wondering about what gibberish is written in the Analysis section of Level 2, or why you're always losing in Level 2, don't worry because you're asking the right questions!\n\nWhat is happening can be explained by recognising that a Quantum computer is fundamentally based on a different principle than the classical computers (the devices we call computers today).\nLet's talk about the Classical Coin game first. Not that hard , right?\nIn fact, if you try the game about 10 times, your odds of not winning even once are ASTRONOMICALLYY low. This is because in the Classical Coin game, you have a 50% chance of winning in each match you play. The computer also has a 50% chance only, and not any higher. In fact, given the Rules of the games, the best that the computer can do is just randomly choose whether or not to flip the coin in a given turn. To explain this a little more, a \"Coin\" can be easily represented by a computer as a \"Bit\" - the most fundamental unit of computing in classical computers. A Bit , like a coin, can only be in 2 states, a 0 or a 1 (like heads or tails). This is what the code that I have written does too. But, according to the rules, the Computer player cannot know the value of this bit (that represnets a coin) once you have made even a single move. Because once you make a single move, the computer doesn't know whether you flipped the bit or not, so the best it can do is just take a random guess, which is exactly what you're doing as the other player. In the end, whoever luck favours the most, wins the game.\nBut this is only about a classical computer. \n\nThe Quantum Computer doesn't work on bits. The fundamental unit of a Quantum Computer is a Qubit - (Quantum Bit). This Qubit works a lot differently than a bit, so stay with me here. A Qubit can be in a state of 0 or 1 (like a bit), but it can also be in a Superposition of both of these states. In a very informal language, this \"Superposition\" means that a Qubit can also be in a 'mixture' of 0 and 1. This is never possible in a bit. So when we are playing a Quantum Coin game, this \"Quantum Coin\" that we're playing with, is actually a Qubit in a Quantum computer. So not only can our Quantum Coin be in Heads or Tails, it can also be in a Superposition of heads & tails. And the quantum computer is capable of putting this qubit in a superposition. This allows the Quantum Computer to come up with a way that always makes him win the game. But how? \nSo basically what happens is, in the very first move itself the Quantum Computer puts the Quantum Coin (that was heads) into a superposition of Heads and tails. Now the User i.e. You, can do anything with any of your chances and it wouldn't even matter a bit. Because all you can do is flip the coin, in essence this would have an effect of shaking/stirring this \"mixture\" of Heads and tails that the Coin is in. But the coin will still remain in that same mixture. Thus your \"flipping the coin\" has no effect at all on the state of the coin. It was a Superposition of Heads & tails before, and it still will be a superposition of Heads and Tails, whether you flip it or not. Finally, in the 7th move, the Quantum Computer reverses the Superposition to get the Quantum coin back into a state of Heads. Thus the Quantum Computer wins every single time, no matter what you, as the other player, choose to do with your moves. This is why you weren't winning even once against the Quantum Computer, because the truth is that you just can't. \n\nThis coin game shows us how different a Quantum Computer is than a Classical computer, and how the game in which you won 50 % of the times against a Classical Computer, you just can't win against a Quantum Computer. This game only highlights 1 of the key powers of Quantum Computers, namely Superposition. The Quantum Computer has other weird and strong powers too, like Interference and Entanglement.  I hope you had fun and learnt something!\n\nThis is the end of the game. If you wish to play it again, please Click on X of this window, and start again from Level 1. If you wish to quit the game, Please press Exit Button."



root = Tk(className = "Coin Game!")
root.geometry("400x500")
#set window color
root.configure(bg='#856ff8')
qplay = 0

coin = 0
k = 7
#----------------------
def info():
	h1 = Toplevel(root)
	h1.title("Learn about the game!")  
	h1.geometry("700x600")
	h1.configure(bg='#856ff8')
	Label(h1,text="WHat is going on?",font=("Arial", 20),bg="#856ff8",fg="white").pack(side=TOP)
	frame = LabelFrame(h1,padx=5,pady=5,bg = "#856ff8",width=600,height=500)

	frame.pack()
	frame.pack_propagate(0)
	v = Scrollbar(frame)
	v.pack(side=RIGHT,fill=Y)
	t = Text(frame,width = 70 , height = 30,wrap = WORD,yscrollcommand=v.set,font=("Arial", 13),bg="#856ff8",fg="white")
	t.insert(INSERT,expl)
	t.configure(state="disabled")
	t.pack(side=TOP, anchor=NW)
	v.config(command=t.yview)
	b = Button(h1,text="Exit",font=("Arial", 15),padx=12,pady=5,bg="white",command= root.destroy)
	b.pack(side=BOTTOM)
#---------------------------
def qb1():
	global coin
	global k
	global qplay
	qplay+=1
	coin = 0
	k = 7
	f = ""
	qW = Toplevel(root)
	qW.title("Level 2")  
	qW.geometry("730x600")
	qW.configure(bg='#856ff8')
	Label(qW,text="Level 2: Quantum Coin Game!",font=("Arial", 25),bg="#856ff8",fg="white").place(x=20,y=0)
	Label(qW,text="Moves 1,3,5,7 are Computer moves.\nMoves 2,4,6 are your moves.",font=("Arial", 20),bg="#856ff8",fg="white",justify="left").place(x=20,y = 60)
	l21 = Label(qW, text = "",bg="#856ff8",fg="white",font=("Arial", 14),wraplength=370 ,justify="left" )
	l21.place(x=20,y=280)
	e = Entry(qW,width = 15,borderwidth = 2)
	e.place(x=400,y=300)

	#print(coin)
	arr = []
	turn = []
	qcoin = QuantumCircuit(1,1)
	arr.append("The coin is Heads")

	qcoin.h(0)
	turn.append("Move "+str(7-k+1)+": Quantum Computer puts the coin into a Superposition!!")
	arr.append("The coin is in a Equal Superposition (\"Mix\") of heads & tails!")
	k-=1


	l21.configure(text="Computer Played Move number " + str(7-k+1-1)+".\nMove number = "+str(7-k+1)+". Your move: \n[Enter Y for Flipping the coin, and N for not Flipping it.Then Click Submit]")

	def qb11():
		global coin
		global k
		global qplay

		f = e.get()
		if f=="Y":
			qcoin.x(0)
			turn.append("Move "+str(7-k+1)+": You flip the coin.")
			k-=1
		else:
			turn.append("Move "+str(7-k+1)+": You don't flip the coin.")
			k-=1
			pass
		arr.append("The coin's still an Equal Superposition (\"Mix\") of heads & tails!")
		
		if k==1:
			qcoin.h(0)
			turn.append("Move "+str(7-k+1)+": Quantum Computer reverses Superposition !!")
			k-=1
			arr.append("The coin is heads!")
		else:
			turn.append("Move "+str(7-k+1)+": Computer doesn't flip the coin.")
			k-=1
			pass
			arr.append("The coin's still an Equal Superposition (\"Mix\") of heads & tails!")
		l21.configure(text="Computer Played Move number " + str(7-k+1-1)+".\nMove number = "+str(7-k+1)+". Your move:")
		
		if k==0:
			#b11.configure(state="disabled")
			qcoin.measure(0,0)

			job = execute(qcoin, Aer.get_backend('qasm_simulator'), shots=1, memory=True)
			coin = int(job.result().get_memory()[0])

			if coin==0:
				l21.configure(text="COMPUTER WINS!\nPLease click X to quit. or Try Again!")
			elif coin==1:
				l21.configure(text="YOU WIN!!!\nPlease click X to quit. or Play Again!")
			
			def qpa():
				qW.destroy()
				qb1()

			def qb13():
				qW.destroy()
				info()

			def qb12():
				results = ""
				results+=arr[0]+"\n"
				for i in range(7):
					results+=turn[i]+"\n"
					results+=arr[i+1]+"\n"
				l22 = Label(qW, text = results,bg="#856ff8",fg="white",font=("Arial", 12),justify="left",wraplength="450")
				l22.place(x=240,y=140)
				l21.configure(text="Computer Wins!!")
				if qplay>=3:
					b22.configure(text="WhaT?!")
					b22.configure(command=qb13)

			b22 = Button(qW,text="Analyse game",font=("Arial", 15),padx=20,pady=20,bg="white",command= qb12)
			b22.place(x= 400, y=500)
			b21.configure(text="Try Again!")
			b21.configure(command=qpa)

	b21 = Button(qW,text="Submit",font=("Arial", 15),padx=20,pady=20,bg="white",command= qb11)
	b21.place(x= 100, y=500)


def cb2():
	global coin
	global k
	coin = 0
	k = 7
	f = ""


	cW = Toplevel(root)
	cW.title("Level 1")  
	cW.geometry("600x600")
	cW.configure(bg='#856ff8')
	Label(cW,text="Level 1: Classical Coin Game!",font=("Arial", 25),bg="#856ff8",fg="white").place(x=20,y=0)
	Label(cW,text="Moves 1,3,5,7 are Computer moves.\nMoves 2,4,6 are your moves.",font=("Arial", 20),bg="#856ff8",fg="white",justify="left").place(x=20,y = 100)
	l11 = Label(cW, text = "",bg="#856ff8",fg="white",font=("Arial", 15),justify="left",wraplength = 380)
	l11.place(x=20,y=280)
	e = Entry(cW,width = 15,borderwidth = 2)
	e.place(x=400,y=300)
	
	
	#print(coin)
	arr = []
	turn = []

	arr.append("The coin is " + str("Heads" if coin==0 else "Tails"))

	f = random.randint(0,1)
	if f==0:
		coin= int(not(coin))
		turn.append("Move "+str(7-k+1)+": Computer flips the coin.")
		k-=1
	else:
		turn.append("Move "+str(7-k+1)+": Computer doesn't flip the coin.")
		k-=1
		pass
	arr.append("The coin is " + str("Heads" if coin==0 else "Tails"))

	l11.configure(text="Computer Played Move number " + str(7-k+1-1)+".\nMove number = "+str(7-k+1)+". Your move: \n[Enter Y for Flipping the coin, and N for not Flipping it.Then Click Submit]")
	def cb11():
		global coin
		global k

		f = e.get()
		if f=="Y":
			turn.append("Move "+str(7-k+1)+": You flip the coin.")
			coin = int(not(coin))
			k-=1
		else:
			turn.append("Move "+str(7-k+1)+": You don't flip the coin.")
			k-=1
			pass
		arr.append("The coin is " + str("Heads" if coin==0 else "Tails"))
		f = random.randint(0,1)
		if f==0:
			turn.append("Move "+str(7-k+1)+": Computer flips the coin.")
			coin= int(not(coin))
			k-=1
		else:
			turn.append("Move "+str(7-k+1)+": Computer doesn't flip the coin.")
			k-=1
			pass
		arr.append("The coin is " + str("Heads" if coin==0 else "Tails"))
		l11.configure(text="Computer Played Move number " + str(7-k+1-1)+".\nMove number = "+str(7-k+1)+" i.e. Your move:")


		if k==0:
			#b11.configure(state="disabled")
			if coin==0:
				l11.configure(text="Computer Played Move number " + str(7-k+1-1)+".\nCOMPUTER WINS!\nPlease click X to quit, or Play Again!")
			elif coin==1:
				l11.configure(text="Computer Played Move number " + str(7-k+1-1)+".\nYOU WIN!!!\nPlease click X to quit, or Play Again!")
			def cb12():
				results = ""
				results+=arr[0]+"\n"
				for i in range(7):
					results+=turn[i]+"\n"
					results+=arr[i+1]+"\n"
				l12 = Label(cW, text = results ,bg="#856ff8",fg="white",font=("Arial", 12),justify="left")
				l12.place(x=300,y=180)
				l11.configure(text="Computer Wins!!" if coin==0 else "You Win!!")
			def cp():
				cW.destroy()
				cb2()
			b12 = Button(cW,text="Analyse game",font=("Arial", 15),padx=20,pady=20,bg="white",command= cb12)
			b12.place(x=400, y=500)

			def q1():
				cW.destroy()
				qb1()

			b11.configure(text='Play again',command=cp)
			b11.place(x=20,y=500)
			if coin ==1 :
				b1 = Button(cW,text="Go to Level 2:\nQuantum",font=("Arial", 15),padx=20,pady=10,bg="white",command=q1)
				
				b12.place(x=200,y=500)
				b1.place(x= 400, y=500)

	

	b11 = Button(cW,text="Submit",font=("Arial", 15),padx=20,pady=20,bg="white",command= cb11)
	b11.place(x= 100, y=500)






#-----------------------------------------------------------
def cb3():
	htp = Toplevel(root)
	htp.title("RUlebook")  
	htp.geometry("400x600")
	htp.configure(bg='#856ff8')
	Label(htp,text="Rulebook",font=("Arial", 25),bg="#856ff8",fg="white",justify="center").place(x=20,y=0)
	Label(htp,text="Players",font=("Arial", 17),bg="#856ff8",fg="white").place(x=0,y=50)
	Label(htp,text="1.This game has 2 players, the computer and you.",font=("Arial", 12),bg="#856ff8",fg="white").place(x=0,y=80)
	Label(htp,text="The Game",font=("Arial", 17),bg="#856ff8",fg="white").place(x=0,y=110)
	Label(htp,text="1.The game starts with the coin in the Heads position. \n\n2.The game consists of 7 moves, the first move by the computer and the next by you, and so on.\n\n3.In each move, a player can either choose to change the state of the coin (for eg. for a classical coin, from heads to tails or vice-a-versa), or let it stay in the same state.\n\n4.The state of the coin is revealed after all 7 moves.\n\n5.If in the end, the coin is Heads, then the computer wins. If it is tails, You win. ",font=("Arial", 12),bg="#856ff8",fg="white",wraplength ="380",justify="left").place(x=0,y=140)
	Label(htp,text="The Rules",font=("Arial", 17),bg="#856ff8",fg="white").place(x=0,y=410)
	Label(htp,text="1.No player can see any moves done by the other player.\n\n2.None of the players can see the state of the coin during the game.\n(Trust me , not even the computer player knows the moves you play.)",font=("Arial", 12),bg="#856ff8",fg="white",wraplength ="380",justify="left").place(x=0,y=440)
	
	#Label(htp, text = "Coin Game!",bg="#856ff8",fg="white",font=("Arial", 25)).place(x= 120, y=0)
#-------------------------
Label(root, text = "Coin Game!",bg="#856ff8",fg="white",font=("Arial", 25)).place(x= 120, y=0)

#intro = "Welcome! \n This is a small educational project that explains a key difference between classical and quantum computers through a small game.\n Please press the Quantum button if you wish to experience the Quantum version of the game , and the Classical button if you wish to play the Classical version of the game."
intro="Welcome! This game has to levels:\nLevel 1: Classical Coin Game \nLevel 2: Quantum Coin Game\n\nLearn how to play, and then start off with level 1!"
w = Label(root,text=intro,bg ="#856ff8",fg="white",font=("Arial", 17),wraplength=380,justify="left")

w.place(x= 0, y=80)

def cg2():

	#root.withdraw()
	cb2()

b2= Button(root,text = "Start Level 1: Classical",font=("Arial", 15),padx=20,pady = 10,bg="white",command=cg2)
b2.place(x= 100, y=400)
b3 = Button(root,text="How to play",font=("Arial", 15),padx=20,pady=10,bg="white",command=cb3)
b3.place(x=100,y=300)
root.mainloop()