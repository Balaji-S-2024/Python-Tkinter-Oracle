from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle

#db = Database("Employee.db")
root = Tk()
root.title("Enterprise Application.")
root.geometry("1920x1080+0+0")
root.config(bg="#535c68")
root.state("zoomed")

#textbox for salesman table

cid = StringVar()
cname = StringVar()
ccity = StringVar()
cgrade = StringVar()

# Entries Frame Table 1 Salesman
eframe = Frame(root, bg="#535c68")
eframe.pack(side=TOP, fill=X)
title = Label(eframe, text="Enterprise Application.", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")


#widgets
lblstablename = Label(eframe, text="Customer Table", font=("Calibri", 16), bg="#535c68", fg="white")
lblstablename.grid(row=0, column=2, padx=10, pady=10, sticky="w")


lblcid= Label(eframe, text="Customer Id", font=("Calibri", 16), bg="#535c68", fg="white")
lblcid.grid(row=1 , column=0, padx=10, pady=10, sticky="w")
txtcid= Entry(eframe, textvariable=cid, font=("Calibri", 16), width=30)
txtcid.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblcname = Label(eframe, text="Customer Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblcname.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtcname = Entry(eframe, textvariable=cname, font=("Calibri", 16), width=30)
txtcname.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblccity = Label(eframe, text="Customer City", font=("Calibri", 16), bg="#535c68", fg="white")
lblccity.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtccity = Entry(eframe, textvariable=ccity, font=("Calibri", 16), width=30)
txtccity.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblcgrade = Label(eframe, text="Grade", font=("Calibri", 16), bg="#535c68", fg="white")
lblcgrade.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtcgrade = Entry(eframe, textvariable=cgrade, font=("Calibri", 16), width=30)
txtcgrade.grid(row=2, column=1, padx=10, pady=10, sticky="w")


def insert():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    csid=int(txtcid.get())
    csname=txtcname.get()
    cscity=txtccity.get()
    csgrade=int(txtcgrade.get())
    icsid=int(csid)
    icsgrade=int(csgrade)
    datai=[[icsid,csname,cscity,csgrade]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('insert into customers25 values(:1,:2,:3,:4)',datai)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        messagebox.showinfo("Inserted Dialogbox", "INSERTED SUCCESSFULLY!")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
    tab()
def update():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    csid=int(txtcid.get())
    csname=txtcname.get()
    cscity=txtccity.get()
    csgrade=int(txtcgrade.get())
    icsid=int(csid)
    icsgrade=int(csgrade)
    datau=[[csname,cscity,icsgrade,icsid]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('update customers25 set customer_name=:1,city=:2,grade=:3 where customer_id=:4',datau)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        messagebox.showinfo("Updated Dialogbox", "UPDATED SUCCESSFULLY!")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
    tab()

    
def delete():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    csid=int(txtcid.get())
    icsid=int(csid)
    datau=[[icsid]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('delete from customers25 where customer_id=:1',datau)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        messagebox.showinfo("Deleted Dialogbox", "DELETED SUCCESSFULLY!")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
    tab()
    
#insert rows in tables
def tab():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            sql="select * from customers25"
            cur.execute(sql)
            rows=cur.fetchall()
            tv.delete(*tv.get_children())
            for ro in rows:
                tv.insert("",END,values=ro)
    except cx_Oracle.DatabaseError as er:
        print('IN TAB There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        print("Table Created in GUI")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

def change():
    import order3
    print('changed')


#button for crud
btnframe1 = Frame(eframe, bg="#535c68")
btnframe1.grid(row=1, column=4, padx=10, pady=10, sticky="w")
insbtn = Button(btnframe1, command=insert, text="Insert", width=8, font=("Calibri", 16, "bold"), fg="white",
                bg="#535c68", bd=2).grid(row=1, column=5, padx=100, pady=10, sticky="w")

btnframe2 = Frame(eframe, bg="#535c68")
btnframe2.grid(row=2, column=4, padx=10, pady=10, sticky="w")
insbtn = Button(btnframe1, command=update, text="Update", width=8, font=("Calibri", 16, "bold"), fg="white",
                bg="#535c68", bd=2).grid(row=2, column=5, padx=100, pady=10, sticky="w")

btnframe3 = Frame(eframe, bg="#535c68")
btnframe3.grid(row=3, column=4, padx=10, pady=10, sticky="w")
insbtn = Button(btnframe1, command=delete, text="Delete", width=8, font=("Calibri", 16, "bold"), fg="white",
                bg="#535c68", bd=2).grid(row=3, column=5, padx=100, pady=10, sticky="w")

btnframe4 = Frame(eframe, bg="#535c68")
btnframe4.grid(row=4, column=4, padx=10, pady=10, sticky="w")
insbtn1 = Button(btnframe4, command=change, text="ORDER", width=8, font=("Calibri", 16, "bold"), fg="white",
                bg="#535c68", bd=2).grid(row=4, column=5, padx=100, pady=10, sticky="w")

#Display tables
tframe=Frame(root)
tframe.place(x=100,y=400,width=1000,height=250)
#style for table
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',14),rowheight=40)
#table show
tv=ttk.Treeview(tframe,columns=(1,2,3,4),style="mystyle.Treeview")
tv.heading("1",text="CUSTOMER ID")
tv.heading("2",text="CUSTOMER NAME")
tv.heading("3",text="CUSTOMER CITY")
tv.heading("4",text="CUSTOMER GRADE")
tv['show']='headings'
tv.pack(fill=X)


tab()
root.mainloop()
