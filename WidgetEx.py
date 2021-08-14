from tkinter import *

def sayHelloWorld():
    print("Hello world")
def sayNo():
    print("Bye Bye")

mainWindow = Tk()
button = Button(mainWindow,text = "Click me",command = sayHelloWorld)
button.place(x = 20, y = 10)
button2 = Button(mainWindow,text = "Click me2",command = sayNo)
button2.place(x = 120, y = 10)
mainWindow.mainloop()