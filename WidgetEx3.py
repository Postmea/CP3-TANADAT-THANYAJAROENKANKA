from tkinter import *

def sayHelloWorld():
    print("Hello world")
def sayNo():
    print("Bye Bye")

mainWindow = Tk()
button = Button(mainWindow,text = "Click me",command = sayHelloWorld,activebackground = "blue").grid(row = 1,column = 1)
button2 = Button(mainWindow,text = "Click me2",command = sayNo).grid(row = 2,column = 1)
button3 = Button(mainWindow,text = "Click me3",command = sayNo).grid(row = 2,column = 2)
label = Label(mainWindow,text = "Hello world",width = 20,fg = "red",bg = "pink",font = ("Helvetica", "16","bold"),anchor="center").grid(row = 0,column = 1)
mainWindow.mainloop()