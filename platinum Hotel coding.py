import tkinter
from PIL import ImageTk,Image
root=tkinter.Tk()
root.title("customer details ")
root.geometry("1000x800")
C = tkinter.Canvas(root, height=10, width=10)
filename = ImageTk.PhotoImage(Image.open(r'C:\Users\DOLA BANERJEE\Downloads\plat.jpeg'))
background_label = tkinter.Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack(side="bottom",fill="both",expand="yes")
i=tkinter.StringVar()
k=tkinter.StringVar()
g=tkinter.IntVar()
h=tkinter.StringVar()
l=tkinter.Label(root,text="PLATINUM HOTEL",font = ("Algerian", 50),foreground='yellow',background='blue').pack(pady=20)
l=tkinter.Label(root,text="NAME",font = ("Forte", 20),foreground='red',background='pink').pack(pady=10)
tkinter.Entry(root,textvariable=i,borderwidth=2,relief="sunken").pack(ipadx=30,pady=15)
l=tkinter.Label(root,text="E-MAIL ADDRESS",font = ("Forte", 20),foreground='red',background='pink').pack(pady=10)
tkinter.Entry(root,textvariable=k,borderwidth=2,relief="sunken").pack(ipadx=30,pady=15)
l=tkinter.Label(root,text="PHONE-NUMBER",font = ("Forte", 20),foreground='red',background='pink').pack( pady=10)
tkinter.Entry(root,textvariable=g,borderwidth=2,relief="sunken").pack(ipadx=30,pady=15)
l=tkinter.Label(root,text="ADDRESS",font = ("Forte", 20),foreground='red',background='pink').pack(pady=15)
tkinter.Entry(root,textvariable=h,borderwidth=2,relief="sunken").pack(ipadx=30,pady=15)
def database():
    text2=i.get()
    text3=k.get()
    text4=g.get()
    text5=h.get()
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    qs="insert into main1 values('{}','{}','{}','{}')".format(text2,text3,text4,text5)
    try:
        mycursor.execute(qs)
        con.commit()
    except:
        con.rollback()
    from subprocess import call
    with open("r1.txt","w") as f2:
        call(['Thonny',r'C:\Users\DOLA BANERJEE\Downloads\home 4.py'],stdout=f2)
tkinter.Button(root,text="CLICK ME",command=database,foreground ="white",background='navy blue',relief="sunken",borderwidth=4,font = ("Times New Roman", 15)).pack(pady=35)