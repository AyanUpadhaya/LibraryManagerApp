#Library management System app

#import neccessary libraries
import sqlite3
from tkinter import*
import PIL.Image
from PIL import ImageTk
from PIL.Image import *
from tkinter import messagebox as ms
from AddBook import*
from ViewBooks import*
from IssueBook import*
from ReturnBook import*
from DeleteBook import*
from OverduesBook import*
from DeleteOverdue import*


#Database
DATABASE = 'DB/library.db'

#create database
 
conn=sqlite3.connect(DATABASE)
cur=conn.cursor() 

def createTable():
	try:
		conn.execute("""CREATE TABLE books (book_name TEXT,book_code TEXT , author TEXT, subject TEXT, status TEXT);""")
		conn.execute("""CREATE TABLE issuedbooks (book_name TEXT,book_code TEXT , reg_no INT, date_issued TEXT);""")
		conn.execute("""CREATE TABLE returnedbooks (book_name TEXT,book_code TEXT , reg_no INT, date_submitted TEXT);""")
		conn.execute("""CREATE TABLE overduefines (book_name TEXT,book_code TEXT , reg_no INT, fine INT);""")
		print("DATABASE Tables Created Succssfully")
	except:
		print("Our DATABASE System is Ready to go")


createTable()
WIDTH=800
HEIGHT=540

"""--APP-INTERFACE-"""

root=Tk()
root.title("Library Manager")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(width=0,height=0)

#adding a background image

canvas1=Canvas(root,width=WIDTH,height=HEIGHT,bg='white')
canvas1.pack(expand=YES, fill=BOTH)


background_image=PIL.Image.open('images/library.jpeg')
set_width=800
set_height=545
background_image.resize((set_width,set_height),PIL.Image.ANTIALIAS)
img=ImageTk.PhotoImage(background_image)
canvas1.create_image(300,250,image=img)


#head frame
headingFrm=Frame(root,bg="#ffbb00",bd=5)
headingFrm.place(relx=0.2,rely=0.01, relwidth=0.6,relheight=0.15)
headLabel=Label(headingFrm,text="Welcome to \nLibrary Manager",bg='black',fg='white',font=('Arial',15))
headLabel.place(relx=0,rely=0,relwidth=1,relheight=1)


#adding some buttons
add_btn=Button(root,text="Add Book",bg='black',fg='white',font=('Arial',15),command=addBook)
add_btn.place(relx=0.28,rely=0.2,relwidth=0.45,relheight=0.1)

view_btn=Button(root,text="View Books",bg='black',fg='white',font=('Arial',15),command=viewBooks)
view_btn.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)

issue_btn=Button(root,text="Issue Book to Student",bg='black',fg='white',font=('Arial',15),command=issueBook)
issue_btn.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)

return_btn=Button(root,text="Return Book to Library",bg='black',fg='white',font=('Arial',15),command=returnBook)
return_btn.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)

delete_btn=Button(root,text="Delete Book Form Library",bg='black',fg='white',font=('Arial',15),command=deleteBook)
delete_btn.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)

due_btn=Button(root,text="Check Overdues",bg='black',fg='white',font=('Arial',15),command=overdues)
due_btn.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)

del_due_btn=Button(root,text="Delete Overdue",bg='black',fg='white',font=('Arial',15),command=deloverdue)
del_due_btn.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)


"""-APP-INTERFACE-"""

#exit keybinding

root.bind("<e>", lambda x: root.destroy())

root.mainloop()



