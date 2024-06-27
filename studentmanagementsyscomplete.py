from tkinter import*
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
import pandas
import pymysql.cursors

root=Tk()
root.title('Student Management System')
root.config(bg='#F05B56')
root.geometry('1150x686+55+0')
root.iconbitmap('icon.ico')

root.resizable(False,False)


def Connectdb():
    def submitdb():
        global con, mycursor
        host=hostval.get()
        user=userval.get()
        password=passval.get()
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror("Notification","Cannot connect to server",parent=dbroot)
            return
        try:
            strr='create database studentmanagementsystem'
            mycursor.execute(strr)
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            strr='create table studentdata(id int primary key not null,name varchar(20),mobile varchar(12),email varchar(30),address varchar(50),gender varchar(10),dob varchar(11),added_date varchar(11),added_time varchar(30))'
            mycursor.execute(strr)
            messagebox.showinfo("Notification","Database created and connection successful",parent=dbroot)
        except:
            strr='use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo("Notification","Connection successful",parent=dbroot) 
        dbroot.destroy()
        strr='select* from studentdata'
        mycursor.execute(strr)
        stdata=mycursor.fetchall()
        for i in stdata:
            v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert("",END,values=v)

    dbroot=Toplevel()
    dbroot.geometry('450x250+805+250')
    dbroot.config(bg='#F04842')
    dbroot.grab_set()
    dbroot.iconbitmap('icon.ico')
    dbroot.resizable(False,False)
    
    #----------------------------------------
    idlabel=Label(dbroot,text="Enter Host :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=15)
    idlabel.place(x=10,y=20)
    
    userlabel=Label(dbroot,text="Enter user :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=15)
    userlabel.place(x=10,y=70)
    
    passlabel=Label(dbroot,text="Enter Password :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=15)
    passlabel.place(x=10,y=120)
    
    #---------------------------------------------------------------------------------------------------------------------
    hostval=StringVar()
    userval=StringVar()
    passval=StringVar()
    hostentry=Entry(dbroot,bd=3,font=('sitika',15),textvariable=hostval,width=16)
    hostentry.place(x=252,y=20)
    
    userentry=Entry(dbroot,bd=3,font=('sitika',15),textvariable=userval,width=16)
    userentry.place(x=252,y=70)
    
    passentry=Entry(dbroot,bd=3,font=('sitika',15),textvariable=passval,width=16)
    passentry.place(x=252,y=120)
    #-------------------------------------------------------------------------------------------------------------------------
    submit=Button(dbroot,text="Submit",font=('Granger',19,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=16,activebackground='#F3DFA2',activeforeground='#ED231D',bd=3,command=submitdb)
    submit.place(x=110,y=180)
    dbroot.mainloop()

###############################################################################[data entry frame]
DataEntryF=Frame(root,bg='#F3DFA2',relief=GROOVE,borderwidth=5)
DataEntryF.place(x=40,y=76,height=600,width=500)
#------------------------------------------------------------------------------
def add():
    def submitadd():
        id=idvar.get()
        name=namevar.get()
        mobile=mobvar.get()
        email=emailvar.get()
        address=addressvar.get()
        gender=genvar.get()
        dob=dobvar.get()
        added_date=time.strftime("%d/%m/%Y")
        added_time=time.strftime('%H:%M:%S')
        try:
            strr='insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,added_date,added_time))
            con.commit()
            res=messagebox.askyesno('Notification','Data has been added... Do you want to clear form?',parent=addroot)
            if res==True:
                idvar.set("")
                namevar.set("")
                mobvar.set("")
                emailvar.set("")
                addressvar.set("")
                genvar.set("")
                dobvar.set("")

        except:
            messagebox.showerror('Notification','Either database not connected or ID already exists')

        strr='select* from studentdata'
        mycursor.execute(strr)
        stdata=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in stdata:
            v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert("",END,values=v)
        


    addroot=Toplevel(master=DataEntryF)
    addroot.geometry('450x450+125+140')
    addroot.config(bg='#F04842')
    addroot.grab_set()
    addroot.iconbitmap('icon.ico')
    addroot.resizable(False,False)
    #-----------------------------------------------------------------------
    idlabel=Label(addroot,text="Enter ID :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    idlabel.place(x=10,y=20)
    
    Namelabel=Label(addroot,text="Enter Name :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    Namelabel.place(x=10,y=70)
    
    moblabel=Label(addroot,text="Enter Mobile :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    moblabel.place(x=10,y=120)
    
    emailabel=Label(addroot,text="Enter Email :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    emailabel.place(x=10,y=170)
    
    addresslabel=Label(addroot,text="Enter Address :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    addresslabel.place(x=10,y=220)
    
    genlabel=Label(addroot,text="Enter Gender :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    genlabel.place(x=10,y=270)
    
    doblabel=Label(addroot,text="Enter D.O.B. :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    doblabel.place(x=10,y=320)

    submit=Button(addroot,text="Submit",font=('Granger',19,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14,activebackground='#F3DFA2',activeforeground='#ED231D',bd=3,command=submitadd)
    submit.place(x=110,y=370)
    #------------------------------------------------------------------------------------------------------------------------------
    idvar=StringVar()
    namevar=StringVar()
    mobvar=StringVar()
    emailvar=StringVar()
    addressvar=StringVar()
    genvar=StringVar()
    dobvar=StringVar()
    
    identry=Entry(addroot,bd=3,font=('sitika',15),textvariable=idvar,width=17)
    identry.place(x=245,y=20)
    
    namentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=namevar,width=17)
    namentry.place(x=245,y=70)
    
    mobentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=mobvar,width=17)
    mobentry.place(x=245,y=120)
    
    emailentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=emailvar,width=17)
    emailentry.place(x=245,y=170)
    
    addressentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=addressvar,width=17)
    addressentry.place(x=245,y=220)
    
    genentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=genvar,width=17)
    genentry.place(x=245,y=270)
    
    dobentry=Entry(addroot,bd=3,font=('sitika',15),textvariable=dobvar,width=17)
    dobentry.place(x=245,y=320)
    
    addroot.mainloop()
    
def search():
    def submitsearch():
        id=idvar.get()
        name=namevar.get()
        mobile=mobvar.get()
        email=emailvar.get()
        address=addressvar.get()
        gender=genvar.get()
        dob=dobvar.get()
        added_date=time.strftime("%d/%m/%Y")
        
        if (id!=""):
            strr='select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            stdata=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in stdata:
                v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert("",END,values=v)
        
        elif (name!=""):
            strr='select * from studentdata where name=%s'
            mycursor.execute(strr,(name))
            stdata=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in stdata:
                v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert("",END,values=v)
        
        elif (mobile!=""):
            strr='select * from studentdata where mobile=%s'
            mycursor.execute(strr,(mobile))
            stdata=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in stdata:
                v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert("",END,values=v)

        elif (email!=""):
            strr='select * from studentdata where email=%s'
            mycursor.execute(strr,(email))
            stdata=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in stdata:
                v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert("",END,values=v)

        elif (address!=""):
            strr='select * from studentdata where address=%s'
            mycursor.execute(strr,(address))
            stdata=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in stdata:
                v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert("",END,values=v)

        elif (gender!=""):
            strr='select * from studentdata where gender=%s'
            mycursor.execute(strr,(gender))
            stdata=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in stdata:
                v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert("",END,values=v)

        elif (dob!=""):
            strr='select * from studentdata where dob=%s'
            mycursor.execute(strr,(dob))
            stdata=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in stdata:
                v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert("",END,values=v)

        elif (added_date!=""):
            strr='select * from studentdata where added_date=%s'
            mycursor.execute(strr,(added_date))
            stdata=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in stdata:
                v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert("",END,values=v)

        



    searchroot=Toplevel(master=DataEntryF)
    searchroot.geometry('450x490+125+140')
    searchroot.config(bg='#F04842')
    searchroot.grab_set()
    searchroot.iconbitmap('icon.ico')
    searchroot.resizable(False,False)
    #-----------------------------------------------------------------------
    idlabel=Label(searchroot,text="Enter ID :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    idlabel.place(x=10,y=20)
    
    Namelabel=Label(searchroot,text="Enter Name :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    Namelabel.place(x=10,y=70)
    
    moblabel=Label(searchroot,text="Enter Mobile :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    moblabel.place(x=10,y=120)
    
    emailabel=Label(searchroot,text="Enter Email :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    emailabel.place(x=10,y=170)
    
    addresslabel=Label(searchroot,text="Enter Address :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    addresslabel.place(x=10,y=220)
    
    genlabel=Label(searchroot,text="Enter Gender :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    genlabel.place(x=10,y=270)
    
    doblabel=Label(searchroot,text="Enter D.O.B. :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    doblabel.place(x=10,y=320)

    datelabel=Label(searchroot,text="Enter Date :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    datelabel.place(x=10,y=370)

    submit=Button(searchroot,text="Search",font=('Granger',19,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14,activebackground='#F3DFA2',activeforeground='#ED231D',bd=3,command=submitsearch)
    submit.place(x=110,y=420)
    #------------------------------------------------------------------------------------------------------------------------------
    idvar=StringVar()
    namevar=StringVar()
    mobvar=StringVar()
    emailvar=StringVar()
    addressvar=StringVar()
    genvar=StringVar()
    dobvar=StringVar()
    datevar=StringVar()

    identry=Entry(searchroot,bd=3,font=('sitika',15),textvariable=idvar,width=17)
    identry.place(x=245,y=20)
    
    namentry=Entry(searchroot,bd=3,font=('sitika',15),textvariable=namevar,width=17)
    namentry.place(x=245,y=70)
    
    mobentry=Entry(searchroot,bd=3,font=('sitika',15),textvariable=mobvar,width=17)
    mobentry.place(x=245,y=120)
    
    emailentry=Entry(searchroot,bd=3,font=('sitika',15),textvariable=emailvar,width=17)
    emailentry.place(x=245,y=170)
    
    addressentry=Entry(searchroot,bd=3,font=('sitika',15),textvariable=addressvar,width=17)
    addressentry.place(x=245,y=220)
    
    genentry=Entry(searchroot,bd=3,font=('sitika',15),textvariable=genvar,width=17)
    genentry.place(x=245,y=270)
    
    dobentry=Entry(searchroot,bd=3,font=('sitika',15),textvariable=dobvar,width=17)
    dobentry.place(x=245,y=320)

    dateentry=Entry(searchroot,bd=3,font=('sitika',15),textvariable=datevar,width=17)
    dateentry.place(x=245,y=370)
    
    searchroot.mainloop()

def delstd():
    select=studenttable.focus()
    content=studenttable.item(select)
    key=content['values'][0]
    strr='delete from studentdata where id=%s'
    mycursor.execute(strr,key)
    con.commit()
    messagebox.showinfo('Notification','Deleted successfully')
    strr='select* from studentdata'
    mycursor.execute(strr)
    stdata=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in stdata:
        v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert("",END,values=v)

def update():
    def submitupdate():
        id=idvar.get()
        name=namevar.get()
        mobile=mobvar.get()
        email=emailvar.get()
        address=addressvar.get()
        gender=genvar.get()
        dob=dobvar.get()
        added_date=datevar.get()
        added_time=timevar.get()

        strr='update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,added_date=%s,added_time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,added_date,added_time,id))
        con.commit()
        messagebox.showinfo('Notification','Updated successfully',parent=updateroot)
        strr='select* from studentdata'
        mycursor.execute(strr) 
        stdata=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in stdata:
            v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert("",END,values=v)
        updateroot.destroy()


    updateroot=Toplevel(master=DataEntryF)
    updateroot.geometry('450x540+125+100')
    updateroot.config(bg='#F04842')
    updateroot.grab_set()
    updateroot.iconbitmap('icon.ico')
    updateroot.resizable(False,False)
    #-----------------------------------------------------------------------
    idlabel=Label(updateroot,text="Enter ID :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    idlabel.place(x=10,y=20)
    
    Namelabel=Label(updateroot,text="Update Name :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    Namelabel.place(x=10,y=70)
    
    moblabel=Label(updateroot,text="Update Mobile :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    moblabel.place(x=10,y=120)
    
    emailabel=Label(updateroot,text="Update Email :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    emailabel.place(x=10,y=170)
    
    addresslabel=Label(updateroot,text="Update Address :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    addresslabel.place(x=10,y=220)
    
    genlabel=Label(updateroot,text="Update Gender :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    genlabel.place(x=10,y=270)
    
    doblabel=Label(updateroot,text="Update D.O.B. :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    doblabel.place(x=10,y=320)

    datelabel=Label(updateroot,text="Update Date :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    datelabel.place(x=10,y=370)

    timelabel=Label(updateroot,text="Update Time :",font=('Granger',18,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14)
    timelabel.place(x=10,y=420)

    submit=Button(updateroot,text="Update",font=('Granger',19,'bold'),bg='#E5BA38',relief=GROOVE,borderwidth=3,width=14,activebackground='#F3DFA2',activeforeground='#ED231D',bd=3,command=submitupdate)
    submit.place(x=110,y=470)
    #------------------------------------------------------------------------------------------------------------------------------
    idvar=StringVar()
    namevar=StringVar()
    mobvar=StringVar()
    emailvar=StringVar()
    addressvar=StringVar()
    genvar=StringVar()
    dobvar=StringVar()
    datevar=StringVar()
    timevar=StringVar()

    identry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=idvar,width=17)
    identry.place(x=245,y=20)
    
    namentry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=namevar,width=17)
    namentry.place(x=245,y=70)
    
    mobentry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=mobvar,width=17)
    mobentry.place(x=245,y=120)
    
    emailentry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=emailvar,width=17)
    emailentry.place(x=245,y=170)
    
    addressentry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=addressvar,width=17)
    addressentry.place(x=245,y=220)
    
    genentry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=genvar,width=17)
    genentry.place(x=245,y=270)
    
    dobentry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=dobvar,width=17)
    dobentry.place(x=245,y=320)
    
    dateentry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=datevar,width=17)
    dateentry.place(x=245,y=370)

    timeentry=Entry(updateroot,bd=3,font=('sitika',15),textvariable=timevar,width=17)
    timeentry.place(x=245,y=420)

    c=studenttable.focus()
    content=studenttable.item(c)
    pp=content['values']
    if pp!="":
        idvar.set(pp[0])
        namevar.set(pp[1])
        mobvar.set(pp[2])
        emailvar.set(pp[3])
        addressvar.set(pp[4])
        genvar.set(pp[5])
        dobvar.set(pp[6])
        datevar.set(pp[7])
        timevar.set(pp[8])

    updateroot.mainloop()

def show():
    strr='select* from studentdata'
    mycursor.execute(strr)
    stdata=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in stdata:
        v=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        studenttable.insert("",END,values=v)

def export():
    ff=filedialog.asksaveasfilename()
    g=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,added_date,added_time=[],[],[],[],[],[],[],[],[]
    for i in g:
        content=studenttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),
        address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),added_date.append(pp[7]),added_time.append(pp[8])
    
    dd=['Id','Name','mobile','email','address','gender','dob','added_date','added_time']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,added_date,added_time)),columns=dd)
    path=r'{}.csv'.format(ff)
    df.to_csv(path,index=False)
    messagebox.showinfo('Notification','Student data saved at {}'.format(path))

def exit():
    res=messagebox.askyesno('Notification','Do you want to exit?')
    if (res==True):
        root.destroy()


    
    
frontlabel=Label(DataEntryF,text='----------------WELCOME----------------',font=('Granger',22,'bold'),bg='#F3DFA2')
frontlabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryF,text="1. Add Student",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=add)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryF,text="2. Search Student",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=search)
searchbtn.pack(side=TOP,expand=True)

delbtn=Button(DataEntryF,text="3. Delete Student",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=delstd)
delbtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryF,text="4. Update student",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=update)
updatebtn.pack(side=TOP,expand=True)

showbtn=Button(DataEntryF,text="5. Show All",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=show)
showbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryF,text="6. Export Data",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=export)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryF,text="7. Exit",font=('Granger',19,'bold'),bg='#F04842',fg='#F5E6B7',relief=GROOVE,borderwidth=3,width=20,activebackground='#E5BA38',activeforeground='#F04842',bd=3,command=exit)
exitbtn.pack(side=TOP,expand=True)


###############################################################################[showdataframe]
style=ttk.Style()
style.configure('Treeview.Heading',font=('Granger',13,'bold'),foreground='#F04842')
style.configure('Treeview',font=('Granger',11),background='#E5BA38',foreground='black')
ShowDataF=Frame(root,bg='#F3DFA2',relief=GROOVE,borderwidth=5)
ShowDataF.place(x=605,y=76,height=600,width=500)
scroll_x=Scrollbar(ShowDataF ,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataF ,orient=VERTICAL)

studenttable=Treeview(ShowDataF,columns=('ID','Name','Mobile No.','Email','Address','Gender','D.O.B','Added Date','Added time'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Email',text="Email")
studenttable.heading('Address',text="Address")
studenttable.heading('Gender',text="Gender")
studenttable.heading('D.O.B',text="D.O.B")
studenttable.heading('Added Date',text="Added Date")
studenttable.heading('Added time',text="Added time")

studenttable['show']='headings'
studenttable.column('ID',width=50)
studenttable.column('Name',width=200)
studenttable.column('Mobile No.',width=150)
studenttable.column('Email',width=200)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=100)
studenttable.column('Added Date',width=100)
studenttable.column('Added time',width=100)
studenttable.pack(fill=BOTH,expand=True)

#################################################################################
count=0
text=''
ss='Welcome to Student Management System'
sliderlabel=Label(root,text=ss,bg='#F3DFA2',font=('Granger',25,'bold'),width=35,relief=RIDGE,borderwidth=4)
sliderlabel.place(x=175,y=5)

def Introslider():
    global count,text
    if (count>=len(ss)):
        count=0
        text=''
        sliderlabel.config(text=text)
    else:
        text+=ss[count]
        sliderlabel.config(text=text)
        count+=1
    sliderlabel.after(250,Introslider)
    
Introslider()  
def tick():
    time_str=time.strftime("%H:%M:%S")
    date_str=time.strftime("%d/%m/%Y")   
    clock.config(text="Date: "+date_str+'\n'+'Time: '+time_str)
    clock.after(20,tick)
    
###################################################################################
clock=Label(root,bg='#F3DFA2',font=('Granger',10,'bold'),relief=GROOVE,borderwidth=4)
clock.place(x=5,y=10)
tick()
#####################################################################################

    
    
connect=Button(root,text='Connect to Database', bg='#F3DFA2',font=('Granger',15,'bold'),relief=GROOVE,borderwidth=4,activebackground='#F04842',activeforeground='#F3DFA2',command=Connectdb)   
connect.place(x=920,y=6)
 
root.mainloop()