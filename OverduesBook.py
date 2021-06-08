from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3

DATABASE = 'DB/library.db'


def overdues():

	root=Tk()
	root.title("Library Manager - Overdue Book")
	root.geometry('1300x720')

	conn=sqlite3.connect(DATABASE)
	cur=conn.cursor() 


	v=Scrollbar(root,orient='vertical')
	v.pack(side=RIGHT, fill=Y)
	t = Text(root, width = 15, height = 100,bg='black',fg='yellow',font='bold',yscrollcommand = v.set)
	t.pack(fill=BOTH)	

	getBooks="SELECT rowid,book_name,book_code,reg_no,fine FROM overduefines ORDER BY rowid DESC;"

	try:
		cur.execute(getBooks)
		conn.commit()

		t.insert(1.0,f"BID\t\t\tBook Name\t\t\tBook Code\t\t\tRegestration Number\t\t\tFine\n" )
		t.insert(1.0,"==================================================================================================\n" )
		for i in cur:
			t.insert(0.0,f"{i[0]}\t\t\t{i[1]}\t\t\t{i[2]}\t\t\t{i[3]}\t\t\t{i[4]}\n" )
	except:
		ms.showinfo('Error',"Failed to extract data from database")

	v.config(command=t.yview)


	root.mainloop()

