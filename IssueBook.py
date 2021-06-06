from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as ms
import sqlite3


DATABASE = 'DB/library.db'
check=[]
status='Available'
def issue():
	bookname=book_name_entry.get()
	bookcode=book_code_entry.get()
	regnumber=reg_number_entry.get()
	dateissued=date_issued_entry.get()
	
	def checkAvailable():
		response=conn.execute("SELECT status FROM books WHERE book_code=('%s')"%(bookcode))
		for data in response:
			return check.append(data[0])
			
	checkAvailable()
	if check[0]==status:
		params2=(bookname,bookcode,regnumber,dateissued)
		cur.execute("INSERT INTO issuedbooks VALUES (?,?,?,?)",params2)
		cur.execute("UPDATE books SET status='issued' WHERE book_code=('%s')"%(bookcode))
		conn.commit()
		ms.showinfo("Success",f"Book issued to {regnumber}")
		check.clear()
	else:
		ms.showinfo("Info","The Book is not Available")
		check.clear()



def issueBook():

	global book_name_entry,book_code_entry,reg_number_entry,date_issued_entry,conn, cur,root

	root=Tk()
	root.title("Library Manager - Issue Book")
	root.geometry('600x500')

	conn=sqlite3.connect(DATABASE)
	cur=conn.cursor()

	canvas1=Canvas(root)
	canvas1.config(bg="#008080")
	canvas1.pack(expand=True,fill=BOTH)

	#head frame
	headingFrm=Frame(root,bg="#ffbb00",bd=5)
	headingFrm.place(relx=0.2,rely=0.1, relwidth=0.6,relheight=0.16)
	headLabel=Label(headingFrm,text="Issue Book",bg='black',fg='white',font=('Arial',15))
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


	# Student Regestration number
	reg_number_label = Label(labelFrame,text="Regestration : ", bg='black', fg='white')
	reg_number_label.place(relx=0.05,rely=0.50, relheight=0.08)

	reg_number_entry = Entry(labelFrame)
	reg_number_entry.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

	# Date issued
	date_issued_label = Label(labelFrame,text="Date : ", bg='black', fg='white')
	date_issued_label.place(relx=0.05,rely=0.65, relheight=0.08)

	date_issued_entry = Entry(labelFrame)
	date_issued_entry.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

	#Submit Button
	SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=issue)
	SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
	quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
	quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

	root.mainloop()	