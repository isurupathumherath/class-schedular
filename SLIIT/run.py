from tkinter import *
import os
import runpy

runpy.run_path('attend.py')
window = Tk()
window.geometry("400x200")
window.title("")

def run():
    print("DONE")
    runpy.run_path('addteacher.py')
    #os.system('addteacher.py')
    #exec(open('addteacher.py').read())
    print("Done")


# Buttons
btnadd = Button(window, text="Add Teacher", width=12, command=run and window.destroy)
btnadd.place(x=110, y=140)

btnclose = Button(window, text="Close", width=12, command=window.destroy())
btnadd.place(x=110, y=140)
btnclose.pack()


window.mainloop()
