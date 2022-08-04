import tkinter
from PIL import ImageTk,Image
root=tkinter.Tk()
root.geometry('800x400')
root.title('editing password')
photo=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\user.png"))
photo1=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\password.png"))
o2=tkinter.Button(root,image=photo)
o2.grid(row=4,column=0,pady=15)
o3=tkinter.Button(root,image=photo1)
o3.grid(row=5,column=0,pady=15)
y=tkinter.StringVar()
x=tkinter.StringVar()
tkinter.Label(root, text = "RESETTIING PASSWORD....",background = 'blue', foreground ="white",font = ("Forte", 19)).grid(row = 0, column = 1,pady=20)  
tkinter.Label(root,text='Enter Username',font = ("Times New Roman ", 17)).grid(row = 4,column=1,)
tkinter.Entry(root,textvariable=y,borderwidth=7,relief='sunken').grid(row=4,column=2,ipadx=40)
tkinter.Label(root,text='Enter new Password',font = ("Times New Roman", 17)).grid(row = 5,column=1,pady=15)
tkinter.Entry(root,textvariable=x,show="*",borderwidth=7,relief='sunken').grid(row=5,column=2,ipadx=40)
def rxx():
    p=x.get()
    q=y.get()
    import mysql.connector
    con=mysql.connector.connect(host="localhost",user="root",password="aditya19",database="alisha")
    mycursor=con.cursor()
    st="update main SET password='{}' where name='{}'".format(p,q)
    try:
        mycursor.execute(st)
        con.commit() 
    except:
        con.rollback()
    from tkinter import messagebox
    messagebox.showinfo("","PASSWORD CHANGED\nSUCCESFULLY")
    from subprocess import call
    with open("r3.txt","w") as f3:
            call(['Thonny',r'C:\Users\DOLA BANERJEE\Downloads\login1.py'],stdout=f3)
tkinter.Button(root,text="change password",command=rxx,foreground ="blue",font = ("Times New Roman", 15)).grid(row = 7,pady=13,column=1)

    


    

