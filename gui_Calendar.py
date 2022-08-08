#!/usr/bin/python

# TODO: pip install tk

from tkinter import *
import calendar


def displayCalender():
    calGui = Tk()
    calGui.config(background='black')
    inputYear = int(textYear.get())
    calGui.title("Calender " + str(inputYear))
    calGui.geometry("600x600")
    gui_content= calendar.calendar(inputYear)
    displayingYear = Label(calGui, text= gui_content, font= "Consolas 10 bold")
    displayingYear.grid(row=5, column=1,padx=20)
    calGui.mainloop()


if __name__=='__main__':
    mainThread = Tk()
    mainThread.config(background='black')
    mainThread.title("Calender")
    mainThread.geometry("300x250")

    labelCalendar = Label(mainThread, text="Calender",bg='black', fg="white",font=("times", 28, "bold"))
    labelYear = Label(mainThread, text="Enter year", bg='black', fg="white")
    textYear=Entry(mainThread)
    
    buttonShowCalander = Button(mainThread, text='Show Calender',fg='Black',bg='grey',command=displayCalender)
    buttonExit = Button(mainThread, text='Exit',fg='Black',bg='grey',command=mainThread.destroy)


    #adjusting widgets in position
    labelCalendar.grid(row = 1, column = 1)
    labelYear.grid(row = 2, column = 1)
    textYear.grid(row = 3, column = 1)
    buttonShowCalander.grid(row = 4, column = 1)
    buttonExit.grid(row = 5, column = 1)
    mainThread.mainloop()
    
