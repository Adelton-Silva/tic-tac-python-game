import tkinter
from tkinter import *
from tkinter import ttk


#----------------colors -----------------------------

co0 = "#FFFFFF" # White
co1 = "#333333" #dark black
co2 = "#fcc058" #orange
co3 = "#38576b" #value
co4 = "#3297a8" #blue
co5 = "#fff873" #yellow
co6 = "#fcc058" #orange
co7 = "#e85151" #red
co8 = co4 # + green
co10 = "#fcfbf7"
back = "#3b3b3b" # black


# create main window
window = Tk()
window.title('')
window.geometry('260x370')
window.configure(bg=back)


#----------------Divide window in 2 frame ----------------

frame_up = Frame(window, width=240, height=100, bg=co1, relief="raised")
frame_up.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_down = Frame(window, width=240, height=000, bg=back, relief="flat")
frame_down.grid(row=1, column=0, sticky=NW)

#----------------Config frame up --------------------------
app_x = Label(frame_up, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_up, text='Player one', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_points= Label(frame_up, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_points.place(x=80, y=20)

app_split = Label(frame_up, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_split.place(x=110, y=20)

app_o = Label(frame_up, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_up, text='Player two', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_o_points= Label(frame_up, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_o_points.place(x=130, y=20)

window.mainloop()