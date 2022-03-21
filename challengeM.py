import os
import tkfn
from tkfn import *
from tkinter import scrolledtext
import time
global lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9, lb10,lb11, lb12, lb13, lb14, lb15, lb16,lb17,lb18, lb19,lb20
global sv1,sv2,sv3,sv4,sv5,sv6,sv7,sv8,sv9,sv10
global frm
bg = '#152030'
fg ='#ffffff'
win = Tk()
win.geometry('500x660+20+15')
win.title('The 60 Challenge')
win.config(bg=bg)
Label(win, text='Suffer Now And live The Rest Of \nYour Life As A Champion', font='times 18 bold ', bg=bg, fg='tomato').pack(padx=5, pady=15)


def winn():
    global lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9, lb10, lb11, lb12, lb13, lb14, lb15, lb16, lb17, lb18, lb19, lb20
    global sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8, sv9, sv10
    global frm
    import tkinter
    frm = Frame(win, background=bg)
    frm.pack()
    sv1 = BooleanVar()
    cb1 = Checkbutton(frm, bg=bg, variable=sv1)
    cb1.grid(row=0, column=0, pady=3)

    sv2 = BooleanVar()
    cb2 = Checkbutton(frm, bg=bg, var=sv2)
    cb2.grid(row=1, column=0, pady=3)

    sv3 = BooleanVar()
    cb3 = Checkbutton(frm, bg=bg, var=sv3)
    cb3.grid(row=2, column=0, pady=3)

    sv4 = BooleanVar()
    cb4 = Checkbutton(frm, bg=bg, var=sv4)
    cb4.grid(row=3, column=0, pady=3)

    sv5 = BooleanVar()
    cb5 = Checkbutton(frm, bg=bg, var=sv5)
    cb5.grid(row=4, column=0, pady=3)

    sv6 = BooleanVar()
    cb6 = Checkbutton(frm, bg=bg, var=sv6)
    cb6.grid(row=5, column=0, pady=3)

    sv7 = BooleanVar()
    cb7 = Checkbutton(frm, bg=bg, var=sv7)
    cb7.grid(row=6, column=0, pady=3)

    sv8 = BooleanVar()
    cb8 = Checkbutton(frm, bg=bg, var=sv8)
    cb8.grid(row=7, column=0, pady=3)

    sv9 = BooleanVar()
    cb9 = Checkbutton(frm, bg=bg, var=sv9)
    cb9.grid(row=8, column=0, pady=3)

    sv10 = BooleanVar()
    cb10 = Checkbutton(frm, bg=bg, var=sv10)
    cb10.grid(row=9, column=0, pady=3)

    lb1 = Label(frm, text='time :', bg=bg, anchor=W, fg=fg, font='courier ')
    lb1.grid(row=0, column=1, sticky=W)
    lb2 = Label(frm, text='task 1', bg=bg, anchor=W, fg=fg, font='courier ')
    lb2.grid(row=0, column=2, sticky=W)

    lb1.bind('<Button-1>', lambda f: change(lb1, 0, 1))
    lb2.bind('<Button-1>', lambda f: change(lb2, 0, 2))

    lb3 = Label(frm, text='time :', bg=bg, anchor=W, fg=fg, font='courier ')
    lb3.grid(row=1, column=1, sticky=W)
    lb4 = Label(frm, text='task 2', bg=bg, anchor=W, fg=fg, font='courier ')
    lb4.grid(row=1, column=2, sticky=W)

    lb3.bind('<Button-1>', lambda f: change(lb3, 1, 1))
    lb4.bind('<Button-1>', lambda f: change(lb4, 1, 2))

    lb5 = Label(frm, text='time :', bg=bg, fg=fg, font='courier ')
    lb5.grid(row=2, column=1, sticky=W)
    lb6 = Label(frm, text='task 3', bg=bg, fg=fg, font='courier ')
    lb6.grid(row=2, column=2, sticky=W)

    lb5.bind('<Button-1>', lambda f: change(lb5, 2, 1))
    lb6.bind('<Button-1>', lambda f: change(lb6, 2, 2))

    lb7 = Label(frm, text='time :', bg=bg, fg=fg, font='courier ')
    lb7.grid(row=3, column=1, sticky=W)
    lb8 = Label(frm, text='task 4', bg=bg, fg=fg, font='courier ')
    lb8.grid(row=3, column=2, sticky=W)

    lb7.bind('<Button-1>', lambda f: change(lb7, 3, 1))
    lb8.bind('<Button-1>', lambda f: change(lb8, 3, 2))

    lb9 = Label(frm, text='time :', bg=bg, fg=fg, font='courier ')
    lb9.grid(row=4, column=1, sticky=W)
    lb10 = Label(frm, text='task 5', bg=bg, fg=fg, font='courier ')
    lb10.grid(row=4, column=2, sticky=W)

    lb9.bind('<Button-1>', lambda f: change(lb9, 4, 1))
    lb10.bind('<Button-1>', lambda f: change(lb10, 4, 2))

    lb11 = Label(frm, text='time :', bg=bg, fg=fg, font='courier ')
    lb11.grid(row=5, column=1, sticky=W)
    lb12 = Label(frm, text='task 6', bg=bg, fg=fg, font='courier ')
    lb12.grid(row=5, column=2, sticky=W)

    lb11.bind('<Button-1>', lambda f: change(lb11, 5, 1))
    lb12.bind('<Button-1>', lambda f: change(lb12, 5, 2))

    lb13 = Label(frm, text='time :', bg=bg, fg=fg, font='courier ')
    lb13.grid(row=6, column=1, sticky=W)
    lb14 = Label(frm, text='task 7', bg=bg, fg=fg, font='courier ')
    lb14.grid(row=6, column=2, sticky=W)

    lb13.bind('<Button-1>', lambda f: change(lb13, 6, 1))
    lb14.bind('<Button-1>', lambda f: change(lb14, 6, 2))

    lb15 = Label(frm, text='time :', bg=bg, fg=fg, font='courier ')
    lb15.grid(row=7, column=1, sticky=W)
    lb16 = Label(frm, text='task 8', bg=bg, fg=fg, font='courier')
    lb16.grid(row=7, column=2, sticky=W)

    lb15.bind('<Button-1>', lambda f: change(lb15, 7, 1))
    lb16.bind('<Button-1>', lambda f: change(lb16, 7, 2))

    lb17 = Label(frm, text='time :', bg=bg, fg=fg, font='courier ')
    lb17.grid(row=8, column=1, sticky=W)
    lb18 = Label(frm, text='task 9', bg=bg, fg=fg, font='courier ')
    lb18.grid(row=8, column=2, sticky=W)

    lb17.bind('<Button-1>', lambda f: change(lb17, 8, 1))
    lb18.bind('<Button-1>', lambda f: change(lb18, 8, 2))

    lb19 = Label(frm, text='time :', bg=bg, fg=fg, font='courier ')
    lb19.grid(row=9, column=1, sticky=W)
    lb20 = Label(frm, text='task 10', bg=bg, fg=fg, font='courier ')
    lb20.grid(row=9, column=2, sticky=W)

    lb19.bind('<Button-1>', lambda f: change(lb19, 9, 1))
    lb20.bind('<Button-1>', lambda f: change(lb20, 9, 2))

    frm1 = Frame(win, bg=bg)
    frm1.pack()
    Button(frm1, text='Saving Changes', font='times ', command=save).grid(row=0, column=0, pady=10, padx=5,
                                                                          columnspan=2)
    Button(frm1, text="Show Today's Score", command=score, font='times ').grid(row=1, column=0, pady=5, padx=5)
    Button(frm1, text="Show Weekly Score", command=wscore, font='times ').grid(row=1, column=1, pady=5, padx=5)

    Button(win, text='exit', command=win.quit, font='times ').pack(pady=50, padx=5)
def wscore():
     try:
        with open('WeekScore.txt', 'r') as file:
            l = [0]
            r = file.readlines()
            for x in r:
                l.append(x[-3:-1])
            y = 1
            sum = 0
            while y < len(l):
                sum = sum + int(l[y])
                y = y + 1
            win1 = Toplevel()
            txt = scrolledtext.ScrolledText(win1)
            txt.pack()
            txt.insert(INSERT, r)
            score = 'your score till today is '+str(sum)
            txt.insert(INSERT, score)
            win1.grab_set()
     except:
         msgbox('showinfo', '', " you don't have any scores right now")
def fri():
    if time.strftime('%a') == 'Fri': return True
def save():
    global lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9, lb10, lb11, lb12, lb13, lb14, lb15, lb16, lb17, lb18, lb19, lb20
    global sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8, sv9, sv10
    global frm
    lst = [lb1['text'], lb2['text'], lb3['text'], lb4['text'], lb5['text'], lb6['text'], lb7['text'], lb8['text'], lb9['text'],
           lb10['text'], lb11['text'], lb12['text'], lb13['text'], lb14['text'], lb15['text'],lb16['text'],  lb17['text'], lb18['text'],
           lb19['text'], lb20['text']]
    j = 1
    i = 0
    with open(r'saving.txt', 'w') as sf:
        for x in range(0, 20, 2):
            line = lst[i] +'\t'+ lst[j] + '\n'
            sf.write(line)
            i = i+2
            j = j+2


def lab(lb, str, ent):
    global lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9, lb10, lb11, lb12, lb13, lb14, lb15, lb16, lb17, lb18, lb19, lb20
    global sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8, sv9, sv10
    global frm
    ent.destroy()
    lb['text'] = str
def change(label, r, c):
    global lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9, lb10, lb11, lb12, lb13, lb14, lb15, lb16, lb17, lb18, lb19, lb20
    global sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8, sv9, sv10
    global frm
    en_v = StringVar()
    en = Entry(frm, textvariable=en_v)
    if c == 1:
        en['width'] = 10
    if c == 2:
        en['width'] = 16
    en.focus()
    en.grid(row=r, column=c)
    en.bind('<Return>', lambda f: lab(label, en_v.get(), en))
def score():
    global lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9, lb10, lb11, lb12, lb13, lb14, lb15, lb16, lb17, lb18, lb19, lb20
    global sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8, sv9, sv10
    global frm
    sc = 0
    if sv1.get() == True:
        sc = sc + 1
    if  sv2.get() == True:
        sc = sc + 1
    if  sv3.get() == True:
        sc = sc + 1
    if  sv4.get() == True:
        sc = sc + 1
    if  sv5.get() == True:
        sc = sc + 1
    if  sv6.get() == True:
        sc = sc + 1
    if  sv7.get() == True:
        sc = sc + 1
    if  sv8.get() == True:
        sc = sc + 1
    if  sv9.get() == True:
        sc = sc + 1
    if  sv10.get() == True:
        sc = sc + 1
    if sv1.get() == False and sv2.get() == False and sv3.get() == False and sv4.get() == False:pass
    message = str(sc)+"\n Do you want to save this as today's score"
    msgbox('askyesno', 'score', message)
    print(tkfn.i)
    if tkfn.i == True:
        string = time.strftime('%A %d %B %Y')+' : Score : 0'+str(sc)+'\n'
        with open('WeekScore.txt', 'a+') as af:
            af.write(string)
    if tkfn.i == False:
        pass
    if fri() == True:
        wscore()




if os.path.exists('saving.txt') == False:
    winn()
    pass
if os.path.isfile('saving.txt') == True:
    msgbox('askyesno', 'INFO', 'Do You Want to Delete Your Past Schedule')
    ls = []
    if tkfn.i == False:
        with open('saving.txt', 'r+') as rf:
            r = rf.readlines()
            i = 0
            while i < len(r):
                ls.append(r[i].split('\t'))
                i = i+1
        frm = Frame(win, background=bg)
        frm.pack()
        sv1 = BooleanVar()
        cb1 = Checkbutton(frm, bg=bg, variable=sv1)
        cb1.grid(row=0, column=0, pady=3)

        sv2 = BooleanVar()
        cb2 = Checkbutton(frm, bg=bg, var=sv2)
        cb2.grid(row=1, column=0, pady=3)

        sv3 = BooleanVar()
        cb3 = Checkbutton(frm, bg=bg, var=sv3)
        cb3.grid(row=2, column=0, pady=3)

        sv4 = BooleanVar()
        cb4 = Checkbutton(frm, bg=bg, var=sv4)
        cb4.grid(row=3, column=0, pady=3)

        sv5 = BooleanVar()
        cb5 = Checkbutton(frm, bg=bg, var=sv5)
        cb5.grid(row=4, column=0, pady=3)

        sv6 = BooleanVar()
        cb6 = Checkbutton(frm, bg=bg, var=sv6)
        cb6.grid(row=5, column=0, pady=3)

        sv7 = BooleanVar()
        cb7 = Checkbutton(frm, bg=bg, var=sv7)
        cb7.grid(row=6, column=0, pady=3)

        sv8 = BooleanVar()
        cb8 = Checkbutton(frm, bg=bg, var=sv8)
        cb8.grid(row=7, column=0, pady=3)

        sv9 = BooleanVar()
        cb9 = Checkbutton(frm, bg=bg, var=sv9)
        cb9.grid(row=8, column=0, pady=3)

        sv10 = BooleanVar()
        cb10 = Checkbutton(frm, bg=bg, var=sv10)
        cb10.grid(row=9, column=0, pady=3)

        lb1 = Label(frm, text=ls[0][0], bg=bg, anchor=W, fg=fg, font='courier ')
        lb1.grid(row=0, column=1, sticky=W)
        lb2 = Label(frm, text=ls[0][1][:-1], bg=bg, anchor=W, fg=fg, font='courier ')
        lb2.grid(row=0, column=2, sticky=W)

        lb1.bind('<Button-1>', lambda f: change(lb1, 0, 1))
        lb2.bind('<Button-1>', lambda f: change(lb2, 0, 2))

        lb3 = Label(frm, text=ls[1][0], bg=bg, anchor=W, fg=fg, font='courier ')
        lb3.grid(row=1, column=1, sticky=W)
        lb4 = Label(frm, text=ls[1][1][:-1], bg=bg, anchor=W, fg=fg, font='courier ')
        lb4.grid(row=1, column=2, sticky=W)

        lb3.bind('<Button-1>', lambda f: change(lb3, 1, 1))
        lb4.bind('<Button-1>', lambda f: change(lb4, 1, 2))

        lb5 = Label(frm, text=ls[2][0], bg=bg, fg=fg, font='courier ')
        lb5.grid(row=2, column=1, sticky=W)
        lb6 = Label(frm, text=ls[2][1][:-1], bg=bg, fg=fg, font='courier ')
        lb6.grid(row=2, column=2, sticky=W)

        lb5.bind('<Button-1>', lambda f: change(lb5, 2, 1))
        lb6.bind('<Button-1>', lambda f: change(lb6, 2, 2))

        lb7 = Label(frm, text=ls[3][0], bg=bg, fg=fg, font='courier ')
        lb7.grid(row=3, column=1, sticky=W)
        lb8 = Label(frm, text=ls[3][1][:-1], bg=bg, fg=fg, font='courier ')
        lb8.grid(row=3, column=2, sticky=W)

        lb7.bind('<Button-1>', lambda f: change(lb7, 3, 1))
        lb8.bind('<Button-1>', lambda f: change(lb8, 3, 2))

        lb9 = Label(frm, text=ls[4][0], bg=bg, fg=fg, font='courier ')
        lb9.grid(row=4, column=1, sticky=W)
        lb10 = Label(frm, text=ls[4][1][:-1], bg=bg, fg=fg, font='courier ')
        lb10.grid(row=4, column=2, sticky=W)

        lb9.bind('<Button-1>', lambda f: change(lb9, 4, 1))
        lb10.bind('<Button-1>', lambda f: change(lb10, 4, 2))

        lb11 = Label(frm, text=ls[5][0], bg=bg, fg=fg, font='courier ')
        lb11.grid(row=5, column=1, sticky=W)
        lb12 = Label(frm, text=ls[5][1][:-1], bg=bg, fg=fg, font='courier ')
        lb12.grid(row=5, column=2, sticky=W)

        lb11.bind('<Button-1>', lambda f: change(lb11, 5, 1))
        lb12.bind('<Button-1>', lambda f: change(lb12, 5, 2))

        lb13 = Label(frm, text=ls[6][0], bg=bg, fg=fg, font='courier ')
        lb13.grid(row=6, column=1, sticky=W)
        lb14 = Label(frm, text=ls[6][1][:-1], bg=bg, fg=fg, font='courier ')
        lb14.grid(row=6, column=2, sticky=W)

        lb13.bind('<Button-1>', lambda f: change(lb13, 6, 1))
        lb14.bind('<Button-1>', lambda f: change(lb14, 6, 2))

        lb15 = Label(frm, text=ls[7][0], bg=bg, fg=fg, font='courier ')
        lb15.grid(row=7, column=1, sticky=W)
        lb16 = Label(frm, text=ls[7][1][:-1], bg=bg, fg=fg, font='courier')
        lb16.grid(row=7, column=2, sticky=W)

        lb15.bind('<Button-1>', lambda f: change(lb15, 7, 1))
        lb16.bind('<Button-1>', lambda f: change(lb16, 7, 2))

        lb17 = Label(frm, text=ls[8][0], bg=bg, fg=fg, font='courier ')
        lb17.grid(row=8, column=1, sticky=W)
        lb18 = Label(frm, text=ls[8][1][:-1], bg=bg, fg=fg, font='courier ')
        lb18.grid(row=8, column=2, sticky=W)

        lb17.bind('<Button-1>', lambda f: change(lb17, 8, 1))
        lb18.bind('<Button-1>', lambda f: change(lb18, 8, 2))

        lb19 = Label(frm, text=ls[9][0], bg=bg, fg=fg, font='courier ')
        lb19.grid(row=9, column=1, sticky=W)
        lb20 = Label(frm, text=ls[9][1][:-1], bg=bg, fg=fg, font='courier ')
        lb20.grid(row=9, column=2, sticky=W)

        lb19.bind('<Button-1>', lambda f: change(lb19, 9, 1))
        lb20.bind('<Button-1>', lambda f: change(lb20, 9, 2))

        frm1 = Frame(win, bg=bg)
        frm1.pack()
        Button(frm1, text='Saving Changes', font='times ', command=save).grid(row=0, column=0, pady=10, padx=5,
                                                                              columnspan=2)
        Button(frm1, text="Show Today's Score", command=score, font='times ').grid(row=1, column=0, pady=5, padx=5)
        Button(frm1, text="Show Weekly Score", command=wscore, font='times ').grid(row=1, column=1, pady=5, padx=5)

        Button(win, text='exit', command=win.quit, font='times ').pack(pady=50, padx=5)
    if tkfn.i == True:
        os.remove('saving.txt')
        winn()
win.mainloop()
if fri() == True and os.path.isfile('WeekScore.txt') == True:
    os.remove('WeekScore.txt')
