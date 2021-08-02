from tkinter import *
import mysql.connector

window = Tk()
#window.geometry("400x200")
window.title("")

window.minsize(width=400, height=200)
window.maxsize(width=400, height=200)

label1 = Label(window, text="Add Details to add a new teacher", font=("arial", 16, "bold")).place(x=20)


# Create a function to add data to the database
def tadd():


    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="test1")

    n = name.get()
    s = subject.get()
    t = tid.get()
    v = StringVar()
    v = "1"

    print("Connected")

    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE IF NOT EXISTS teacher (tid varchar(5) NOT NULL,name varchar(100),subject varchar(20),primary key(tid))')
    query = 'INSERT INTO teacher(tid,name,subject) VALUES (%s,%s,%s)'
    val = (t, n, s)
    mycursor.execute('CREATE TABLE IF NOT EXISTS attend(tid varchar(5)NOT NULL,val varchar(3),primary key(tid))')
    query1 = 'INSERT INTO attend(tid,val)VALUES (%s,%s)'
    val1 = (t, v)
    mycursor.execute(query, val)
    mycursor.execute(query1, val1)
    # myresult = mycursor.fetchall()
    print("Working")


# Identify String Variables
tid = StringVar()
name = StringVar()
subject = StringVar()

# Create the Input window

label2 = Label(window, text="Teacher ID:", font=("arial", 12, "bold"))
label2.place(x=30, y=50)
entry_1 = Entry(window, width=40, textvar=tid)
entry_1.place(x=130, y=50)

label2 = Label(window, text="Name:", font=("arial", 12, "bold"))
label2.place(x=30, y=80)
entry_2 = Entry(window, width=40, textvar=name)
entry_2.place(x=130, y=80)

label2 = Label(window, text="Subject:", font=("arial", 12, "bold"))
label2.place(x=30, y=110)
entry_3 = Entry(window, width=40, textvar=subject)
entry_3.place(x=130, y=110)

# Buttons
btnadd = Button(window, text="Add Teacher", width=12, command=tadd)
btnadd.place(x=110, y=140)

window.mainloop()
