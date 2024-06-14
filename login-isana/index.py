#importar as bibliotecas 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#criar nossa janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False,height=False) 
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/Logoicon.ico")

#=== carregar imagens 
Logo = PhotoImage(file="icons/raposa.png")


#=== Widgets ==========

LeftFrame = Frame(jan,width=200,height=300,bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan,width=395,height=300,bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=Logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50,y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame,width=30)
UserEntry.place(x=150,y=110)

PassLabel = Label(RightFrame, text="Passworld:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5,y=150)

PassEntry = ttk.Entry(RightFrame,width=30,show="•")
PassEntry.place(x=150,y=160)

#botões 

LoginButton = ttk.Button (RightFrame, text= "Login", width=30)
LoginButton.place(x=100, y=225)

def Register():
    #Removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5,y=5)

    NomeEntry = Entry(RightFrame,width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5,y=55)

    EmailEntry = Entry(RightFrame,width=39)
    EmailEntry.place(x=100, y=66)

    Register = ttk.Button (RightFrame, text= "Register", width=30)
    Register.place(x=100, y=225)

    def BackToLogin():
        #Removend widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo de volta os widgets de login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button (RightFrame, text= "Back", width=20, command=BackToLogin)
    Back.place(x=125,y=260)







RegisterButton = ttk.Button (RightFrame, text= "Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)











jan.mainloop()

