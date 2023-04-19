import tkinter as tk
from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

####################################################################################

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบอกสีเสื้อประจำวัน') #นี่คือชื่อโปรแกรม
GUI.geometry('500x200') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='เลือกวัน เพื่อบอกสีเสื้อของแต่ละวัน',font=('Angsana New',20),fg='black')
L1.place(x=10,y=10)

#################################Drop Down List#####################################

daylist = ['วันจันทร์','วันอังคาร','วันพุธ','วันพฤหัส','วันศุกร์','วันเสาร์','วันอาทิตย์']
day = tk.StringVar(GUI)
dropdown = tk.OptionMenu(GUI,day,*daylist)
dropdown.place(x=10,y=50)

#day.set(daylist[0])
print(day)

#################################แสดงข้อมูล############################################

selectday = day
data={'วันจันทร์':'สีเหลือง','วันอังคาร':'สีชมพู','วันพุธ':'สีเขียว','วันพฤหัส':'สีส้ม','วันศุกร์':'สีฟ้า','วันเสาร์':'สีม่วง','วันอาทิตย์':'สีแดง'}
color = data['วันจันทร์']

L2 = Label(GUI,text='คุณเลือก',selectday,'ควรใส่เสื้อสี',color)
L2.place(x=150,y=20)

print('คุณเลือก',selectday,'ควรใส่เสื้อสี',color)

##################################CSV###############################################

import csv

def writecsv(datalist):
    with open('record.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fw = file reader
        data = list(fr)
    return data

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = selectday.get() #ดึงข้อมูลจากตัวแปร day มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    variable.set(daylist[0]) #เคลียร์ข้อมูลที่อยู่ในช่องที่เลือก

LF1 = ttk.LabelFrame(GUI,text='กดเพื่อบันทึกค่า')
LF1.place(x=100,y=50)

B1 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B1.pack(ipadx=10,ipady=10)

#################################CSV###############################################
GUI.mainloop()


#v_day = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui เก็บวัน
#E1 = ttk.Entry(L1,textvariable=v_day,font=('Angsana New',25))
#E1.pack(pady=100,padx=10)
#E1.place(x=100,y=500)


def Button1():
    day = 'จันทร์'
    #color = 'เหลือง'
    messagebox.showinfo('วันนี้ควรใส่เสื้อสี')

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=200,y=100)
#B1 = ttk.Button(FB1,text='เลือกวัน',command=Button1)
#B1.pack(ipadx=20,ipady=20)
