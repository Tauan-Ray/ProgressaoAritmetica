from tkinter import *

def an(frameinfo, frameresult, buttons):
    
    for b in buttons:
        b.destroy()

    a1Label = Label(frameinfo, text='Diga o valor de A1', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    a1Label.place(x=30, y=50)

    a1Entry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    a1Entry.place(x=56, y=75)

    nLabel = Label(frameinfo, text='Diga o valor de N', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    nLabel.place(x=30, y=110)

    nEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    nEntry.place(x=56, y=135)

    rLabel = Label(frameinfo, text='Diga o valor de R', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    rLabel.place(x=30, y=170)

    rEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    rEntry.place(x=56, y=195)

    def calculeAn():
        a1Value = float(a1Entry.get())
        nValue = float(nEntry.get())
        rValue = float(rEntry.get())

        result = a1Value+(nValue-1)*rValue

        resultShow = Label(frameresult, text=f'O valor de AN é {result:.2f}', width=25, height=1, anchor='w' ,font=('Arial 14 bold'), relief='flat', bg='#63749c', fg='#242424')
        resultShow.place(x=10, y=120)

        def restart():
            a1Label.destroy()
            a1Entry.destroy()
            nLabel.destroy()
            nEntry.destroy()
            rLabel.destroy()
            rEntry.destroy()
            calculate_button.destroy()
            resultShow.destroy()
            restart_button.destroy()
        
        restart_button = Button(frameresult, text='Restart', width=32, height=1, padx=4 ,anchor='center', font=('Arial 12 bold'), relief='raised', overrelief='sunken', bg='#969696', fg='#242424')
        restart_button.place(x=0, y=270)
        
    
    calculate_button = Button(frameinfo, command=calculeAn ,text='Calcular', width=22, height=1 ,anchor='center', compound='center', font=('Arial 10 bold'), relief='raised', overrelief='sunken', bg='#4f4f4f', fg='#242424')
    calculate_button.place(x=0, y=270)

