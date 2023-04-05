from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
root = Tk()
root.title("Enterprise Application.")
root.geometry("1920x1080+0+0")
root.config(bg="#535c68")
root.state("zoomed")
#textbox for salesman table
sid = StringVar()
sname = StringVar()
scity = StringVar()
scommi = StringVar()
# Entries Frame Table 1 Salesman
eframe = Frame(root, bg="#535c68")
eframe.pack(side=TOP, fill=X)
title = Label(eframe, text="Enterprise Application.", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
#widgets
lblstablename = Label(eframe, text="Salesman Table", font=("Calibri", 16), bg="#535c68", fg="white")
lblstablename.grid(row=0, column=2, padx=10, pady=10, sticky="w")

lblsid = Label(eframe, text="Salesman Id", font=("Calibri", 16), bg="#535c68", fg="white")
lblsid.grid(row=1 , column=0, padx=10, pady=10, sticky="w")
txtsid = Entry(eframe, textvariable=sid, font=("Calibri", 16), width=30)
txtsid.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblsname = Label(eframe, text="Salesman Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblsname.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtsname = Entry(eframe, textvariable=sname, font=("Calibri", 16), width=30)
txtsname.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblscity = Label(eframe, text="Salesman City", font=("Calibri", 16), bg="#535c68", fg="white")
lblscity.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtscity = Entry(eframe, textvariable=scity, font=("Calibri", 16), width=30)
txtscity.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblscommi = Label(eframe, text="Commision", font=("Calibri", 16), bg="#535c68", fg="white")
lblscommi.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtscommi = Entry(eframe, textvariable=scommi, font=("Calibri", 16), width=30)
txtscommi.grid(row=2, column=1, padx=10, pady=10, sticky="w")


def insert():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    slid=int(txtsid.get())
    slname=txtsname.get()
    slcity=txtscity.get()
    slcommi=int(txtscommi.get())
    islid=int(slid)
    islcommi=int(slcommi)
    datai=[[islid,slname,slcity,islcommi]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('insert into salesman25 values(:1,:2,:3,:4)',datai)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            messagebox.showerror("ERROR", "ENTER VALID DETAILS !")
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
    slid=int(txtsid.get())
    slname=txtsname.get()
    slcity=txtscity.get()
    slcommi=int(txtscommi.get())
    islid=int(slid)
    islcommi=int(slcommi)
    datau=[[slname,slcity,islcommi,islid]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('update salesman25 set name=:1,city=:2,commision=:3 where salesman_id=:4',datau)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            messagebox.showerror("ERROR", "ENTER VALID DETAILS !")
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
    slid=int(txtsid.get())
    islid=int(slid)
    datau=[[islid]]
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.executemany('delete from salesman25 where salesman_id=:1',datau)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
        messagebox.showerror("ERROR", "ENTER VALID DETAILS !")            
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
            sql="select * from salesman25"
            cur.execute(sql)
            rows=cur.fetchall()
            tv.delete(*tv.get_children())
            for ro in rows:
                tv.insert("",END,values=ro)
    except cx_Oracle.DatabaseError as er:
        print('IN TAB There is an error in Oracle database:', er)
    except Exception as er:
            messagebox.showerror("ERROR", "ENTER VALID DETAILS !")
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
    import customer2
    print("changed")

        

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

#NEW FOR CHANGE WINDOW
btnframe4 = Frame(eframe, bg="#535c68")
btnframe4.grid(row=4, column=4, padx=10, pady=10, sticky="w")
insbtn1 = Button(btnframe4, command=change, text="CUSTOMER", width=8, font=("Calibri", 16, "bold"), fg="white",
                bg="#535c68", bd=2).grid(row=4, column=5, padx=100, pady=10, sticky="w")

#Display tables
tframe=Frame(root)
tframe.place(x=100,y=400,width=1000,height=250)
#style for table
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',14),rowheight=40)
#table show
tv=ttk.Treeview(tframe,columns=(1,2,3,4),style="mystyle.Treeview")
tv.heading("1",text="SALESMAN ID")
tv.heading("2",text="SALESMAN NAME")
tv.heading("3",text="SALESMAN CITY")
tv.heading("4",text="SALESMAN COMMISION")
tv['show']='headings'
tv.pack(fill=X)
tab()
root.mainloop()
