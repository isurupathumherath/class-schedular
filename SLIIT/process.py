from tkinter import *

import runpy
import mysql.connector

runpy.run_path('attend.py')

window = Tk()
window.geometry("500x600")
window.title("")

var1 = StringVar()

#lists
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
absent_list=[]
present_list=[]
classid = []
clzre=[]

#mysql connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="2019sliit")
mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM class;") #select names from calss table
myresult = mycursor.fetchall()

for e in myresult:
    classid.append(e[0]) #add class names in to classid list from result variable
    classcount = len(classid) #count the lenth of classcount list

# print(classcount)
# print(classid)

def process():
    mycursor.execute('SELECT tid FROM attend WHERE val="0"')  #select adsent teacher ids
    myresult2 = mycursor.fetchall() #get absent teachers data into result2 variable
    for q in myresult2:
        absent_list.append(q) #add absent teachers ids into absent list

    mycursor.execute('SELECT tid FROM attend WHERE val="1"')   #select present teacher ids
    myresult3 = mycursor.fetchall()  #get present teachers data into result3 variable
    for w in myresult3:
        present_list.append(w)  #add present teachers ids into present list
    print("absent list is", absent_list)
    print("present list is", present_list)

    #get data from inputs
    vari2 = var1.get()
    name = StringVar()
    clid = StringVar()
    x = 0

    while x < classcount:
        clid = classid[x] #Add Class IDs to clid list
        name = clid+vari2 #create the name using classid and date
        mycursor.execute('SELECT p1,p2,p3,p4,p5,p6,p7,p8 FROM timetable WHERE name=+name') #select teachers period by period
        myresult1 = mycursor.fetchall() #get results of teacher ids in to myresult1 variable
        x = x + 1
        print(name)

    for y in myresult1:
        clzre.append(y)  #add myresult1 data in to clzre list

    t = 0
    pc = 0
    f = 0
    while t < 8:
        pl = present_list[0]
        #print(pl)
        cl = clzre[0]
        #print(cl)
        if pl == cl:
            pc = pc+1
        t = t+1
    print("Teacher has", pc)



label1 = Label(window, text="Releif", font=("arial", 16, "bold")).place(x=20)

# Input Window
label3 = Label(window, text="Day:", font=("arial", 12, "bold"))
label3.place(x=30, y=40)
droplist = OptionMenu(window, var1, *day)
var1.set("Select a Day")
droplist.config(width=34)
droplist.place(x=110, y=40)

# Buttons
btnadd = Button(window, text="Process", width=12, command=process)
btnadd.place(x=110, y=350)



window.mainloop()