import tkinter
root=tkinter.Tk()
root.geometry('1250x700')
def start():
	global frame
	frame=tkinter.Frame(bg="#ffccf6")
	frame.pack(fill="both",expand="true",)
	l1=tkinter.Label(frame,text="Welcome To Expense Manager",bg="#330033",fg="#ffffff",relief="groove",pady=30,font=16)
	l1.pack(fill="x",expand="true",anchor="n")
	l1=tkinter.Label(frame,text="Press To Create A new Entry",bg="#330066",fg="#66FFFF",relief="groove",pady=15,font=16,padx=16)
	l1.place(relx=0.2,rely=0.2,anchor="n")
	b1=tkinter.Button(frame,text="Create Entry Sheet",bg="#9999FF",fg="#660099",relief="solid",font=11,pady=16,cursor="dot")
	b1.place(relx=0.2,rely=0.3,anchor="n")
	l1=tkinter.Label(frame,text="Press To Get Entry By Date",bg="#330066",fg="#66FFFF",relief="groove",pady=15,font=16,padx=16)
	l1.place(relx=0.4,rely=0.2,anchor="n")
	b1=tkinter.Button(frame,text="Get Entry Sheet",bg="#9999FF",fg="#660099",relief="solid",font=11,pady=16,cursor="dot")
	b1.place(relx=0.4,rely=0.3,anchor="n")
	l1=tkinter.Label(frame,text="Press To Get Entry By Month",bg="#330066",fg="#66FFFF",relief="groove",pady=15,font=16,padx=7)
	l1.place(relx=0.6,rely=0.2,anchor="n")
	b1=tkinter.Button(frame,text="Get Monthly Entry Sheet",bg="#9999FF",fg="#660099",relief="solid",font=11,pady=16,cursor="dot")
	b1.place(relx=0.6,rely=0.3,anchor="n")
	l1=tkinter.Label(frame,text="Press To Get Total Expense On Date",bg="#330066",fg="#66FFFF",relief="groove",pady=15,font=16)
	l1.place(relx=0.8,rely=0.2,anchor="n")
	b1=tkinter.Button(frame,text="Get Total Expense On Date",bg="#9999FF",fg="#660099",relief="solid",font=11,pady=16,cursor="dot")
	b1.place(relx=0.8,rely=0.3,anchor="n")
	l1=tkinter.Label(frame,text="Press To Get Total Expense In A Month",bg="#330066",fg="#66FFFF",relief="groove",pady=15,font=16)
	l1.place(relx=0.3,rely=0.5,anchor="n")
	b1=tkinter.Button(frame,text="Get Total Expense",bg="#9999FF",fg="#660099",relief="solid",font=11,pady=16,cursor="dot")
	b1.place(relx=0.3,rely=0.6,anchor="n")
	l1=tkinter.Label(frame,text="Press To Add To Existing Entry",bg="#330066",fg="#66FFFF",relief="groove",pady=15,font=16)
	l1.place(relx=0.51,rely=0.5,anchor="n")
	b1=tkinter.Button(frame,text="Add To Entry",bg="#9999FF",fg="#660099",relief="solid",font=11,pady=16,cursor="dot")
	b1.place(relx=0.51,rely=0.6,anchor="n")
	l1=tkinter.Label(frame,text="Press To Delete Existing Entry",bg="#330066",fg="#66FFFF",relief="groove",pady=15,font=16)
	l1.place(relx=0.7,rely=0.5,anchor="n")
	b1=tkinter.Button(frame,text="Delete Entry",bg="#9999FF",fg="#660099",relief="solid",font=11,pady=16,cursor="dot")
	b1.place(relx=0.7,rely=0.6,anchor="n")
	l1=tkinter.Label(frame,text="\u00a9"+" copyright 2017\t\t\t\t\t\t\t\t\t\t\t\t"+"Developed By: Abhishek Maderana",bg="#330033",fg="#FFFFFF",relief="groove",pady=30,font=16)
	l1.pack(fill="x",expand="true",anchor="s")
	root.mainloop()
start()