#To-Do List Antonis Sidiras

from tkinter import *

def add():
    x1 = title_text.get()
    x2 = var_list1.get()
    x3 = var_list2.get()
    x4 = var_list3.get()
    x5 = var_list4.get()
    y = "- " + x1 + " μέχρι " + x2 + " " + x3 + "  Υπενθύμιση: " + x4 + " " + x5 + "\n"
    output_text.insert(END, y)


def remove():
    selected = output_text.curselection()
    if selected:
        output_text.delete(selected)

def remove_all():
    output_text.delete(0.0, END)

window=Tk()
window.title("To-Do List")
window.geometry("600x400+350+100")
window.configure(background="#CDBA96") #wheat3
window.resizable(width=False, height=False)

#Labels
title_label = Label(window, text="Τίτλος Εργασίας", bg="#CDBA96", fg="Black", font="Arial 12 bold")
deadline_label = Label(window, text="Προθεσμία", bg="#CDBA96", fg="Black", font="Arial 12")
reminder_label = Label(window, text="Υπενθύμιση", bg="#CDBA96", fg="Black", font="Arial 12")

#Lists
var_list1 = StringVar()
day_list = "Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"
firstlist = OptionMenu(window, var_list1, *day_list)
var_list1.set("Ημέρα")
firstlist.config(width=5, font="Arial 10")

var_list2 = StringVar()
hour_list = "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"
secondlist = OptionMenu(window, var_list2, *hour_list)
var_list2.set("Ώρα")
secondlist.config(width=5, font="Arial 10")

var_list3 = StringVar()
day_list = "Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"
thirdlist = OptionMenu(window, var_list3, *day_list)
var_list3.set("Ημέρα")
thirdlist.config(width=5, font="Arial 10")

var_list4 = StringVar()
hour_list = "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"
fourthlist = OptionMenu(window, var_list4, *hour_list)
var_list4.set("Ώρα")
fourthlist.config(width=5, font="Arial 10")

#Buttons
add_btn = Button(window, text="Προσθήκη", bg="#808069", fg="Black", font="Arial 12 bold", width=15, command=add) #warmgrey
remove_btn = Button(window, text="Αφαίρεση", bg="#808069", fg="Black", font="Arial 12 bold", width=15, command=remove)
remove_all_btn = Button(window, text="Αφαίρεση Όλων", bg="#808069", fg="Black", font="Arial 12 bold", width=15, command=remove_all)
exit_btn = Button(window, text="Έξοδος", bg="#808069", fg="Black", font="Arial 12 bold", width=52, command=window.destroy)

#Texts
title_text = Entry(window, width=55, bg="white", font="Arial 10")
output_text = Text(window, width=75, height=13, background="white", font="Arial 10 bold")

#Place_Everything
title_label.place(x=30, y=10)
title_text.place(x=170, y=10.5)
deadline_label.place(x=30, y=45.5)
firstlist.place(x=115, y=45)
secondlist.place(x=200, y=45)
reminder_label.place(x=300, y=45.5)
thirdlist.place(x=395, y=45)
fourthlist.place(x=480, y=45)
add_btn.place(x=30, y=90)
remove_btn.place(x=215, y=90)
remove_all_btn.place(x=400, y=90)
output_text.place(x=30, y=135)
exit_btn.place(x=30, y=360)

window.mainloop()
