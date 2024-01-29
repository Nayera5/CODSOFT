import tkinter
from tkinter import messagebox
window=tkinter.Tk()
window.title("Login")
window.geometry('350x320')
window.configure(bg='#273746')

def generate():
  import random
  import string
  l=int(length_e.get())
  #join the characters into one string with '' _no space_
  password =''.join(random.choices(string.ascii_letters + string.digits + string.punctuation ,k=l))
  messagebox.showinfo("P.W","your strong password is  "+str(password))


#creat widget
tobic=tkinter.Label(window,text="Password Generator",bg='#D0D3D4',fg="black",font=("Arial",15))

length=tkinter.Label(window,text="Write the desired length",bg='#273746',fg="white",font=("Arial",15))
length_e=l=tkinter.Entry(window,font=("Arial",15))

press=tkinter.Button(window,text="show password",bg='#D0D3D4',fg="black",font=("Arial",12),command=generate)

tobic.grid(row=0,column=4,pady=20)
length.grid(row=1,column=1,pady=20)
length_e.grid(row=1,column=3,pady=20)
press.grid(row=3,column=4,pady=20)
