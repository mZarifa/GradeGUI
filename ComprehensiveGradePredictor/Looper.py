def GUISetup ( ) :
    text=GUISetup
    execfile ("GUISetup.py")

from Tkinter import *
master = Tk ()

Label(master, text="Would you like to run again? Clicking yes will display the previous results and relaunch. \
Clicking no will display the results and close the program.").grid(row=0)
Button(master, text='No', command=tkinter.quit).grid(row=1, column=2, sticky=W, pady=4)
Button(master, text='Yes', command=GUISetup).grid(row=1, column=1, sticky=W, pady=4)
mainloop( )