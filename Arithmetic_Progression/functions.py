from tkinter import *

def an(frameinfo, frameresult, buttons, function):
    
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

        result = a1Value + (nValue - 1) * rValue

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
            function()
        
        restart_button = Button(frameresult, command=restart ,text='Restart', width=32, height=1, padx=4 ,anchor='center', font=('Arial 12 bold'), relief='raised', overrelief='sunken', bg='#969696', fg='#242424')
        restart_button.place(x=0, y=270)
        
    
    calculate_button = Button(frameinfo, command=calculeAn ,text='Calcular', width=22, height=1 ,anchor='center', compound='center', font=('Arial 10 bold'), relief='raised', overrelief='sunken', bg='#4f4f4f', fg='#242424')
    calculate_button.place(x=0, y=270)


def a1(frameinfo, frameresult, buttons, function):
    
    for b in buttons:
        b.destroy()

    anLabel = Label(frameinfo, text='Diga o valor de AN', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    anLabel.place(x=30, y=50)

    anEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    anEntry.place(x=56, y=75)

    nLabel = Label(frameinfo, text='Diga o valor de N', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    nLabel.place(x=30, y=110)

    nEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    nEntry.place(x=56, y=135)

    rLabel = Label(frameinfo, text='Diga o valor de R', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    rLabel.place(x=30, y=170)

    rEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    rEntry.place(x=56, y=195)

    def calculeA1():
        anValue = float(anEntry.get())
        nValue = float(nEntry.get())
        rValue = float(rEntry.get())
        p = (nValue - 1) * rValue
        result = anValue - p

        resultShow = Label(frameresult, text=f'O valor de A1 é {result:.2f}', width=25, height=1, anchor='w' ,font=('Arial 14 bold'), relief='flat', bg='#63749c', fg='#242424')
        resultShow.place(x=10, y=120)

        def restart():
            anLabel.destroy()
            anEntry.destroy()
            nLabel.destroy()
            nEntry.destroy()
            rLabel.destroy()
            rEntry.destroy()
            calculate_button.destroy()
            resultShow.destroy()
            restart_button.destroy()
            function()
        
        restart_button = Button(frameresult, command=restart ,text='Restart', width=32, height=1, padx=4 ,anchor='center', font=('Arial 12 bold'), relief='raised', overrelief='sunken', bg='#969696', fg='#242424')
        restart_button.place(x=0, y=270)
        
    
    calculate_button = Button(frameinfo, command=calculeA1 ,text='Calcular', width=22, height=1 ,anchor='center', compound='center', font=('Arial 10 bold'), relief='raised', overrelief='sunken', bg='#4f4f4f', fg='#242424')
    calculate_button.place(x=0, y=270)


def n(frameinfo, frameresult, buttons, function):
    
    for b in buttons:
        b.destroy()

    a1Label = Label(frameinfo, text='Diga o valor de A1', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    a1Label.place(x=30, y=50)

    a1Entry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    a1Entry.place(x=56, y=75)

    anLabel = Label(frameinfo, text='Diga o valor de AN', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    anLabel.place(x=30, y=110)

    anEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    anEntry.place(x=56, y=135)

    rLabel = Label(frameinfo, text='Diga o valor de R', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    rLabel.place(x=30, y=170)

    rEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    rEntry.place(x=56, y=195)

    def calculeN():
        a1Value = float(a1Entry.get())
        anValue = float(anEntry.get())
        rValue = float(rEntry.get())
        p = -1 * rValue
        p1 = p
        p2 = a1Value + p1
        p3 = anValue - p2
        result = p3 / rValue

        resultShow = Label(frameresult, text=f'O valor de A1 é {result:.2f}', width=25, height=1, anchor='w' ,font=('Arial 14 bold'), relief='flat', bg='#63749c', fg='#242424')
        resultShow.place(x=10, y=120)

        def restart():
            anLabel.destroy()
            anEntry.destroy()
            anLabel.destroy()
            anEntry.destroy()
            rLabel.destroy()
            rEntry.destroy()
            calculate_button.destroy()
            resultShow.destroy()
            restart_button.destroy()
            function()
        
        restart_button = Button(frameresult, command=restart ,text='Restart', width=32, height=1, padx=4 ,anchor='center', font=('Arial 12 bold'), relief='raised', overrelief='sunken', bg='#969696', fg='#242424')
        restart_button.place(x=0, y=270)
        
    
    calculate_button = Button(frameinfo, command=calculeN ,text='Calcular', width=22, height=1 ,anchor='center', compound='center', font=('Arial 10 bold'), relief='raised', overrelief='sunken', bg='#4f4f4f', fg='#242424')
    calculate_button.place(x=0, y=270)

def r(frameinfo, frameresult, buttons, function):
    
    for b in buttons:
        b.destroy()

    anLabel = Label(frameinfo, text='Diga o valor de AN', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    anLabel.place(x=30, y=50)

    anEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    anEntry.place(x=56, y=75)

    nLabel = Label(frameinfo, text='Diga o valor de N', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    nLabel.place(x=30, y=110)

    nEntry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    nEntry.place(x=56, y=135)

    a1Label = Label(frameinfo, text='Diga o valor de A1', width=15, height=1, font=('Ivy 10 bold'), relief='flat', bg='#4f4f4f', fg='#242424')
    a1Label.place(x=30, y=170)

    a1Entry = Entry(frameinfo, width=10, justify='center', relief='solid', borderwidth=1, bg='#4f4f4f', fg='white')
    a1Entry.place(x=56, y=195)

    def calculeR():
        anValue = float(anEntry.get())
        nValue = float(nEntry.get())
        a1Value = float(a1Entry.get())
        p = nValue - 1
        p1 = anValue - a1Value
        result = p1 / p

        resultShow = Label(frameresult, text=f'O valor de A1 é {result:.2f}', width=25, height=1, anchor='w' ,font=('Arial 14 bold'), relief='flat', bg='#63749c', fg='#242424')
        resultShow.place(x=10, y=120)

        def restart():
            anLabel.destroy()
            anEntry.destroy()
            anLabel.destroy()
            anEntry.destroy()
            a1Label.destroy()
            a1Entry.destroy()
            calculate_button.destroy()
            resultShow.destroy()
            restart_button.destroy()
            function()
        
        restart_button = Button(frameresult, command=restart ,text='Restart', width=32, height=1, padx=4 ,anchor='center', font=('Arial 12 bold'), relief='raised', overrelief='sunken', bg='#969696', fg='#242424')
        restart_button.place(x=0, y=270)
        
    
    calculate_button = Button(frameinfo, command=calculeR ,text='Calcular', width=22, height=1 ,anchor='center', compound='center', font=('Arial 10 bold'), relief='raised', overrelief='sunken', bg='#4f4f4f', fg='#242424')
    calculate_button.place(x=0, y=270)