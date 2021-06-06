from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as ms
import sqlite3


DATABASE = 'DB/library.db'

def bookRegister():
	bookname=book_name_entry.get()
	bookcode=book_code_entry.get()
	bookauthor=book_author_entry.get()
	booksubject=book_subject_entry.get()
	default_bookstatus='Available'

	params=(bookname,bookcode,bookauthor,booksubject,default_bookstatus)

	try:
		cur.execute("INSERT INTO books VALUES(?,?,?,?,?);",params)
		conn.commit()
		ms.showinfo('Success',"Book added successfully")
	except:
		ms.showinfo("Error","Can't add data into Database")

	root.destroy()

def addBook():
	global book_name_entry ,book_code_entry, book_author_entry, book_subject_entry,book_status_entry,canvas1, conn, cur,root


	root=Tk()
	root.title("Library Manager - Add Book")
	root.geometry('600x500')

	conn=sqlite3.connect(DATABASE)
	cur=conn.cursor() 

	#Book Table
	bookTable="books" 

	canvas1=Canvas(root)
	canvas1.config(bg="#d36952")
	canvas1.pack(expand=True,fill=BOTH)

	#head frame
	headingFrm=Frame(root,bg="#ffbb00",bd=5)
	headingFrm.place(relx=0.2,rely=0.1, relwidth=0.6,relheight=0.16)
	headLabel=Label(headingFrm,text="Add Books",bg='black',fg='white',font=('Arial',15))
	headLabel.place(relx=0,rely=0,relwidth=1,relheight=1)	



	labelFrame = Frame(root,bg='black')
	labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

	# Book Name
	book_name_label = Label(labelFrame,text="Book Name : ", bg='black', fg='white')
	book_name_label.place(relx=0.05,rely=0.2, relheight=0.08)

	book_name_entry = Entry(labelFrame)
	book_name_entry.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

	# Book Code
	book_code_label = Label(labelFrame,text="Book Code : ", bg='black', fg='white')
	book_code_label.place(relx=0.05,rely=0.35, relheight=0.08)

	book_code_entry = Entry(labelFrame)
	book_code_entry.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

	# AUTHOR
	book_author_label = Label(labelFrame,text="Book Author : ", bg='black', fg='white')
	book_author_label.place(relx=0.05,rely=0.50, relheight=0.08)

	book_author_entry = Entry(labelFrame)
	book_author_entry.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

	# Book Subject
	book_subject_label = Label(labelFrame,text="Subject : ", bg='black', fg='white')
	book_subject_label.place(relx=0.05,rely=0.65, relheight=0.08)

	book_subject_entry = Entry(labelFrame)
	book_subject_entry.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

	#Submit Button
	SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
	SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
	quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
	quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

	root.mainloop()