from Tkinter import *

# uses the Tkinter module to allow for the easier programming of and creation of the GUI.


def hide():
    e15.grid_forget()
    e16.grid_forget()
    e17.grid_forget()
    e18.grid_forget()
    e19.grid_forget()
    e20.grid_forget()
    e21.grid_forget()
    e22.grid_remove()
    e23.grid_remove()
    e24.grid_remove()
    e25.grid_remove()
    Button(master, text='Add 3rd Section', command=newline).grid(row=32, column=0, sticky=W, pady=4)


def newline():
    Label(master, text="Category 3 of Class 1").grid(row=7)
    Label(master, text="Category Weight").grid(row=8)
    Label(master, text="Class Grades").grid(row=9)
    Label(master, text="Grade Weights").grid(row=10)
    e15.grid(row=8, column=1)
    e16.grid(row=9, column=1)
    e17.grid(row=9, column=2)
    e18.grid(row=9, column=3)
    e19.grid(row=10, column=1)
    e20.grid(row=10, column=2)
    e21.grid(row=10, column=3)
    e22.grid(row=7, column=0)
    e23.grid(row=8, column=0)
    e24.grid(row=9, column=0)
    e25.grid(row=10, column=0)


def save():
    text = e1.get() \
         + "\n" + e2.get() + " "+e3.get() + " "+e4.get() + \
         "\n" + e5.get() + " "+e6.get() + " "+e7.get() \
         + "\n" + e8.get() \
         \
         + "\n" + e9.get() + " " + e10.get() + " " + e11.get() \
         + "\n" + e12.get() + " " + e13.get() + " " + e14.get() \
        \
         + "\n" + e15.get() \
        \
         + "\n" + e16.get() + " " + e17.get() + " " + e18.get() \
         + "\n" + e19.get() + " " + e20.get() + " " + e21.get() \

    with open("GradeFile.txt", "w") as f:
        f.writelines(text)

master = Tk()
e1 = Entry(master)

e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)

e8 = Entry(master)

e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)

e12 = Entry(master)
e13 = Entry(master)
e14 = Entry(master)

e15 = Entry(master)
e16 = Entry(master)
e17 = Entry(master)
e18 = Entry(master)

e19 = Entry(master)
e20 = Entry(master)
e21 = Entry(master)

e22 = LabelFrame(master)
e23 = LabelFrame(master)
e24 = LabelFrame(master)
e25 = LabelFrame(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=1, column=2)
e4.grid(row=1, column=3)
e5.grid(row=2, column=1)
e6.grid(row=2, column=2)
e7.grid(row=2, column=3)

e8.grid(row=4, column=1)
e9.grid(row=5, column=1)
e10.grid(row=5, column=2)
e11.grid(row=5, column=3)
e12.grid(row=6, column=1)
e13.grid(row=6, column=2)
e14.grid(row=6, column=3)

e15.grid(row=8, column=1)
e16.grid(row=9, column=1)
e17.grid(row=9, column=2)
e18.grid(row=9, column=3)
e19.grid(row=10, column=1)
e20.grid(row=10, column=2)
e21.grid(row=10, column=3)
e22.grid(row=7, column=0)
e23.grid(row=8, column=0)
e24.grid(row=9, column=0)
e25.grid(row=10, column=0)


Label(master, text="Category Weight").grid(row=0)
Label(master, text="Class Grades").grid(row=1)
Label(master, text="Grade Weights").grid(row=2)
Label(master, text="Category 2 of Class 1").grid(row=3)
Label(master, text="Category Weight").grid(row=4)
Label(master, text="Class Grades").grid(row=5)
Label(master, text="Grade Weights").grid(row=6)
Label(master, text="Click save, then click run. Enter '0' for blank sections").grid(row=30)
Button(master, text='Save', command=save).grid(row=31, column=0, sticky=W, pady=4)
Button(master, text='Run', command=tkinter.quit).grid(row=31, column=1, sticky=W, pady=4)
Button(master, text='Add 3rd Section', command=newline).grid(row=32, column=0, sticky=W, pady=4)

hide()

mainloop()


execfile("Calc.py")