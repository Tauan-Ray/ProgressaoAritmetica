from tkinter import *

# Cores
Colorbackground = '#FFFFFF'
ColorFont = '#242424'
ColorFrameCalculate = '#4f4f4f'

# Criando janela
app = Tk()
app.title('Progressão Aritmética')
app.geometry('520x300')
app.config(bg=Colorbackground)
app.resizable(False, False)

# Criando Header
header = Frame(app, width=335, height=50, bg=Colorbackground, relief='raised', borderwidth=1)
header.place(x=0, y=0)

titleHeader = Label(header, text='Progressão Aritmética', width=20, height=1, font=('Sans-Serif 15 bold'), relief='flat', bg=Colorbackground, fg=ColorFont)
titleHeader.place(x=45, y=9)

# Criando frame para colocar informações sobre operação
calculate = Frame(app, width=186, height=300, bg=ColorFrameCalculate, relief='raised', borderwidth=1)
calculate.place(x=334, y=0)

# Criando botões para as operações


app.mainloop()
