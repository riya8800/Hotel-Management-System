import tkinter
from PIL import ImageTk,Image
from tkinter import ttk 
root=tkinter.Tk()
root.title("login")
root.geometry('700x300')
photo=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\user.png"))
photo1=ImageTk.PhotoImage(Image.open(r"C:\Users\DOLA BANERJEE\Downloads\password.png "))
e=tkinter.StringVar()
f=tkinter.StringVar()
o2=tkinter.Button(root,image=photo)
o2.grid(row=4,column=0,pady=15)
o3=tkinter.Button(root,image=photo1)
o3.grid(row=5,column=0,pady=15)
tkinter.Label(root, text = "LOGIN",font = ("Forte", 30)).grid(row = 0, column = 1)  
l=tkinter.Label(root,text="Username",font = ("Times New Roman", 17)).grid(row = 4,pady=15,column=1)
tkinter.Entry(root,textvariable=e,borderwidth=7,relief='sunken').grid(row=4,column=2,ipadx=30)
tkinter.Label(root,text="Password",font = ("Times New Roman", 17)).grid(row = 5,column=1)
tkinter.Entry(root,show="*",textvariable=f,borderwidth=7,relief='sunken').grid(row=5,column=2,ipadx=30)
def sql1():
    text=e.get()
    text1=f.get()
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    sq="insert into main values('{}',{})".format(text,text1)
    try:
        mycursor.execute(sq)
        con.commit()
        from tkinter import messagebox
        messagebox.showinfo("registered", "REGISTERED")
    except:
        con.rollback()   
def sql2():
    text=e.get()
    text1=f.get()
    import mysql.connector
    con=mysql.connector.connect(user="root",password="aditya19",host="localhost",database="alisha")
    mycursor=con.cursor()
    sql="select name from main"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    l=list()
    l1=list()
    d=dict()
    for i in result:
        l.append(i[0])
    con.commit()
    sql1="select password from main"     
    mycursor.execute(sql1)
    r=mycursor.fetchall()
    for j in r:
        l1.append(j[0])
    for k in l:
        for u in l1:
            d[k]=u
            l1.remove(u)
            break
    text=str(text)
    text1=int(text1)
    if text in d.keys() and d[text]==text1:
        from tkinter import messagebox
        messagebox.showinfo("logged in", "LOGGED IN")
        from subprocess import call
        with open("r1.txt","w") as f2:
            call(['Thonny',r'C:\Users\DOLA BANERJEE\Downloads\platinum 3.py'],stdout=f2)    
    if text not in d.keys():
        from tkinter import messagebox
        messagebox.showerror("ERROR", "NOT A VALID USER")
    if text in d.keys() and d[text]!=text1:
        from tkinter import messagebox
        messagebox.showerror("ERROR", "WRONG PASSWORD")
def sql3():
    from subprocess import call
    with open("r.txt","w") as f1:
        call(['Thonny',r'C:\Users\DOLA BANERJEE\Downloads\reset pass 2.py'],stdout=f1)    
tkinter.Button(root,text="Forget password?",command=sql3,foreground ="blue",font = ("Times New Roman", 13)).grid(row = 7,pady=13,column=1)
tkinter.Button(root,text="click me",command=sql2,foreground ="blue",font = ("Times New Roman", 13)).grid(row = 7,pady=13,column=0,padx=30)
tkinter.Button(root,text="Register now",command=sql1,foreground ="blue",font = ("Times New Roman", 13)).grid(row = 7,pady=13,padx=10,column=2)
root.mainloop()