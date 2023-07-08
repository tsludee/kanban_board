from tkinter import *
import sqlite3

root = Tk()
root.title('Kanban Board')
root.iconbitmap('bookmarkicon.ico')
root.geometry('600x400')
# create/connect to a database
conn = sqlite3.connect('workflow.db')

#create cursor
c= conn.cursor()

#create table
c.execute(""" CREATE TABLE workflow (
          to_do text,
          in_progress text,
          help text,
          review text,
          questions text,
          complete text
          )""")

#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()