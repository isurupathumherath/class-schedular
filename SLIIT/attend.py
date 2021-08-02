from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="2019sliit")
mycursor = mydb.cursor()

tdi = []

mycursor.execute("SELECT tid FROM attend")
myresult = mycursor.fetchall()

for x in myresult:
    tdi.append(x[0])
print(tdi)
y = len(tdi)
print(y)
count=0
while count<y:
    id=StringVar()
    id=tdi[count]
    print(id)
    mycursor.execute('UPDATE attend SET val="0" WHERE tid=' + id)
    count=count+1


tid = StringVar()
teacherid = StringVar()


def process():
    print("Working")


def attend():
    teacherid = tid.get()


    # mycursor.execute('UPDATE attend SET value="No" WHERE tid = ',+td)
    mycursor.execute('UPDATE attend SET val="1" WHERE tid=' + teacherid)

    print("Done")


# ===========================================HEADINGS(LABELS)=======================================
label_0 = Label(root, text="Input Teacher ID", width=15, fg="white", bg="#2D317E", font=("calibri", 40))
label_0.place(x=10, y=30)

label_1 = Label(root, text="Please Enter your Teacher ID", width=30, font=("calibri", 20))
label_1.place(x=10, y=130)

# ================================================LABELS==========================================
label2 = Label(root, text="Teacher ID:", font=("arial", 12, "bold"))
label2.place(x=30, y=200)
entry_1 = Entry(root, width=40, textvar=tid)
entry_1.place(x=130, y=200)

# ===========================================BUTTONS==============================================
but_signup = Button(root, text="Submit", width=12, bg="#BB2C60", fg="white", command=attend).place(x=150, y=230)
but_signup = Button(root, text="Process>>", width=12, bg="#BB2C60", fg="white", command=process).place(x=250, y=230)

root.mainloop()
