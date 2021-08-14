from tkinter import *

def sayHelloWorld():
    print("Hello world")
def sayNo():
    print("Bye Bye")

mainWindow = Tk()
button = Button(mainWindow,text = "Click me",command = sayHelloWorld).grid(row=0,column=1)
button2 = Button(mainWindow,text = "Click me2",command = sayNo).grid(row=1,column=1)
button3 = Button(mainWindow,text = "Click me3",command = sayNo).grid(row=1,column=2)
mainWindow.mainloop()