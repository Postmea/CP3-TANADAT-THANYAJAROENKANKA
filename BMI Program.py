from tkinter import *
import math

def BMICal(event):
    x = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if x > 30:
        result = "อ้วนมาก"
    elif 25 <= x <= 29.9:
        result = "อ้วน"
    elif 23 <= x <= 24.9:
        result = "น้ำหนักเกิน"
    elif 18.6 <= x <= 22.9:
        result = "น้ำหนักปกติ"
    elif x <= 18.5:
        result = "ผอมเกิน"
    labelResult.configure(text=x)
    labelResult2.configure(text=result)

main = Tk()
labelHeight = Label(main,text='ส่วนสูง (ซม.)')
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(main,text='น้ำหนัก (กิโลกรัม)')
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1,column=1)
calButton = Button(main,text='คำนวน',bg='yellow',fg='red',font='bold')
calButton.bind('<Button-1>',BMICal)
calButton.grid(row=2,column=0)
labelResult = Label(main,text='ผลลัพธ์ BMI')
labelResult.grid(row=2,column=1)
labelResult2 = Label(main,text='')
labelResult2.grid(row=3,column=1)
main.mainloop()