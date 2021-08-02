from tkinter import *

window = Tk()
window.geometry("400x450")
window.title("")

label1 = Label(window, text="Add New Timetable Details", font=("arial", 16, "bold")).place(x=20)

# Identify Variables
p1 = StringVar()
p2 = StringVar()
p3 = StringVar()
p4 = StringVar()
p5 = StringVar()
p6 = StringVar()
p7 = StringVar()
p8 = StringVar()

var1 = StringVar()
var2 = StringVar()
name = StringVar()

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="2019sliit")

classid = []
period = []
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM class;")
myresult = mycursor.fetchall()

for x in myresult:
    classid.append(x[0])
classcount = len(classid)
print(classcount)
print(classid)

# ********************************************************
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# ********************************************************

x = len(classid)


# Create a function to add data to the database
def tableadd():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="2019sliit")

    vari1 = var1.get()
    vari2 = var2.get()
    pe1 = p1.get()
    pe2 = p2.get()
    pe3 = p3.get()
    pe4 = p4.get()
    pe5 = p5.get()
    pe6 = p6.get()
    pe7 = p7.get()
    pe8 = p8.get()

    name = vari1 + vari2
    print(name)

    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS timetable(tableid int NOT NULL AUTO_INCREMENT,name varchar(20) UNIQUE,p1 varchar(5),p2 varchar(5),p3 varchar(5),p4 varchar(5),p5 varchar(5),p6 varchar(5),p7 varchar(5),p8 varchar(5),primary key(tableid))')
    query = 'INSERT INTO timetable(name,p1,p2,p3,p4,p5,p6,p7,p8) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (name, pe1, pe2, pe3, pe4, pe5, pe6, pe7, pe8)
    mycursor.execute(query, val)

    # myresult = mycursor.fetchall()
    print("Working")


# Create the Input window

label2 = Label(window, text="Class:", font=("arial", 12, "bold"))
label2.place(x=30, y=50)
droplist = OptionMenu(window, var1, *classid)
var1.set("Select a Class")
droplist.config(width=34)
droplist.place(x=110, y=50)

label3 = Label(window, text="Day:", font=("arial", 12, "bold"))
label3.place(x=30, y=80)
droplist = OptionMenu(window, var2, *day)
var2.set("Select a Day")
droplist.config(width=34)
droplist.place(x=110, y=80)

label2 = Label(window, text="Period 1:", font=("arial", 12, "bold"))
label2.place(x=30, y=110)
entry_1 = Entry(window, width=40, textvar=p1)
entry_1.place(x=110, y=110)

label2 = Label(window, text="Period 2:", font=("arial", 12, "bold"))
label2.place(x=30, y=140)
entry_1 = Entry(window, width=40, textvar=p2)
entry_1.place(x=110, y=140)

label2 = Label(window, text="Period 3:", font=("arial", 12, "bold"))
label2.place(x=30, y=170)
entry_1 = Entry(window, width=40, textvar=p3)
entry_1.place(x=110, y=170)

label2 = Label(window, text="Period 4:", font=("arial", 12, "bold"))
label2.place(x=30, y=200)
entry_1 = Entry(window, width=40, textvar=p4)
entry_1.place(x=110, y=200)

label2 = Label(window, text="Period 5:", font=("arial", 12, "bold"))
label2.place(x=30, y=230)
entry_1 = Entry(window, width=40, textvar=p5)
entry_1.place(x=110, y=230)

label2 = Label(window, text="Period 6:", font=("arial", 12, "bold"))
label2.place(x=30, y=260)
entry_1 = Entry(window, width=40, textvar=p6)
entry_1.place(x=110, y=260)

label2 = Label(window, text="Period 7:", font=("arial", 12, "bold"))
label2.place(x=30, y=290)
entry_1 = Entry(window, width=40, textvar=p7)
entry_1.place(x=110, y=290)

label2 = Label(window, text="Period 8:", font=("arial", 12, "bold"))
label2.place(x=30, y=320)
entry_1 = Entry(window, width=40, textvar=p8)
entry_1.place(x=110, y=320)

# Buttons
btnadd = Button(window, text="Add Teacher", width=12, command=tableadd)
btnadd.place(x=110, y=350)

window.mainloop()
