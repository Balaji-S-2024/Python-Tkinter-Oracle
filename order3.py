from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
#import customer

#db = Database("Employee.db")
root = Tk()
root.title("Enterprise Application.")
root.geometry("1920x1080+0+0")
root.config(bg="#535c68")
root.state("zoomed")

#textbox for salesman table

ono = StringVar()
pamt = StringVar()
odate = StringVar()
cid = StringVar()
sid = StringVar()

# Entries Frame Table 1 Salesman
eframe = Frame(root, bg="#535c68")
eframe.pack(side=TOP, fill=X)
title = Label(eframe, text="Enterprise Application.", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")


#widgets
lblotablename = Label(eframe, text="Order Table", font=("Calibri", 16), bg="#535c68", fg="white")
lblotablename.grid(row=0, column=2, padx=10, pady=10, sticky="w")


lblono= Label(eframe, text="Order No", font=("Calibri", 16), bg="#535c68", fg="white")
lblono.grid(row=1 , column=0, padx=10, pady=10, sticky="w")
txtono= Entry(eframe, textvariable=ono, font=("Calibri", 16), width=30)
txtono.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblpamt = Label(eframe, text="Purchase Amount", font=("Calibri", 16), bg="#535c68", fg="white")
lblpamt.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtpamt = Entry(eframe, textvariable=pamt, font=("Calibri", 16), width=30)
txtpamt.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblodate = Label(eframe, text="Order Date ", font=("Calibri", 16), bg="#535c68", fg="white")
lblodate.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtodate = Entry(eframe, textvariable=odate, font=("Calibri", 16), width=30)
txtodate.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblcid = Label(eframe, text="Customer Id", font=("Calibri", 16), bg="#535c68", fg="white")
lblcid.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtcid = Entry(eframe, textvariable=cid, font=("Calibri", 16), width=30)
txtcid.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblsid = Label(eframe, text="Salesman Id", font=("Calibri", 16), bg="#535c68", fg="white")
lblsid.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtsid = Entry(eframe, textvariable=sid, font=("Calibri", 16), width=30)
txtsid.grid(row=3, column=1, padx=10, pady=10, sticky="w")


def insert():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    ono=int(txtono.get())
    pamt=txtpamt.get()
    odate=txtodate.get()
    cid=int(txtcid.get())
    sid=int(txtsid.get())
    iono=int(ono)
    ipamt=int(pamt)
    icid=int(cid)
    isid=int(sid)
    datai=[[iono,ipamt,odate,isid,icid]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('insert into orderr25 values(:1,:2,:3,:4,:5)',datai)
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
    ono=int(txtono.get())
    pamt=txtpamt.get()
    odate=txtodate.get()
    cid=int(txtcid.get())
    sid=int(txtsid.get())
    iono=int(ono)
    ipamt=int(pamt)
    icid=int(cid)
    isid=int(sid)
    datai=[[pamt,odate,isid,icid,iono]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('update orderr25 set purchase_amt=:1,ord_date=:2,salesman_id=:3,customer_id=:4 where ord_no=:1',datai)
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
    ono=int(txtono.get())
    iono=int(ono)
    datau=[[iono]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('delete from orderr25 where ord_no=:1',datau)
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
            sql="select * from orderr25"
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
    import queries
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
insbtn1 = Button(btnframe4, command=change, text="QUERIES", width=8, font=("Calibri", 16, "bold"), fg="white",
                bg="#535c68", bd=2).grid(row=3, column=5, padx=100, pady=10, sticky="w")

#Display tables
tframe=Frame(root)
tframe.place(x=100,y=400,width=1000,height=250)
#style for table
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',14),rowheight=40)
#table show
tv=ttk.Treeview(tframe,columns=(1,2,3,4,5),style="mystyle.Treeview")
tv.heading("1",text="ORDER NO")
tv.heading("2",text="PURCHASE AMOUNT")
tv.heading("3",text="ORDER DATE")
tv.heading("4",text="CUSTOMER ID")
tv.heading("5",text="SALESMAN ID")
tv['show']='headings'
tv.pack(fill=X)


tab()
root.mainloop()
