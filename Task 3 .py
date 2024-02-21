import tkinter as tk
from tkinter import ttk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("GAME")
root.configure(bg='#616A6B')
import random
m=None
case=None

#game logic
def game():
  global m,case
  computer_choice=(random.choice(["Rock","Paper","Scissors"]))
  your_choice=choice.get()
  
  if your_choice==computer_choice:
     m=tk.Label(root,text=f"""\n Your choice : {your_choice}
      \n Computer choice : {computer_choice} 
    """,fg='#17202A',bg='#E5E8E8',font=("Arial",16))
     case=tk.Label(root,text="IT'S A TIE !",bg='#FDFEFE',fg='#229954',font=("Arial",18))
     m.pack(pady=5)
     case.pack(pady=10,padx=10)
    
  elif (your_choice=="Rock" and computer_choice=="Scissors")or(your_choice=="Paper" and computer_choice=="Rock") or(your_choice=="Scissors" and computer_choice=="Paper") :
    m=tk.Label(root,text=f"""\n Your choice : {your_choice}
     \n Computer choice : {computer_choice} 
    """,fg='#17202A',bg='#E5E8E8',font=("Arial",16))
    case=tk.Label(root,text="YOU WIN !",bg='#FDFEFE',fg='#0B4EDF',font=("Arial",18))
    m.pack(pady=5)
    case.pack(pady=10,padx=10)
    

  elif (computer_choice=="Rock" and your_choice=="Scissors")or(computer_choice=="Paper" and your_choice=="Rock") or(computer_choice=="Scissors" and your_choice=="Paper") :
   m=tk.Label(root,text=f"""\n Your choice : {your_choice}
   \n Computer choice : {computer_choice} 
""",fg='#17202A',bg='#E5E8E8',font=("Arial",16))
   case=tk.Label(root,text="YOU LOSE..",bg='#FDFEFE',fg='#EF1313',font=("Arial",18))
   m.pack(pady=5)
   case.pack(pady=10,padx=10)
    
  else:
    case=tk.Label(root,text="INVALID CHOICE",bg='#FDFEFE',fg='#616A6B',font=("Arial",15))
    case.pack(pady=10)

  play_button.pack_forget()
  reset_button.pack(pady=15)

# Reset the game
def reset_game():
  global m, case  
  m.pack_forget()
  case.pack_forget()
  reset_button.pack_forget()
  play_button.pack(pady=10)
  
# Create a widget
frame=tk.LabelFrame(root,bg='#616A6B',padx=5)
frame.pack(pady=5,padx=10)
intro=tk.Label(frame,text="Rock Paper Scissors Game",bg='#616A6B',fg='#FDFEFE',font=font.Font(family="Helvetica",size=20,weight="bold",slant="italic"))
intro.pack(pady=10)
choice=ttk.Combobox(root, values=["Rock","Paper","Scissors"],font=("Arial",12))
choice.pack(pady=10)
play_button=tk.Button(root,text="PLAY",font=("Arial",13),command=game)
play_button.pack(pady=7)
reset_button = tk.Button(root, text="Play Again",font=("Arial",13), command=reset_game)


root.mainloop()
