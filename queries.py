from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
#from salesman1 import tab
root = Tk()
root.title("Enterprise Application.")
root.geometry("1920x1080+0+0")
#root.config(bg="#535c68")
root.state("zoomed")

#display1
tframe=Frame(root)
tframe.place(x=10,y=100,width=200,height=125)
#style for table
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',14),rowheight=40)
#table show
tv=ttk.Treeview(tframe,columns=(1),style="mystyle.Treeview")
tv.heading("1",text="COUNT(CUSTOMER_ID)")
tv['show']='headings'
tv.pack(fill=X)

label1 = Label(root, text = "1. Count of customers with grades above Tirupur's average",font=("Calibri", 18))
label1.place(x = 10,y = 10)

label2 = Label(root, text = "2. Find the name and numbers of all salesmen who had more than one customer",font=("Calibri", 18))
label2.place(x = 10,y = 200)

def get1():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.execute("select count(customer_id) from customers where grade>(select avg(grade) from customers where city='Tirupur')")
            result=cur.fetchall() 
            print(result)
            tv.delete(*tv.get_children())
            for ro in result :
                tv.insert("",END,values=ro)
#select count(customer_id) from customers where grade>(select avg(grade) from customers where city='Tirupur');
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        print('Get1 Executed')
        print("Printed Tirupur geade avg")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

def get2():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.execute("select salesman_id,name from salesman a where 1<(select count(*) from customer where salesman_id=a.salesman_id)")
            result=cur.fetchall() 
            print(result)
            tv1.delete(*tv1.get_children())
            for ro in result :
                print(ro)
                tv1.insert("",END,values=ro)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        print('Get2 Executed')
        print("Printed Salesman id and salesman name")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

#display2
tframe1=Frame(root)
tframe1.place(x=10,y=280,width=400,height=125)
#style for table
style1=ttk.Style()
style1.configure("mystyle.Treeview",font=('Calibri',14),rowheight=40)
#table show
tv1=ttk.Treeview(tframe1,columns=(1,2),style="mystyle.Treeview")
tv1.heading("1",text="SALESMAN ID)")
tv1.heading("2",text="SALESMAN NAME")
tv1['show']='headings'
tv1.pack(fill=X)

label3 = Label(root, text = "3. List all the salesman and indicate those who have and don’t have customers in their cities",font=("Calibri", 18))
label3.place(x = 10,y = 400)

def get3():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.execute("select salesman.salesman_id,name,customer_name,commision from salesman,customers where salesman.city=customers.city union (select salesman_id,name,'NO SAME CITY',commision from salesman where not city=any(select city from customers)) order by 2 desc")
            result=cur.fetchall() 
            print(result)
            tv2.delete(*tv2.get_children())
            for ro in result :
                print(ro)
                tv2.insert("",END,values=ro)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        print('Get2 Executed')
        print("Printed Salesman id and salesman name")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

#display3
tframe2=Frame(root)
tframe2.place(x=10,y=500,width=800,height=125)
#style for table
style2=ttk.Style()
style2.configure("mystyle.Treeview",font=('Calibri',14),rowheight=40)
#table show
tv2=ttk.Treeview(tframe2,columns=(1,2,3,4),style="mystyle.Treeview")
tv2.heading("1",text="SALESMAN ID)")
tv2.heading("2",text="SALESMAN NAME")
tv2.heading("3",text="CUSTOMER NAME)")
tv2.heading("4",text="COMMISION")
tv2['show']='headings'
tv2.pack(fill=X)

label4 = Label(root, text = " 4. Create a view that finds the salesman who has the customer with the highest order of a day",font=("Calibri", 18))
label4.place(x = 590,y = 10)

def get4():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.execute("SELECT * FROM HighSalesmanView11")
            print('below query')
            result=cur.fetchall() 
            print(result)
            tv3.delete(*tv3.get_children())
            for ro in result :
                print(ro)
                tv3.insert("",END,values=ro)
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        print('Get2 Executed')
        print("Printed Salesman id and salesman name")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

#display4
tframe3=Frame(root)
tframe3.place(x=400,y=80,width=800,height=125)
#style for table
style3=ttk.Style()
style3.configure("mystyle.Treeview",font=('Calibri',14),rowheight=40)
#table show
tv3=ttk.Treeview(tframe3,columns=(1,2,3),style="mystyle.Treeview")
tv3.heading("1",text="ORDER DATE)")
tv3.heading("2",text="SALESMAN ID")
tv3.heading("3",text="SALESMAN NAME)")
tv3['show']='headings'
tv3.pack(fill=X)

label5 = Label(root, text = " 5. Delete salesman who has id 1000",font=("Calibri", 18))
label5.place(x = 800,y = 300)

def get5():
    con = cx_Oracle.connect('system/balaji@localhost:1521/xe')
    try:
        if con:
            print(con.version)
            cur = con.cursor()
            cur.execute('delete from salesman25 where salesman_id=1000')
            cur.execute('delete from orderr25 where salesman_id=1000')
            messagebox.showinfo("Deleted Dialogbox", "DELETED SUCCESSFULLY!")
    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)
    except Exception as er:
            print(er)
    else:
        # To commit the transaction manually
        con.commit()
        print('Get5 Executed')
        print("Deleted 5")
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
    print()
    

# #display5
# tframe4=Frame(root)
# tframe4.place(x=400,y=80,width=800,height=125)
# #style for table
# style4=ttk.Style()
# style4.configure("mystyle.Treeview",font=('Calibri',14),rowheight=40)
# #table show
# tv4=ttk.Treeview(tframe4,columns=(1,2,3),style="mystyle.Treeview")
# tv4.heading("2",text="SALESMAN ID")
# tv4.heading("1",text="ORDER DATE)")
# tv4.heading("3",text="SALESMAN NAME)")
# tv4['show']='headings'
# tv4.pack(fill=X)


insbtn = Button(root, command=get1, text="GET1", width=8, font=("Calibri", 16, "bold"), fg="white",bg="#535c68", bd=2)
insbtn.place(x=10,y=50)

insbtn1 = Button(root, command=get2, text="GET2", width=8, font=("Calibri", 16, "bold"), fg="white",bg="#535c68", bd=2)
insbtn1.place(x=10,y=230)

insbtn2 = Button(root, command=get3, text="GET3", width=8, font=("Calibri", 16, "bold"), fg="white",bg="#535c68", bd=2)
insbtn2.place(x=10,y=440)

insbtn3 = Button(root, command=get4, text="GET4", width=8, font=("Calibri", 16, "bold"), fg="white",bg="#535c68", bd=2)
insbtn3.place(x=300,y=100)

insbtn4 = Button(root, command=get5, text="DELETE", width=8, font=("Calibri", 16, "bold"), fg="white",bg="#535c68", bd=2)
insbtn4.place(x=1000,y=350)





root.mainloop()
