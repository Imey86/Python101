import sys
from datetime import datetime

import tkinter.messagebox as box
from tkinter.filedialog import asksaveasfile
if sys.version_info[0] >= 3:
    import tkinter as tk
    import tkinter.ttk as ttk
    # from tkinter import *
else:
    import Tkinter as tk

datadict = {'วันจันทร์': {'money': 'สีส้มอิฐ' ,'work': 'สีเขียวใบเตย' ,'love': 'สีเทาดำ'}
            ,'วันอังคาร': {'money': 'สีโลหะ' ,'work':'สีเทาดำ' ,'love': 'สีเหลืองสว่าง'}
            ,'วันพุธ': {'money': 'สีฟ้าอ่อน' ,'work':'สีส้มอิฐ' ,'love': 'สีเงิน'}
            ,'วันพฤหัส': {'money': 'สีขาวมุก' ,'work':'สีน้ำเงินยีนส์' ,'love': 'สีเหลืองสว่าง'}
            ,'วันศุกร์': {'money': 'สีเขียวใบเตย' ,'work':'สีขาวมุก' ,'love': 'สีเหลืองนวล'}
            ,'วันเสาร์': {'money': 'สีแดงเลือดหมู' ,'work':'สีทอง' ,'love': 'สีส้มแดง'}
            , 'วันอาทิตย์': {'money': 'สีเทาดำ' ,'work': 'สีแดงเลือดหมู', 'love': 'สีเขียวใบเตย'}
            }
print(datadict.keys())
GUI = tk.Tk()  # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบอกสีเสื้อประจำวัน')  # นี่คือชื่อโปรแกรม
GUI.geometry('400x300')  # นี่คือขนาดโปรแกรม

GUI.L1 = tk.Label(GUI, text='เลือกวัน เพื่อบอกสีเสื้อของแต่ละวัน',font=('Angsana New', 20), fg='black')
GUI.L1.grid() # L1.place(x=10, y=10)

#################################Drop Down List#####################################

def fun(GUI):
    GUI.color = GUI.combobox.get()
    GUI.life = datadict[GUI.color]['money']
    GUI.work = datadict[GUI.color]['work']
    GUI.love = datadict[GUI.color]['love']
    print(GUI.color,GUI.life ,GUI.work ,GUI.love )
    GUI.L2.config(text=f'คุณเลือก {GUI.color}')
    GUI.L3.config(text=f'-ด้านชีวิต ควรใส่เสื้อ {GUI.money}') 
    GUI.L4.config(text=f'-ด้านการงาน ควรใส่เสื้อ {GUI.work}') 
    GUI.L5.config(text=f'-ด้านความรัก ควรใส่เสื้อ {GUI.love}') 

GUI.combobox = ttk.Combobox(GUI, values=list(datadict.keys()), state='readonly')    
GUI.combobox.grid(column=0, row=1)
GUI.combobox.set("--- Select ---")  # default value
GUI.combobox.grid(column=0, row=1)
GUI.combobox.bind("<<ComboboxSelected>>", lambda f1: fun(GUI))
GUI.color = GUI.combobox.get()
GUI.money = ''
GUI.work = ''
GUI.love =''

#################################แสดงข้อมูล############################################
GUI.L2 = tk.Label(GUI, text=f'คุณเลือก {GUI.color}', font=('Angsana New', 20), fg='black')
GUI.L2.grid(column=0, row=2)  # L1.place(x=10, y=10)

GUI.L3 = tk.Label(GUI, text=f'ด้านชีวิต ควรใส่เสื้อ {GUI.money}', font=('Angsana New', 20), fg='black')
GUI.L3.grid(column=0, row=3)  # L1.place(x=10, y=10)

GUI.L4 = tk.Label(GUI, text=f'ด้านการงาน ควรใส่เสื้อ {GUI.work}', font=('Angsana New', 20), fg='black')
GUI.L4.grid(column=0, row=4)  # L1.place(x=10, y=10)

GUI.L5 = tk.Label(GUI, text=f'ด้านความรัก ควรใส่เสื้อ {GUI.love}', font=('Angsana New', 20), fg='black')
GUI.L5.grid(column=0, row=5)  # L1.place(x=10, y=10)


# ####################################################################################
GUI.mainloop()
