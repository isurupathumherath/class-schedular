from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import Image,ImageTk    #pip install pillow

root = Tk()
root.geometry("1150x620")
root.title("Class Shedule")

imge=Image.open("D:/Class_shedular_codefest2019ccs/Background.jpg")
photo=ImageTk.PhotoImage(imge)

radio_var1=StringVar()
radio_var2=StringVar()
radio_var3=StringVar()
radio_var4=StringVar()
radio_var5=StringVar()



absent_list=[]
present_list=[]


def exitt():
    exit()

def abt():
    tkinter.messagebox.showinfo("About","CLASS SHEDULER 1.0, Is the Very Good Software For You ! Produced by _2019 Flix Software Developers, Email:flixdeveloper@gmail.com")

def hlp():
    tkinter.messagebox.showinfo("Help","Please Kind to be use the User Manual :)")




def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text= "Hey whatsup bro, i am doing something very interresting.")
    #this creates a new label to the GUI
    label.pack()
#====================================================Dynamic_labels========================================================================

def printSomething_0():
        tname=Tk()
        tname.geometry("510x330")
        tname.title("About Teachers")
        

def pre():
    winpre=Tk()
    winpre.geometry("500x300")
    winpre.title("Presented Teachers")
    imge=Image.open("D:/Class_shedular_codefest2019ccs/Background.jpg")
    photo=ImageTk.PhotoImage(imge)
    #winpre.config(background='#2D317E')
    labb=Label(winpre,bg="#2D317E",fg="white",text="P   r   e   s   e   n   t   e   d          T   e   a   c   h   e   r   s",font=("bold",12)).pack(fill=BOTH)
    label_1 = Label(winpre,fg="black",text=present_list,font=(15))
    label_1.pack()
    winpre.mainloop()
def abb():
    winabb=Tk()
    winabb.geometry("500x300")
    winabb.title("Absent Teachers")
    imge=Image.open("D:/Class_shedular_codefest2019ccs/Background.jpg")
    photo=ImageTk.PhotoImage(imge)
    #winabb.config(background='#2D317E')
    labb=Label(winabb,bg="#2D317E",fg="white",text="A   b   s   e   n   t          T   e   a   c   h   e   r   s",font=("bold",12)).pack(fill=BOTH)
    label_2 = Label(winabb, fg="Black",text=absent_list,font=(15))
    label_2.pack()
    winabb.mainloop()
    
    

#=============================================================================================================================

var=StringVar()

radio_var1=StringVar()
radio_var2=StringVar()
radio_var3=StringVar()
radio_var4=StringVar()
radio_var5=StringVar()
#Extra codes=====================================

#==========================================SYSTEM_KERNEL======================================================================    
def printt():
    #System Don't Run Without 60% of Teachers (Remeber to users)
    #Day 1 Time Table
    #Database connection
    # Remember clear the Updated_time_table (#Mark)

    #mysql connect
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="2019sliit")
    #databas connection is ok
    

    mark_attend_t1=radio_var1.get()
    mark_attend_t2=radio_var2.get()
    mark_attend_t3=radio_var3.get()
    mark_attend_t4=radio_var4.get()
    mark_attend_t5=radio_var5.get()

    #Make time tables
    class_A=[]
    mycursor = mydb.cursor()
    mycursor.execute("select * from class_A")
    myresult = mycursor.fetchall()

    for x in myresult:
        class_A.append(x[0])

    #classB list make 
    class_B=[]
    mycursor = mydb.cursor()
    mycursor.execute("select * from class_B;")
    myresult = mycursor.fetchall()

    for x in myresult:
        class_B.append(x[0])

    #classC list make
    class_C=[]
    mycursor = mydb.cursor()
    mycursor.execute("select * from class_C;")
    myresult = mycursor.fetchall()

    for x in myresult:
        class_C.append(x[0])

    dict_1={1:"TID_001",2:"TID_002",3:"TID_003",4:"TID_004",5:"TID_005"}
    new=[]

    #finding absent teachers and make list for absent teachers
    
    
    if mark_attend_t1=="no":
        absent_list.append(1)
    else:
        present_list.append(1)

    if mark_attend_t2=="no":
        absent_list.append(2)
    else:
        present_list.append(2)

    if mark_attend_t3=="no":
        absent_list.append(3)
    else:
        present_list.append(3)

    if mark_attend_t4=="no":
        absent_list.append(4)
    else:
        present_list.append(4)

    if mark_attend_t5=="no":
        absent_list.append(5)
    else:
        present_list.append(5)
    print("")
    print("Presented Teacher's list is",present_list)
    print("Absent teacher's list is",absent_list)
    print("")


    #==============================TEST=========================
    def mst_lst():
        nw1=Tk()
        nw1.title("Teachers attendence")
        nw1.geometry("250x200")
        nw1label_0=Label(window,present_list,font=("arial",12,"bold")).place(x=30,y=70)
        but_01=Button(window, text="Details", width=12, bg="brown", fg="white", command=abt).place(x=80, y=110)
    

    #---------------------------------------------------- All This facts are Well :)
    update_list=[class_A,class_B,class_C]
    mst_lst_list=[]
    pcount=0 #pcount is represent number of pereiod teachers has  
    classlist = [class_A,class_B,class_C] #time table ekak add kalama me list ekata add wenna oni
    tcount=1
    count_0=1

    for q in present_list: 
        for i in classlist:
            for x in i: #x is period in a class
                if x == q:
                    pcount= pcount+1
        print("Teacher",q,"has",pcount,"Periods to work")

        #_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_-_-_-_-
        
        
        Mylabel=Label(root,text="Teachers "+str(q) +" has " +str(pcount)+" Periods to work",fg="white",bg="#CF2B5D").place(x=880,y=210+(30*count_0))
        count_0=count_0+1

        
        
        
        #-_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_-

        mst_lst_list.append(pcount)
        pcount=0

    print("")


  
    #----------------------------------------------------   All is well (UP) Count number of teachers Part 2 is Over :)
    #----------------------------------------------------   Compare absent teachers with classes Time table
    #---------------------New Session
    #Check off periods class by class & asking to add relief teachers
    from PIL import Image,ImageTk 
    neww_1=Tk()
    neww_1.geometry("510x330")
    neww_1.title("New Time Table")
    neww_1.config(background='#2D317E')

    labtit=Label(neww_1,text="N    E    W        S     H     E     D     U     L    E",fg="#CF2B5D",bg="#2D317E",font=("calibri",20,"bold")).pack(fill=BOTH)

    label_a=Label(neww_1,text="CLASS A_",fg="white",bg="#2D317E",font=("calibri",15,))
    label_a.place(x=37, y=40)

    label_b=Label(neww_1,text="CLASS B_",fg="white",bg="#2D317E",font=("calibri",15,))
    label_b.place(x=217, y=40)

    label_c=Label(neww_1,text="CLASS C_",fg="white",bg="#2D317E",font=("calibri",15,))
    label_c.place(x=397, y=40)
    
    colcount=0
    classcount=1

    for i in classlist:
        print("Class Shedule")
        print("*****************")
        update_list.remove(i)
        count=1
        for a in i: 
             if a in absent_list:
                 print("# The",count,"period is off")
                 for x in present_list:
                        if x == update_list[0][count-1]:
                            continue
                        else:
                            if x == update_list[1][count-1]:
                                continue
                            else:
                                i[count-1]=x
                 count+=1
             else:  
                 count+=1
        update_list.append(i)
                    
        print ("Class New Time Shedule //////// ")
        print("")
        count_0=0
        print(dict_1[i[0]])
        Mylbl_1=Label(neww_1,text=str(dict_1[i[0]]),fg="white",bg="#2D317E").place(x=40+(180*colcount),y=70+(30*count_0))
        count_0=count_0+1
        print(dict_1[i[1]])
        Mylbl_2=Label(neww_1,text=str(dict_1[i[1]]),fg="white",bg="#2D317E").place(x=40+(180*colcount),y=70+(30*count_0))
        count_0=count_0+1
        print(dict_1[i[2]])
        Mylbl_3=Label(neww_1,text=str(dict_1[i[2]]),fg="white",bg="#2D317E").place(x=40+(180*colcount),y=70+(30*count_0))
        count_0=count_0+1
        print(dict_1[i[3]])
        Mylbl_4=Label(neww_1,text=str(dict_1[i[3]]),fg="white",bg="#2D317E").place(x=40+(180*colcount),y=70+(30*count_0))
        count_0=count_0+1
        print(dict_1[i[4]])
        Mylbl_5=Label(neww_1,text=str(dict_1[i[4]]),fg="white",bg="#2D317E").place(x=40+(180*colcount),y=70+(30*count_0))
        count_0=count_0+1
        print(dict_1[i[5]])
        Mylbl_6=Label(neww_1,text=str(dict_1[i[5]]),fg="white",bg="#2D317E").place(x=40+(180*colcount),y=70+(30*count_0))
        count_0=count_0+1
        print(dict_1[i[6]])
        Mylbl_7=Label(neww_1,text=str(dict_1[i[6]]),fg="white",bg="#2D317E").place(x=40+(180*colcount),y=70+(30*count_0))
        count_0=count_0+1
        print(dict_1[i[7]])
        Mylbl_8=Label(neww_1,text=str(dict_1[i[7]]),fg="white",bg="#2D317E").place(x=40+(180*colcount),y=70+(30*count_0))
        count_0=count_0+1
        print("")
        
        colcount=colcount+1

    

    neww_1.mainloop()
lab=Label(image=photo)
lab.pack( )

#==================================================MENU_BAR==================================================================
menu=Menu(root)
root.config(menu=menu)

subm1=Menu(menu)
menu.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=exitt)

subm2=Menu(menu)
menu.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About",command=abt)

subm2=Menu(menu)
menu.add_cascade(label="Help",menu=subm2)
subm2.add_command(label="More",command=hlp)



#===================================SECOND_WINDOW(DETAILS/TIME_TABLE)===========================================================


def second_win():
    window=Tk()
    window.title("Default Time Tables")
    window.geometry("530x330")
    window.config(background='#2D317E')

    label_02=Label(window,fg="#CF2B5D",bg="#2D317E",text="T      I      M      E                 T     A      B    L      E",font=("calibri",20,"bold")).pack()
    label_03=Label(window,fg="white",bg="#2D317E",text="CLASS A_",font=("calibri",15)).place(x=40,y=40)
    label_04=Label(window,fg="white",bg="#2D317E",text="CLASS B_",font=("calibri",15)).place(x=225,y=40)
    label_05=Label(window,fg="white",bg="#2D317E",text="CLASS C_",font=("calibri",15)).place(x=400,y=40)

    #class A
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB01_MATHS").place(x=40,y=80)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB03_SCIENCE").place(x=40,y=110)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB05_TAMIL").place(x=40,y=140)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB04_SINHALA").place(x=40,y=170)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB03_SCIENCE").place(x=40,y=200)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB03_SCIENCE").place(x=40,y=230)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB02_ENGLISH").place(x=40,y=260)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB02_ENGLISH").place(x=40,y=290)
    #CLASS B
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB05_TAMIL").place(x=225,y=80)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB05_TAMIL").place(x=225,y=110)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB02_ENGLISH").place(x=225,y=140)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB01_MATHS").place(x=225,y=170)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB01_MATHS").place(x=225,y=200)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB04_SINHALA").place(x=225,y=230)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB03_SCIENCE").place(x=225,y=260)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB03_SCIENCE").place(x=225,y=290)
    #CLASS C
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB03_SCIENCE").place(x=400,y=80)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB02_ENGLISH").place(x=400,y=110)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB03_SCIENCE").place(x=400,y=140)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB03_SCIENCE").place(x=400,y=170)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB05_TAMIL").place(x=400,y=200)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB05_TAMIL").place(x=400,y=230)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB01_MATHS").place(x=400,y=260)
    ap1=Label(window,fg="white",bg="#2D317E",text="SUB01_MATHS").place(x=400,y=290)


    

    window.mainloop()


#===========================================HEADINGS(LABELS)========================================================
label_0 = Label(root, text="CLASS SHEDULE",width=15,fg="white",bg="#2D317E",font=("calibri",40))
label_0.place(x=40, y=80)

label_1 = Label(root, text="Teacher's Name",width=20,fg="white",bg="#2D317E",font=("calibri",20))
label_1.place(x=25, y=180)
#================================================TEACHER'S_NAMES===============================================================
r1=Radiobutton(root,text="Yes",variable=radio_var1,width=6,height=1,value="yes").place(x=280,y=240)
r2=Radiobutton(root,text="No",variable=radio_var1,width=6,height=1,value="no").place(x=360,y=240)
label_2 = Label(root, text="001_Mr.Nuwan Balasooriya",width=20,height=1,font=("bold",11))
label_2.place(x=80, y=240)

r3=Radiobutton(root,text="Yes",variable=radio_var2,width=6,height=1,value="yes").place(x=280,y=300)
r4=Radiobutton(root,text="No",variable=radio_var2,width=6,height=1,value="no").place(x=360,y=300)
label_3 = Label(root,text="002_Mrs.Rashmi Thamara",width=20,height=1,font=("bold",11))
label_3.place(x=80, y=300)

r5=Radiobutton(root,text="Yes",variable=radio_var3,width=6,height=1,value="yes").place(x=280,y=360)
r6=Radiobutton(root,text="No",variable=radio_var3,width=6,height=1,value="no").place(x=360,y=360)
label_4 = Label(root, text="003_Mr.Kamal Perera",width=20,height=1,font=("bold",11))
label_4.place(x=80, y=360)

r7=Radiobutton(root,text="Yes",variable=radio_var4,width=6,height=1,value="yes").place(x=280,y=420)
r8=Radiobutton(root,text="No",variable=radio_var4,width=6,height=1,value="no").place(x=360,y=420)
label_5 = Label(root,text="004_Mrs.Dimali fernando",width=20,height=1,font=("bold",11))
label_5.place(x=80, y=420)

r9=Radiobutton(root,text="Yes",variable=radio_var5,width=6,height=1,value="yes").place(x=280,y=480)
r10=Radiobutton(root,text="No",variable=radio_var5,width=6,height=1,value="no").place(x=360,y=480)
label_6 = Label(root, text="005_Mr.Nimal Karunarathna",width=20,height=1,font=("bold",11))
label_6.place(x=80, y=480)
#===================================================ATTENDANCE_LABEL=================================================================
label_att_0 = Label(root, text="Today Attendance",width=15,fg="white",bg="#CF2B5D",font=("calibri",20))
label_att_0.place(x=585, y=180)

label_att_1 = Label(root, text="Present :",width=10,fg="white",bg="#CF2B5D",height=1,font=("bold",11))
label_att_1.place(x=580, y=235)
label_att_1 = Label(root, text="Absent  :",width=10,fg="white",bg="#CF2B5D",height=1,font=("bold",11))
label_att_1.place(x=688, y=235)
#===================================================TODAY_SHEDULE======================================================

label_att_0 = Label(root, text="Today Shedule",width=15,fg="white",bg="#CF2B5D",font=("calibri",20))
label_att_0.place(x=850, y=180)



#===========================================BUTTONS=====================================================
but_signup = Button(root, text="Submit", width=12, bg="#CF2B5D", fg="white", command=printt).place(x=80, y=550)
but_quit = Button(root, text="Quit",width=13, bg="#2D317E", fg="white", command=exitt).place(x=960,y=550)
but_login = Button(root, text="Details", width=12, bg="#CF2B5D", fg="white", command=second_win).place(x=335, y=550)
#but_test = Button(root, text="Teachers",width=12, bg="#CF2B5D", fg="white", command=printSomething_0).place(x=335, y=550)
but_pre = Button(root, text="Present",width=12, bg="#CF2B5D", fg="white", command=pre).place(x=595, y=260)
but_abb = Button(root, text="Absent",width=12, bg="#CF2B5D", fg="white", command=abb).place(x=700, y=260)


root.mainloop()
