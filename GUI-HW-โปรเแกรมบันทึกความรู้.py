from tkinter import *
from tkinter import ttk #theme of tk from tkinter
from tkinter import messagebox

GUI = Tk() #หน้าจอหลัก
GUI.title('โปรแกรมบอกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดหน้าจอหลัก

L1 = Label(GUI,text='โปรแกรมบอกข้อมูล เลือกกดปุ่มที่ต้องการรู้ข้อมูล')
L1.place(x=10,y=20)

def Button1():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 3,000,000 บาท'
    messagebox.showinfo('เงินในบัญชี',text) #.showwarning/showerror

B1 = ttk.Button(GUI,text='มีเงินอยู่กี่บาท',command = Button1) #ปุ่ม
B1.place(x=10,y=50) #ตำแหน่ง


def Button2():
    text = 'ตอนนี้มีเรียน Python 101 กับลุงวิศวกร'
    messagebox.showinfo('วิชาเรียน',text) #.showwarning/showerror

B2 = ttk.Button(GUI,text='เรียนวิชาอะไรอยู่',command = Button2) #ปุ่ม
B2.place(x=10,y=100) #ตำแหน่ง


def Button3():
    text = 'อยากทบทวน แล้วก็ลองสอนไม่แพง'
    messagebox.showinfo('Why',text) #.showwarning/showerror

B3 = ttk.Button(GUI,text='ทำไมลงเรียน Python',command = Button3) #ปุ่ม
B3.place(x=10,y=150) #ตำแหน่ง


def Button4():
    text = 'ลุงสอนดี สอนช้า แต่บางครั้งก็ง่วง'
    messagebox.showinfo('Feedback',text) #.showwarning/showerror

B4 = ttk.Button(GUI,text='ลุงสอนดีมั๊ยะ',command = Button4) #ปุ่ม
B4.place(x=10,y=200) #ตำแหน่ง


GUI.mainloop()
