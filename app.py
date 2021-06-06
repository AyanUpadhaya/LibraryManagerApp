#Library management System

#import neccessary libraries
import sqlite3
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox as ms
from AddBook import*
from ViewBooks import*
from IssueBook import*
from ReturnBook import*
from DeleteBook import*

#credentials
DATABASE = 'DB/library.db'

#create database
 
conn=sqlite3.connect(DATABASE)
cur=conn.cursor() 

def createTable():
	try:
		conn.execute("""CREATE TABLE books (book_name TEXT,book_code TEXT , author TEXT, subject TEXT, status TEXT);""")
		conn.execute("""CREATE TABLE issuedbooks (book_name TEXT,book_code TEXT , reg_no INT, date_issued TEXT);""")
		conn.execute("""CREATE TABLE returnedbooks (book_name TEXT,book_code TEXT , reg_no INT, date_submitted TEXT);""")
		print("DATABASE Tables Created Succssfully")
	except:
		print("Our DATABASE System is Ready to go")


createTable()


"""--APP-INTERFACE-"""

root=Tk()
root.title("Library Manager")
root.geometry('600x500')
root.resizable(width=0,height=0)

#adding a background image

canvas1=Canvas(root,width=600,height=500,bg='white')
canvas1.pack(expand=YES, fill=BOTH)


background_image=Image.open('images/library.jpg')
set_width=600
set_height=500
background_image.resize((set_width,set_height),Image.ANTIALIAS)
img=ImageTk.PhotoImage(background_image)
canvas1.create_image(300,250,image=img)


#head frame
headingFrm=Frame(root,bg="#ffbb00",bd=5)
headingFrm.place(relx=0.2,rely=0.1, relwidth=0.6,relheight=0.16)
headLabel=Label(headingFrm,text="Welcome to \nLibrary Manager",bg='black',fg='white',font=('Arial',15))
headLabel.place(relx=0,rely=0,relwidth=1,relheight=1)


#adding some buttons
add_btn=Button(root,text="Add Book",bg='black',fg='white',font=('Arial',15),command=addBook)
add_btn.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)

view_btn=Button(root,text="View Books",bg='black',fg='white',font=('Arial',15),command=viewBooks)
view_btn.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)

issue_btn=Button(root,text="Issue Book to Student",bg='black',fg='white',font=('Arial',15),command=issueBook)
issue_btn.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)

return_btn=Button(root,text="Return Book to Library",bg='black',fg='white',font=('Arial',15),command=returnBook)
return_btn.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)

delete_btn=Button(root,text="Delete Book Form Library",bg='black',fg='white',font=('Arial',15),command=deleteBook)
delete_btn.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)


"""-APP-INTERFACE-"""


root.mainloop()



