from tkinter import *
import sqlite3

root = Tk()
root.title('Kanban Board')
root.iconbitmap('bookmarkicon.ico')
root.geometry('600x400')

# GUI setup
"""
this is where I will layout the different columns (workflow stages) and their children cards
"""
# define columns

to_do_col = Label(root, text="To Do")
in_progress_col = Label(root, text="In Progress")
help_col = Label(root, text="Help")
review_col = Label(root, text="Review")
questions_col = Label(root, text="Questions")
complete_col = Label(root, text="Complete")

# add to screen
to_do_col.grid(row=0, column=0)
in_progress_col.grid(row=0, column=1)
help_col.grid(row=0, column=2)
review_col.grid(row=0, column=3)
questions_col.grid(row=0, column=4)
complete_col.grid(row=0, column=5)

# create/connect to a database
conn = sqlite3.connect('workflow.db')
#create cursor
c= conn.cursor()
#create table
# c.execute(""" CREATE TABLE workflow (
#           to_do text,
#           in_progress text,
#           help text,
#           review text,
#           questions text,
#           complete text
#           )""")
#commit changes
conn.commit()
#close connection
conn.close()

root.mainloop()