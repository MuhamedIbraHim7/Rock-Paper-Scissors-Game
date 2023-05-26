import random 
from tkinter import *

#dictionary and variables
outcomes = {
    "rock":{"rock":1,"paper":0,"scissors":2},
    "paper":{"rock":2,"paper":1,"scissors":0},
    "scissors":{"rock":0,"paper":2,"scissors":1}
    }
player1_score = 0
player2_score = 0
current_player = 1
player1_choice = None
player2_choice = None

#create functon for button's action
def button_click_handler(choice):
    global player1_choice
    global player2_choice
    global current_player

    if current_player == 1:
        player1_choice = choice
        instruction_label.config(text="Player 2's turn")
        current_player = 2
    else:
        player2_choice = choice
        result_handler(player1_choice, player2_choice)
        current_player = 1
        instruction_label.config(text="Player 1's turn")    
            
            
def result_handler(player1_choice,player2_choice):
    global player1_score
    global player2_score
    
    player1_choice_label.config(fg="blue",text="Player1 : " + str(player1_choice))
    player2_choice_label.config(fg="green",text="Player2 : " + str(player2_choice))
    result = outcomes[player1_choice][player2_choice]
    
    if result == 2 :
        player1_score = player1_score + 2 
        outcome_label.config(fg="red",text="Outcome : Player1 won")
        
    elif result == 1 :
        player1_score = player1_score + 1
        player2_score = player2_score + 1   
        outcome_label.config(fg="red",text="Outcome : Draw")
    
    elif result == 0:
        player2_score = player2_score + 2 
        outcome_label.config(fg="red",text="Outcome : Player2 won")
        
    player1_score_label.config(text="Player1 : " + str(player1_score))
    player2_score_label.config(text="Player2 : " + str(player2_score))

def reset_game():
    global player1_score
    global player2_score
    global current_player
    global player1_choice
    global player2_choice
    
    player1_score = 0
    player2_score = 0
    current_player = 1
    player1_choice = None
    player2_choice = None
    
    player1_score_label.config(text="Player1 : 0")
    player2_score_label.config(text="Player2 : 0")
    player1_choice_label.config(text="Player1 : ")
    player2_choice_label.config(text="Player2 : ")
    outcome_label.config(text="Outcome : ")
    instruction_label.config(text="Player 1's turn")
    
# the main screan
master = Tk()
master.title("RPS Game")
master.geometry("400x300")

#create labels 
Label(master,text="Rock, Paper, Scissors",font=("Calibre",18)).grid(row=0,sticky=N,padx=200,pady=10)
Label(master,text="Please every player should select one option",font=("Calibre",16)).grid(row=1,sticky=N)
instruction_label = Label(master, font=("Calibre", 16),text="Player 1's turn")
instruction_label.grid(row=2, columnspan=2)

player1_score_label = Label(master,text="Player1 : 0",font=("Calibre",16))
player1_score_label.grid(row=3,sticky=W)
player2_score_label = Label(master,text="Player2 : 0",font=("Calibre",16))
player2_score_label.grid(row=3,sticky=E)

player1_choice_label = Label(master,font=("Calibre",16))
player1_choice_label.grid(row=4,sticky=W)
player2_choice_label = Label(master,font=("Calibre",16))
player2_choice_label.grid(row=4,sticky=E)

outcome_label = Label(master,font=("Calibre",16))
outcome_label.grid(row=4,sticky=N)


#Create Buttons
rock_button = Button(master,text="Rock",width=25,bg="red",fg="white",command= lambda:button_click_handler("rock"))
rock_button.grid(row=5,sticky=W,padx=10,pady=10)
paper_button = Button(master,text="Paper",width=25,command= lambda:button_click_handler("paper"))
paper_button.grid(row=5,sticky=E,padx=10,pady=10,)
scissors_button = Button(master,text="Scissors",width=25,bg="gray",fg="white",command= lambda:button_click_handler("scissors"))
scissors_button.grid(row=5,sticky=N,padx=10,pady=10)
reset_button = Button(master, text="Reset", width=25,bg="black",fg="white" ,command=reset_game)
reset_button.grid(row=6, sticky=N, pady=10)

#Dummy label
Label(master).grid(row=5)

master.mainloop()