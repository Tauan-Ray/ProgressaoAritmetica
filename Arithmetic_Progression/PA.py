from functions import * 
from tkinter import *

# Cores
Colorbackground = '#63749c'
Colorfont = '#242424'
ColorFrameCalculate = '#4f4f4f'
Colorbutton = '#969696'


# Criando janela
app = Tk()
app.title('Progressão Aritmética')
app.geometry('520x300')
app.config(bg=Colorbackground)
app.resizable(False, False)


# Criando Header 
header = Frame(app, width=335, height=50, bg=Colorbackground, relief='raised', borderwidth=1)
header.place(x=0, y=0)

titleHeader = Label(header, text='Progressão Aritmética', width=20, height=1, font=('Sans-Serif 15 bold'), relief='flat', bg=Colorbackground, fg=Colorfont)
titleHeader.place(x=45, y=9)


# Criando frame para colocar informações sobre operação e header
calculate = Frame(app, width=186, height=300, bg=ColorFrameCalculate, relief='raised', borderwidth=1)
calculate.place(x=334, y=0)

titleCalculate = Label(calculate, text='Informações', width=15, height=2, font=('Sans-Serif 14 bold'), relief='solid', bg=ColorFrameCalculate, fg=Colorfont, borderwidth=1)
titleCalculate.place(x=0, y=0)

# Criando função que irá iniciar o programa
def start():
    start_button.destroy()

    # Criando botões para as operações
    an_button = Button(app, command= lambda:an(calculate, app, (an_button, a1_button, n_button, r_button)) ,text='AN', width=10, height=3, anchor='center', font=('Arial 9 bold') ,relief='raised', overrelief='sunken', bg=Colorbutton, fg=Colorfont)
    an_button.place(x=30, y=80)

    a1_button = Button(app, text='A1', width=10, height=3, anchor='center', font=('Arial 9 bold') ,relief='raised', overrelief='sunken', bg=Colorbutton, fg=Colorfont)
    a1_button.place(x=190, y=80)

    n_button = Button(app, text='N', width=10, height=3, anchor='center', font=('Arial 9 bold') ,relief='raised', overrelief='sunken', bg=Colorbutton, fg=Colorfont)
    n_button.place(x=30, y=170)

    r_button = Button(app, text='R', width=10, height=3, anchor='center', font=('Arial 9 bold') ,relief='raised', overrelief='sunken', bg=Colorbutton, fg=Colorfont)
    r_button.place(x=190, y=170)


# Criando botão para iniciar
start_button = Button(app, command=start ,text='Clique aqui para começar', width=20, height=1, anchor='center', font=('Arial 12 bold'), relief='raised', overrelief='sunken', bg=Colorbutton, fg=Colorfont)
start_button.place(x=55, y=130)


app.mainloop()
