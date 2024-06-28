from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry('1050x1200')
root.resizable(10, 100)
root.configure(background='#e0dede', borderwidth=3,)

def msg(a):
    final_message['text'] = a

def Computer_sco():
    final = int(computer_score['text'])
    final +=1
    computer_score["text"] = str(final)

def Player_sco():
    final = int(player_score['text'])

    final +=1
    player_score["text"] = str(final)

def reset():
    computer_score['text'] = "0"
    player_score['text'] = "0"
    computer_choice['text'] = ""
    player_choice['text'] = ""
    final_message['text'] = ""
    print("Thanks for playing")

def winner(p,c):
    if p == c:
        msg("The game is draw")
    elif p == "rock":
        if c == "paper":
            msg("Computer win")
            Computer_sco()
        else:
            msg("Player win")
            Player_sco()
    elif p == "paper":
        if c == "scissor":
            msg("Computer win")
            Computer_sco()
        else:
            msg("Player win")
            Player_sco()
    elif p == "scissor":
        if c == "rock":
            msg("Computer win")
            Computer_sco()
        else:
            msg("Player win")
            Player_sco()
    else:
        pass

def play(p):
    choices = ["rock", "paper", "scissor"]
    c = random.choice(choices)
    winner(p,c)
    computer_choice['text'] = "Computer choice: " + c
    player_choice['text'] = "player choice: " + p

computer_score = Label(root, text=0,bg="#8f8b8b",font=("Courier New",25))
player_score = Label(root,text=0,bg="#8f8b8b",font=("Courier New",25))
computer_score.place(x=800,y=570)
player_score.place(x=200,y=570)

player_choice = Label(root, text="",bg="#abd2d4", font=("Courier New",20))
player_choice.place(x=400,y=300)
computer_choice = Label(root, text="",bg="#abd2d4", font=("Courier New",20))
computer_choice.place(x=400,y=350)
final_message = Label(root, text="",bg="#abd2d4", font=("Courier New",20))
final_message.place(x=400,y=400)

Label(root, text='ROCK , PAPER AND SCISSOR GAME', font=('Cambria', 32,"bold"),bg='#e6c8e8', fg='#535798',borderwidth=3,relief=RIDGE ).place(x=180, y=17)
rock   = Button(root,width=10,height=3,text="ROCK",font=("arial",20,"bold"),bg="black",fg="white", command=lambda: play("rock")).place(x=130,y=100)
paper  = Button(root,width=10,height=3,text="Paper",font=("arial",20,"bold"),bg="black",fg="white", command=lambda: play("paper")).place(x=430,y=100)
scissor= Button(root,width=10,height=3,text="Scissor",font=("arial",20,"bold"),bg="black",fg="white", command=lambda: play("scissor")).place(x=730,y=100)
Label(root, text="Player's score", font=('Brush Script', 23),bg='#5c5c5b', fg='white',borderwidth=3,relief=RIDGE ).place(x=110, y=500)
Label(root, text="Computer's score", font=('Brush Script', 23),bg='#5c5c5b', fg='white',borderwidth=3,relief=RIDGE ).place(x=700, y=500)
ok_btn = Button(root, height=2, width=7, text='Ok', font=10, bg='#205b7a',command=lambda: root.destroy())
ok_btn.place(x=400, y=630)
reset_btn = Button(root, height=2, width=7, text='Reset', font=10, bg='#205b7a', command= reset)
reset_btn.place(x=520, y=630)

root.mainloop()