from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as ms
import sqlite3


DATABASE = 'DB/library.db'

def delete():
	bookid=book_id_entry.get()

	try:
		cur.execute("DELETE FROM books WHERE rowid=('%s')"%(bookid))
		conn.commit()
		ms.showinfo('Success',"Entry Deleted Successfully!")
	except:
		ms.showinfo("Error","Unable to delete the entry!")

	root.destroy()



def deleteBook():

	global book_id_entry,conn, cur,root

	root=Tk()
	root.title("Library Manager - Dekete Book")
	root.geometry('600x500')

	conn=sqlite3.connect(DATABASE)
	cur=conn.cursor()

	canvas1=Canvas(root)
	canvas1.config(bg="#d36952")
	canvas1.pack(expand=True,fill=BOTH)

	#head frame
	headingFrm=Frame(root,bg="#ffbb00",bd=5)
	headingFrm.place(relx=0.2,rely=0.1, relwidth=0.6,relheight=0.16)
	headLabel=Label(headingFrm,text="Delete Book",bg='black',fg='white',font=('Arial',15))
	headLabel.place(relx=0,rely=0,relwidth=1,relheight=1)	

	labelFrame = Frame(root,bg='black',width=580)
	labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)


	# Book code
	book_id = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
	book_id.place(relx=0.05,rely=0.2, relheight=0.08)

	book_id_entry = Entry(labelFrame)
	book_id_entry.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

	#Submit Button
	SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=delete)
	SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
	quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
	quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

	root.mainloop()
	
