from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkcalendar import DateEntry
from datetime import datetime
from tabulate import tabulate
import random
window=Tk()

photo=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\BED.png"))
photo1=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\room.jpg"))
photo2=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\child.jpg"))
photo31=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\adult.png"))
photo4=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\cal.png"))
photo7=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\bill.png"))
photo8=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\kit.png"))
photo9=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\game.jpg"))
photo10=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\club.png"))
window.configure(bg="white")
window.title("Home Window")
f=StringVar()
l=Label(window,text="Your email-address:  ",font = ("Times New Roman", 13)).grid(row = 1,column=1,pady=15)
Entry(window,textvariable=f,borderwidth=7,relief='sunken').grid(row=1,column=2,ipadx=50,pady=40,padx=5)

def print_sel1(e):
    text=f.get()
    y=cal1.get_date()

    
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    t="insert into checkin values('{}','{}')".format(text,y)
    try:
        mycursor.execute(t)
        con.commit()
    except:
        con.rollback() 
def print_sel2(e):
        text=f.get()
        l=cal.get_date()
        import mysql.connector
        con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
        mycursor=con.cursor()
        sq="insert into checkout values('{}','{}')".format(text,l)
        try:
            mycursor.execute(sq)
            con.commit()
        except:
            con.rollback()        
def callback1(eventObject):
    # you can also get the value off the eventObject
    text=f.get()
    l=list()
    a=eventObject.widget.get()  
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    sq="insert into rooms values('{}',{})".format(text,a)
    try:
        mycursor.execute(sq)
        con.commit()
    except:
        con.rollback()

def callback2(eventObject):
    l=list()
    text=f.get()
    # you can also get the value off the eventObject
  
    b=eventObject.widget.get()
    
    
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    sq="insert into typeroom values('{}','{}')".format(text,b)
    try:
        mycursor.execute(sq)
        con.commit()
    except:
        con.rollback()  
def callback3(eventObject):
    text=f.get()
    # you can also get the value off the eventObject
    c=eventObject.widget.get()
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    sq="insert into children values('{}',{})".format(text,c)
    try:
        mycursor.execute(sq)
        con.commit()
    except:
        con.rollback()

def callback4(eventObject):
    text=f.get()

    d=eventObject.widget.get()
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    sq="insert into adult values('{}',{})".format(text,d)
    try:
        mycursor.execute(sq)
        con.commit()
    except:
        con.rollback()
o=Button(window,image=photo)
o.grid(row=5,column=0)
l=Label(window, text = " Rooms :",font = ("Times New Roman", 13))
l.grid( column=1,row=5,pady=15) 
n = StringVar() 
monthchoosen =ttk.Combobox(window, textvariable = n,width=20) 
monthchoosen['values'] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")
monthchoosen.current(0)
monthchoosen.grid(column = 2, row = 5,ipadx=30,pady=15)
monthchoosen.bind("<<ComboboxSelected>>", callback1)
o1=Button(window,image=photo1)
o1.grid(row=6,column=0,pady=15)
m=Label(window, text = " Room Type :",font = ("Times New Roman", 13))
m.grid(column = 1,row = 6) 
n = StringVar() 
monthchoosen =ttk.Combobox(window, width = 27, textvariable = n) 
monthchoosen['values'] = ("Special Suite","Type A","Type B","Type C","Type D")
monthchoosen.current(0)
monthchoosen.grid(column = 2, row = 6)
monthchoosen.bind("<<ComboboxSelected>>", callback2)
o2=Button(window,image=photo2)
o2.grid(row=7,column=0,pady=15)
k=Label(window, text = "  Children :",font = ("Times New Roman", 13))
k.grid(column = 1,row = 7) 
n = StringVar() 
monthchoosen =ttk.Combobox(window, width = 27, textvariable = n) 
monthchoosen['values'] = ("0","1","2","3","4","5","6","7","8","9","10")
monthchoosen.current(0)
monthchoosen.grid(column = 2, row = 7)
o3=Button(window,image=photo31)
o3.grid(row=8,column=0,pady=15)
monthchoosen.bind("<<ComboboxSelected>>", callback3)
i=Label(window, text = "  Adult :",font = ("Times New Roman", 13))
i.grid(column = 1,row = 8,  pady = 25) 
n = StringVar() 
monthchoosen =ttk.Combobox(window, width = 27, textvariable = n) 
monthchoosen['values'] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30") 
monthchoosen.current(0)
monthchoosen.grid(column = 2, row = 8)
monthchoosen.bind("<<ComboboxSelected>>", callback4)
o4=Button(window,image=photo4)
o4.grid(row=9,column=0)
Label(window, text = "Check-in Date :",font = ("Times New Roman", 13)).grid(column = 1,row = 9, pady = 25) 
cal1 = DateEntry(window, width=12, year=2019, month=6, day=22,background='darkblue', foreground='white', borderwidth=2)
cal1.grid(row=9,ipadx=55,column=2,pady=10)
cal1.bind("<<DateEntrySelected>>", print_sel1)
o5=Button(window,image=photo4)
o5.grid(row=10,column=0)
Label(window, text = "Check-out Date :",font = ("Times New Roman", 13)).grid(column = 1,row = 10, pady = 25) 
cal = DateEntry(window, width=12, year=2019, month=6, day=22,background='darkblue', foreground='white', borderwidth=2)
cal.grid(row=10,ipadx=55,column=2,pady=40)
cal.bind("<<DateEntrySelected>>", print_sel2)
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
root=Tk()
root.title("DETAILS OF ROOM")
root.geometry("500x500")
C = Canvas(root, height=20, width=30)
filename = ImageTk.PhotoImage(Image.open(r'C:\Users\DOLA BANERJEE\Downloads\bedroom1.jpg'),master=root)
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack(side="bottom",fill="both")
a=Label(root, text = "Details Of Each Categories Of Rooms",background = 'blue', foreground ="white",font = ("Forte", 20))
a.pack(padx=10,pady=10)
def selected(event):
    if clicked.get()=='Platinum Club Premium Room':
        mylabel=Label(root,background='light blue',foreground ="black", text="\nCost/per room-Rs15500\nFeatures a luxurious bathroom with a separate shower cubicle and large bathtub.\n A host of amenities like magazine and 24-hour butler are provided.\n Extras include 10% discount on spa .",font = ("Times New Roman", 13)).pack()
    if clicked.get()=='Type A':
        mylabel=Label(root,background='light blue',foreground ="black", text="\nCost/per room-Rs13500\n1 large double bed\n Offering city or pool view, the air-conditioned rooms\nfeature a minibar and flat-screen cable TV.\n The Type A bathrooms come with a bathtub and shower.",font = ("Times New Roman", 13)).pack()
    if clicked.get()=='Type B':
        mylabel=Label(root,background='light blue',foreground ="black", text="\nCost/per room-Rs11500\nRoom on the high floor offers panoramic views of the city or pool.\nExecutive Suite,1 way transfer,\nLounge Access,Cocktail Hours",font = ("Times New Roman", 13)).pack()
    if clicked.get()=='Type C':
        mylabel=Label(root,background='light blue',foreground ="black", text="\nCost/per room-Rs10500\nLarge room features a balcony.\n Guests enjoy free high-tea, cocktails and\n a free 1-way transfer from airport to hotel.",font = ("Times New Roman", 13)).pack()
    if clicked.get()=='Type D':
        mylabel=Label(root,background='light blue',foreground ="black", text="\nCost/per room-Rs7500\nFeaturing classical decor, \nroom offers city or pool view.\nA host of amenities like magazine and 24-hour butler are provided. ",font = ("Times New Roman", 13)).pack()
        label=Label(root,background='light blue',foreground ="black", font=13,text="Type D").pack()
    else:
        mylabel=Label(root,background='light blue',foreground ="black",font=13 ,text=clicked.get()).pack()
options=["Platinum Club Premium Room","Type A","Type B","Type C","Type D"]
clicked=StringVar()
clicked.set(options[0])
drop=OptionMenu(root,clicked,*options,command=selected)
drop.pack(pady=20,ipadx=70)
def club():
    import tkinter as tk
    from tkinter import ttk
    from PIL import ImageTk,Image
    root=tk.Tk()
    root.geometry("500x500")
    C = tk.Canvas(root, height=20, width=30)
    filename = ImageTk.PhotoImage(Image.open(r'C:\Users\DOLA BANERJEE\Downloads\party.jpg'),master=root)
    background_label = tk.Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack(side="bottom",fill="both")
    a=tk.Label(root, text = "LETS HAVE PARTY TONIGHT IN OUR NIGHT SPOT",background = 'blue', foreground ="white",font = ("Forte", 20))
    a.pack(padx=10,pady=10)
    def selected(event):
        if clicked.get()=='CLUB':
            mylabel=tk.Label(root,bg="pink",foreground ="black", text='''\nSpecial passes for premium members.\nFrom 1 March to 5 March we are having a\n MUSIC FESTIVAL ORGANISED.\nCome on and enjoy your nights here.\nCLUB TIMINGS:2200-0300 ''',font = ("Times New Roman", 13)).pack()
        if clicked.get()=='SPECIAL THEMES':
            mylabel=tk.Label(root,background='pink',foreground ="black", text='''\nWe are having special theme parties everyday.\nThis weekend special:\nMonday:Masks and Mimosa,Tuesday:Tropical Savanna\nWednesday:Glow in the Day,Thursday:Seven Deadly Sins\nFriday:Bubbles in Boca,Saturday:Arabian Nights\nSunday:Flamingo Flau '''
            ,font = ("Times New Roman", 13)).pack()
        if clicked.get()=='DIWALI PARTY SPECIAL':
            mylabel=tk.Label(root, background='pink',foreground ="black", text='''\nTimings:0900-1400\nAll arrangements will be done by us.\nBoueffe system will be there.'''
            ,font = ("Times New Roman", 13)).pack()
        if clicked.get()=='KIDS PLAY':
            mylabel=tk.Label(root, background='pink',foreground ="black", text='''\nA warm and loving environment for your child.\nCome and explore our fun playful heaven.\n\nTimings:0800-20000hrs\nAge limit:5 yrs-9 yr'''
            ,font = ("Times New Roman", 13)).pack()
            label=Label(root,background='pink',foreground ="black", text="KIDS PLAY",font=13).pack()
        else:
            mylabel=tk.Label(root,background='pink',foreground ="black", font=13, text=clicked.get()).pack()
    options=['CLUB','SPECIAL THEMES','DIWALI PARTY SPECIAL','KIDS PLAY']
    clicked=tk.StringVar()
    clicked.set(options[0])
    drop=tk.OptionMenu(root,clicked,*options,command=selected)
    drop.pack(pady=20,ipadx=70)
    root.mainloop()

def rest():
    import tkinter as tk
    from PIL import ImageTk, Image
    my_w = tk.Tk()
    my_w.title("DETAILS(KITCHEN CORNER)")
    my_w.geometry("500x500")
    my_w.configure(bg='cyan')
    photo=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\o.jpg"),master=my_w)
    o3=tk.Button(my_w,image=photo)
    o3.grid(row=5,column=4,padx=30,pady=20)
    photo1=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\th (3).jpg"),master=my_w)
    o4=tk.Button(my_w,image=photo1)
    o4.grid(row=11,column=4,padx=30,pady=20)
    photo2=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\Dal_Makhni_&_Shahi_Paneer.jpg"),master=my_w)
    o5=tk.Button(my_w,image=photo2)
    o5.grid(row=15,column=4,padx=30,pady=20)
    def my_upd(my_widget):
        try:
            my_w = my_widget.widget
            index = int(my_w.curselection()[0])
            value = my_w.get(index) 
        except Exception:
            pass  
        try:
            value1=f.get()
            import mysql.connector
            con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
            mycursor=con.cursor()
            sq1="insert into breakfast values('{}','{}')".format(value1,value)
            mycursor.execute(sq1)
            con.commit()
        except Exception:
            pass
    l1 = tk.Listbox(my_w,height=5,width=35,font = ("forte", 20),foreground='navy blue')
    l1.grid(row=5,column=1,pady=30)
    
    my_list=['CHOLE-BHATURE','STUFFED PARATHAS','PANEER TIKKA','BREAD-BUTTER','SANDWICH','GREEK YOGURT']
    l=tk.Label(my_w,text="BREAKFAST",font = ("Times New Roman", 25)).grid(row = 5,column=0, padx = 10,pady=15)  
    for element in my_list:
        l1.insert(tk.END,element)
   
    l1.bind('<<ListboxSelect>>', my_upd)
    def my_upd1(my_widget):
        try:
            my_w = my_widget.widget
            index = int(my_w.curselection()[0])
            value2 = my_w.get(index)
        except Exception:
            pass
  
        try:
            value3=f.get() 
            import mysql.connector
            con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
            mycursor=con.cursor()
            sq1="insert into lunch values('{}','{}')".format(value3,value2)
            mycursor.execute(sq1)
            con.commit()
        except Exception:
            pass
    l1 = tk.Listbox(my_w,height=5,width=35,font = ("forte", 20),foreground='navy blue')
    l1.grid(row=11,column=1,pady=30)
   
    my_list=['VEG THALI','RAJMA CHAWAL,RAITA','NON-VEG SPECIAL THALI',
    'NOODLES(HAKKA\PLAIN)','SALAD WITH CHEESE','AMATRICIANA(PASTA)']
    l=tk.Label(my_w,text="LUNCH",font = ("Times New Roman", 25)).grid(row =11 ,column=0, padx = 10,pady=15)  
    for element in my_list:
        l1.insert(tk.END,element)
    
    l1.bind('<<ListboxSelect>>', my_upd1)
    def my_upd2(my_widget):
        try:
            my_w = my_widget.widget
            index = int(my_w.curselection()[0])
            value4 = my_w.get(index)
   
   
        except Exception:
            pass
        try:
            value5=f.get()
            import mysql.connector
            con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
            mycursor=con.cursor()
            sq1="insert into dinner values('{}','{}')".format(value5,value4)
            mycursor.execute(sq1)
            con.commit()
        except Exception:
            pass
    l1 = tk.Listbox(my_w,height=5,width=35,font = ("forte", 20),foreground='navy blue' )
    l1.grid(row=15,column=1,pady=30)
    
    my_list=['DAAL MAKHNI','DOSA AND IDLI WITH DAAL','CHILLI CHICKEN& TANDOORI ROTI','CHICKEN POT PIE','CHEESY RANCH TUNA','BROCCOLI CASSEROLE']
    l=tk.Label(my_w,text="DINNER",font = ("Times New Roman", 25)).grid(row = 15,column=0, padx = 10,pady=15)  
    for element in my_list:
        l1.insert(tk.END,element)
    l1.bind('<<ListboxSelect>>', my_upd2)
    import tkinter as tk
    from tkinter import ttk
    root=tk.Tk()
    root.title("RESTAURANT CORNER")
    root.geometry("500x500")
    C = tk.Canvas(root, height=20, width=30)
    filename = ImageTk.PhotoImage(Image.open(r'C:\Users\DOLA BANERJEE\Downloads\res.jpg'),master=root)
    background_label = tk.Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack(side="bottom",fill="both")
    a=tk.Label(root, text = "Details Of Each Categories Of Food",background = 'blue', foreground ="white",font = ("Forte", 20))
    a.pack(padx=10,pady=10)
    def selected1(event):
        if clicked.get()=='BREAKFAST':
            mylabel=tk.Label(root,bg="light yellow",foreground ="black",text='''\nIndian Dishes\n1.Chole-Bhature with imley chatney\n2.Stuffed parathas\n3.Paneer Tikka\n\nWestern Dishes\n1.Bread-butter/jam,boiled egg/cutlets\n2.Sandwich-sause/mayonnaise\n3.Cornflakes,Fruits,Greek yogurt''',font = ("Times New Roman", 13)).pack()
        if clicked.get()=='LUNCH':
            mylabel=tk.Label(root,bg="light yellow",foreground ="black", text='''\nIndian Dishes\n1.Veg Thali\n2.Rajma chawal,raita\n3.Non-Veg Special Thali\n\nWestern Dishes\n1.Noodles(Hakka/Plain) with Tai-Tai sauce\n2.Caesar salad wirh cheese\n3Italian special-Amatriciana(pasta). '''
            ,font = ("Times New Roman", 13)).pack()
        if clicked.get()=='DINNER':
            mylabel=tk.Label(root,bg="light yellow",foreground ="black", text='''\nIndian Dishes\n1.Daal Makhni\n2.Dosa and Idli with daal\n3.Chilli chicken & Tandoori roti\n\nWestern Dishes\n1.Chicken pot pie\n2.Cheesy Ranch tuna\n3.Broccoli Casserole'''  
            ,font = ("Times New Roman", 13)).pack()
            label=tk.Label(root,bg="light yellow",foreground ="black",font=13, text="DINNER").pack() 
        else:
            mylabel=tk.Label(root,bg="light yellow",foreground ="black", font=13,text=clicked.get()).pack()
    options=["BREAKFAST","LUNCH","DINNER"]
    clicked=tk.StringVar()
    drop=tk.OptionMenu(root,clicked,*options,command=selected1)
    drop.pack(ipadx=70,pady=1)
    root.mainloop()
def game():
   import tkinter as tk
   from PIL import ImageTk,Image
   my_w = tk.Tk()
   my_w.geometry("500x500")
   my_w.title("DETAILS(GAME CORNER)")
   my_w.configure(bg='cyan')
   photo=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\nfs.jpg"),master=my_w)
   photo1=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\unnamed.jpg"),master=my_w)
   photo2=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\bowler.jpg"),master=my_w)
   photo3=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\poker.jpg"),master=my_w)
   o3=tk.Button(my_w,image=photo)
   o3.grid(row=6,column=4,padx=30,pady=15)
   o4=tk.Button(my_w,image=photo1)
   o4.grid(row=8,column=4,padx=30,pady=15)
   o5=tk.Button(my_w,image=photo2)
   o5.grid(row=10,column=4,padx=30,pady=15)
   o6=tk.Button(my_w,image=photo3)
   o6.grid(row=12,column=4,padx=30)
   def my_upd(my_widget):
       try:
           my_w = my_widget.widget
           index = int(my_w.curselection()[0])
           value = my_w.get(index)
        
       except:
           IndexError
       try:
           text=f.get()
           import mysql.connector
           con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
           mycursor=con.cursor()
           sq="insert into vgl values('{}','{}')".format(text,value)
           mycursor.execute(sq)
           con.commit()
       except:
           Exception
    
   l=tk.Label(my_w,text="Videogame-Latest games",font = ("Times New Roman", 25) ).grid(row = 6, padx = 10,pady=15)    
   l1 = tk.Listbox(my_w,height=4,width=30,font = ("forte", 20),foreground='navy blue' )
   l1.grid(row=6,column=1,pady=30) 
   my_list=['PUBG-RS100/HR','NEED FOR SPEED-RS60/HR','ROAD RASH-RS60/HR','GTA-RS100/HR','FORTNIGHT-RS70/HR']

   for element in my_list:
       l1.insert(tk.END,element)
    
   l1.bind('<<ListboxSelect>>', my_upd)
   def my(my_widget):
       try:
           my_w = my_widget.widget
           index = int(my_w.curselection()[0])
           value = my_w.get(index)
       
       except:
           IndexError
       try:
           text1=f.get()
           import mysql.connector
           con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
           mycursor=con.cursor()
           sq="insert into vgp values('{}','{}')".format(text1,value)
           mycursor.execute(sq)
           con.commit()
       except:
           Exception
   l=tk.Label(my_w,text="Videogame-popular games",font = ("Times New Roman", 25) ).grid(row = 8, padx = 10,pady=15)    
   l1 = tk.Listbox(my_w,height=4,width=30,font = ("forte", 20),foreground='navy blue' )
   l1.grid(row=8,column=1,pady=30) 
   my_list2=['CALL OF DUTY-RS80/HR','FIFA-RS50/HR','NBA 2K20 RS50/HR','BATTLE FIELD 5-RS 80/HR','FARCRY 5-RS120/HR']

   for element in my_list2:
       l1.insert(tk.END,element)
   l1.bind('<<ListboxSelect>>', my)
   def myy(my_widget):
       try:
            my_w = my_widget.widget
            index = int(my_w.curselection()[0])
            value = my_w.get(index)
       except:
            IndexError
       try:
           text2=f.get()
           import mysql.connector
           con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
           mycursor=con.cursor()
           sq="insert into indoor values('{}','{}')".format(text2,value)
           mycursor.execute(sq)
           con.commit()
       except:
           Exception
   l=tk.Label(my_w,text="Indoor games",font = ("Times New Roman", 25)).grid(row = 10, padx = 10,pady=15)
   l1 = tk.Listbox(my_w,height=4,width=30,font = ("forte", 20),foreground='navy blue' )
   l1.grid(row=10,column=1)
   my_list3=['TABLE TENNIS','BOWLING','SNOOKER','SQUASH','POKER','BILLIARD']
   for element in my_list3:
       l1.insert(tk.END,element)
   l1.bind('<<ListboxSelect>>', myy)
   def myy(my_widget):
       try:
           my_w = my_widget.widget
           index = int(my_w.curselection()[0])
           value = my_w.get(index)
       except:
           IndexError
       try:
           text3=f.get()
           import mysql.connector
           con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
           mycursor=con.cursor()
           sq="insert into addg values('{}','{}')".format(text3,value)
           mycursor.execute(sq)
           con.commit()
       except:
           Exception
  
       
   l=tk.Label(my_w,text="Additional games",font = ("Times New Roman", 25)).grid(row = 12, padx = 10,pady=60)    
   l1 = tk.Listbox(my_w,height=4,width=30,font = ("forte", 20),foreground='navy blue' )
   l1.grid(row=12,column=1) 
   my_list4=['POKER','BILLIARD','POKER AND BILLIARD']

   for element in my_list4:
       l1.insert(tk.END,element)
    
   l1.bind('<<ListboxSelect>>', myy)     
   import tkinter as tk
   from tkinter import ttk
   root=tk.Tk()
   root.title("GAME CORNER")
   root.geometry("500x500")
   C = tk.Canvas(root, height=20, width=30)
   filename = ImageTk.PhotoImage(Image.open(r'C:\Users\DOLA BANERJEE\Downloads\game.png'),master=root)
   background_label = tk.Label(root, image=filename)
   background_label.place(x=0, y=0, relwidth=1, relheight=1)
   C.pack(side="bottom",fill="both")
   a=tk.Label(root, text = "Details Of Each Categories Of Game",background = 'blue', foreground ="white",font = ("Forte", 20))
   a.pack(padx=10,pady=10)
   def selected(event):
       if clicked.get()=='VIDEO GAMES':
           mylabel=tk.Label(root,foreground="black",background="light pink" ,text='''\n\nNew package of Virtual Reality games\n also available\nAll the above mentioned games will cost twice per hr in VR\nSPECIAL DISCOUNTS ON FIRST 30\n CUSTOMERS-HOLI SPECIAL(2 March-5 March ''',font = ("Times New Roman", 13)).pack()
       if clicked.get()=='INDOOR GAMES':
           mylabel=tk.Label(root,foreground="black",background="light pink", text='''\n\nMorning timings:0930-11300hrs\nEvening Timings:1700-1900 hrs\n\nSwimming pool timings:1000-1700 hrs '''
          ,font = ("Times New Roman", 13)).pack()
       if clicked.get()=='ADDITIONAL GAMES':
           mylabel=tk.Label(root, foreground="black",background="light pink",text='''\n\nMorning timings:0930-11300hrs\nEvening Timings:1700-1900 hrs'''
          ,font = ("Times New Roman", 13)).pack()
           label=tk.Label(root,foreground="black",background="light pink",font=13, text="ADDITIONAL GAMES").pack()
       else:
           mylabel=tk.Label(root,text=clicked.get(),foreground="black",background="light pink",font=13 ).pack()
   options=['VIDEO GAMES','INDOOR GAMES','ADDITIONAL GAMES']
   clicked=StringVar()
   drop=tk.OptionMenu(root,clicked,*options,command=selected)
   drop.pack(pady=20,ipadx=70)
   root.mainloop()
def main():
    val=f.get()
    ran=random.randint(500,1000)
    ran1=random.randint(1000,5000)
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    sql="select check_in_date from checkin where registered_name='{}'".format(val)
    mycursor.execute(sql)
    result=mycursor.fetchall()
    l11=list()
    l22=list()
    e=list()
    for i in result:
        l11.append(i[0])
    sql1="select check_out_date from checkout where registered_name='{}'".format(val)     
    mycursor.execute(sql1)
    r=mycursor.fetchall()
    for u in r:
        l22.append(u[0])
    for j in range(len(l11)):
        for k in range(len(l22)):
            if j==k:
              
                l11[j]=str(l11[j])
                l22[k]=str(l22[k])
                day1 = datetime.strptime(l11[j], '%Y-%m-%d').date()
                day2 = datetime.strptime(l22[k], '%Y-%m-%d').date()
                diff = day2 - day1
                a=(diff.days)+2
                e.append(a)
    import tkinter as tk
    w=tk.Tk()
    w.title("bill")
    p1=val+str(ran)+".txt"
    file=open(p1,"w")
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    li=list()
    li1=list()
    li2=list()
    food=list()
    game=list()
    typ=list()
    sq="select room from rooms where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchone()
    for i in result:
        li.append(i)
    sq="select check_in_date from checkin where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchone()
    for i in result:
        li.append(i)
    sq1="select check_out_date from checkout where registered_name='{}'".format(val)
    mycursor.execute(sq1)
    result=mycursor.fetchone()
    for i in result: 
        li.append(i)    
    li.extend(e)
    sq="select room_type from typeroom where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        typ.append(i)
    li.append(typ)
    li1.append(li)
    a1=tabulate(li1,headers=['\n\nNo. of\nrooms','\n\nCheck-in\nDate','\n\nCheck-out\nDate','\n\nDwell Time','\n\n\tType of room'])
    sq="select name,email_address,phone_number,address from main1 where email_address='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        li2.append(i)
    b=tabulate(li2,headers=['\n\n\nName','\n\n\nEmail-address','\n\n\nPhone no','\n\n\nAddress']) 
    sq="select lunch from lunch where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        food.append(i)
    sq="select dinner from dinner where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        food.append(i)
    sq="select breakfast from breakfast where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        food.append(i)
    if food!=[]:
        cd=tabulate([["YES"]],headers=["\n\n\nFood-Packages"])
    if food==[]:
        cd=tabulate([["NO"]],headers=["\n\n\nFood Packages"])
    sq="select popular_games from vgp where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        game.append(i)
    sq="select popular_games from vgp where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        game.append(i)
    sq="select popular_games from vgp where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        game.append(i)
    sq="select latest_games from vgl where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        game.append(i)
    sq="select indoor_games from indoor where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        game.append(i)
    sq="select add_games from addg where registered_name='{}'".format(val)
    mycursor.execute(sq)
    result=mycursor.fetchall()
    for i in result:
        game.append(i)
    if game!=[]:
            d=tabulate([["YES"]],headers=["\n\n\nGame-Packages"])
    if game==[]:
       d=tabulate([["NO"]],headers=["\n\n\nGame-Packages"]) 
    c1=0
    for i in typ:
        if i==('Special Suite',):
            c1=c1+15500
        if i==('Type A',):
            c1=c1+13500
        if i==('Type B',):
            c1=c1+11500
        if i==('Type C',):
            c1=c1+10500
        if i==('Type D',):
            c1=c1+7500
    for m in e:
        c1=c1*m
    c2=((c1+500+375)*0.05)+c1
    e=tabulate([[c1,500,"             "+"375"]],headers=["\n\n\nSubTotal","\n\n\nServiceTax","\n\n\nLuxuryTax"])
    z=tabulate([[c2]],headers=["\n\nTotal(includig 5% Sales Tax)"])
    file.write("\nPLATINUM HOTEL")
    file.write("\n\nBILL")
    file.write(b)
    file.write(a1)
    file.write(cd)
    file.write(d)
    file.write(e)
    file.write(z)
    file.write("\t\t\t\tAll transactions must be done in Rupees")

    file.close()
    p=val+str(ran)+".txt"
    file=open(p,"r+")
    stuff=file.read()
    my_text=tk.Text(w,width=250,height=50,font=("Times New Roman", 15))
    my_text.pack(pady=20)
    my_text.insert(tk.END,"\t\t\t\t\t\t\t\t\t\t\t\t\t\tInvoice no:\t")
    my_text.insert(tk.END,ran)
    my_text.insert(tk.END,"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tCustomer Id:")
    my_text.insert(tk.END,ran1)
    my_text.insert(tk.END,stuff)
    file.close()
    co1="delete from rooms where registered_name='{}'".format(val)

    co2="delete from typeroom where registered_name='{}'".format(val)
    co3="delete from children where registered_name='{}'".format(val)
  
    co4="delete from adult where registered_name='{}'".format(val)

    co5="delete from checkin where registered_name='{}'".format(val)

    co6="delete from checkout where registered_name='{}'".format(val)

    co7="delete from main1 where email_address='{}'".format(val)
  
    co8="delete from lunch where registered_name='{}'".format(val)

    co9="delete from breakfast where registered_name='{}'".format(val)

    co10="delete from dinner where registered_name='{}'".format(val)
  
    co11="delete from vgp where registered_name='{}'".format(val)

    co12="delete from vgl where registered_name='{}'".format(val)

    co13="delete from indoor where registered_name='{}'".format(val)

    co14="delete from addg where registered_name='{}'".format(val)
    mycursor.execute(co1)
    mycursor.execute(co2)
    mycursor.execute(co3)
    mycursor.execute(co4)
    mycursor.execute(co5)
    mycursor.execute(co6)
    mycursor.execute(co7)
    mycursor.execute(co8)
    mycursor.execute(co9)
    mycursor.execute(co10)
    mycursor.execute(co11)
    mycursor.execute(co12)
    mycursor.execute(co13)
    mycursor.execute(co14)
    con.commit()
def q():
  from tkinter import messagebox
  messagebox.showinfo("(:", "THANK YOU FOR VISITING OUR HOTEL")
  quit()
o7=Button(window,image=photo7)
o7.grid(row=16,column=0)
o8=Button(window,image=photo8)
o8.grid(row=14,column=0)
o9=Button(window,image=photo9)
o9.grid(row=14,column=2)
o10=Button(window,image=photo10)
o10.grid(row=15,column=0)
b=Button(window,text="Final Bill",command=main,foreground ="blue",font = ("Times New Roman", 12),borderwidth=7,relief='sunken')
b.grid(row = 16,column=1,ipadx=40)
b1=Button(window,text="Restaurant Corner",command=rest,foreground ="blue",font = ("Times New Roman", 12),borderwidth=7,relief='sunken')
b1.grid(row = 14,column=1,pady=20)
b2=Button(window,text="Games Corner",command=game,foreground ="blue",font = ("Times New Roman", 12),borderwidth=7,relief='sunken')
b2.grid(row = 14,column=3,pady=20,ipadx=40)
b3=Button(window,text="Club Corner",command=club,foreground ="blue",font = ("Times New Roman", 12),borderwidth=7,relief='sunken')
b3.grid(row = 15,column=1,pady=20,ipadx=30)
b3=Button(window,text="Quit",command=q,foreground ="blue",font = ("Times New Roman", 12),borderwidth=7,relief='sunken')
b3.grid(row = 18,column=1,pady=40,ipadx=40)