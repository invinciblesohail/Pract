import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import messagebox
import sqlite3
import pymysql
from tkcalendar import Calendar, DateEntry
from datetime import date
import datetime


first_root = tk.Tk()
first_root.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 400
window_width = 800

screen_width = first_root.winfo_screenwidth()
screen_height = first_root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

first_root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

first_root.title("Library Automation System")

l1= Label(first_root, text="Welcome to the College Library Automation System",
width=40,font=("bold", 20), relief = RAISED, bg= "royal blue",fg = "White") # First Label
l1.pack(side = TOP, padx = 5, pady= 5)

frame1 = Frame(first_root,  bg ="Blue",relief = RAISED, bd=8, width=350, height=250)
frame1.place(x=120, y =100)
frame2 = Frame(first_root,  bg ="Blue",relief = RAISED, bd=8, width=350, height=250)
frame2.place(x=440, y =100)
frame3 = Frame(first_root,  bg ="Blue",relief = RAISED, bd=8, width=350, height=250)
frame3.place(x=280, y =280)

#*******************Admin Login*********************
admin_search_check = False
def admin_sec():
    first_root.withdraw()
    admin_login_root = tk.Tk()
    admin_login_root.geometry('400x350')

    l1= Label(admin_login_root, text="Admin Login",
    width=10,font=("bold", 20), relief = RAISED, bg= "royal blue",fg = "White") # First Label
    l1.pack(side = TOP, padx = 10, pady= 10)

    frame_admin_login = Frame(admin_login_root,  bg ="Yellow",relief = RAISED, bd=8, width=350, height=250)
    frame_admin_login.place(x=60, y =100)

    adminFrame_l1 = Label(frame_admin_login, text="User ID",font=("bold", 15),bg="Yellow" , fg = "Black")
    adminFrame_l1.grid(row=0,column=0,padx=10,pady =10, sticky = E)

    adminFrame_e1 = Entry(frame_admin_login, width = 25, borderwidth = 5)
    adminFrame_e1.grid(row=0, column=1,padx=10,pady =10) # First Entry box

    adminFrame_l2 = Label(frame_admin_login, text="Password",font=("bold", 15),bg="Yellow"  ,  fg = "Black")
    adminFrame_l2.grid(row=1,column=0,padx=10,pady =10,sticky = E)

    adminFrame_e2 = Entry(frame_admin_login, width = 25, borderwidth = 5, show="*")
    adminFrame_e2.grid(row=1,column=1,padx=10,pady =10) # Second Entry box

    #*********************Admin Funtions ********************************
    def admin_functions():
        admin_login_root.withdraw()
        admin_functions_root = tk.Tk()
        admin_functions_root.geometry('500x500')

        #admin_profile
        def admin_profile():
            if admin_search_check == True:

                admin_functions_root.withdraw()
                admin_profile_root = tk.Tk()
                admin_profile_root.title("Admin Profile")
                admin_profile_root.geometry('400x400')

                admin_title_label = Label(admin_profile_root , text = "Admin Profile",
                width=10,font=("bold",20), relief = RAISED, bg= "royal blue", fg = "white" )
                admin_title_label.pack(side = TOP, padx=5, pady=5)

                admin_profile_l1 = Label(admin_profile_root , text = "Admin ID: ",width=10,font=("bold",12) ).place(x=45, y=100)
                admin_profile_e1 = Entry(admin_profile_root, width = 25, borderwidth = 5)
                admin_profile_e1.place(x=140,y=100)

                admin_profile_l2 = Label(admin_profile_root, text = "Name: ", width =10, font=("bold",12)).place(x=50,y=140)
                admin_profile_e2 = Entry(admin_profile_root, width = 25, borderwidth=5)
                admin_profile_e2.place(x=140,y=140)

                admin_profile_l3 = Label(admin_profile_root, text = "Last Name: ",width=10,font=("bold",12)).place(x=40,y=180)
                admin_profile_e3 = Entry(admin_profile_root, width = 25, borderwidth=5)
                admin_profile_e3.place(x=140,y=180)

                admin_profile_l4 = Label(admin_profile_root, text = "Address: ",width =10,font=("bold",12)).place(x=50,y=220)
                admin_profile_e4 = Entry(admin_profile_root, width = 25, borderwidth=5)
                admin_profile_e4.place(x=140, y = 220)

                admin_profile_l5 = Label(admin_profile_root, text = "Contact: ",width=10,font=("bold",12)).place(x=40,y=260)
                admin_profile_e5 = Entry(admin_profile_root, width = 25, borderwidth=5)
                admin_profile_e5.place(x=140, y = 260)

                admin_profile_l6 = Label(admin_profile_root, text = "Designation: ",width=10,font=("bold",12)).place(x=40,y=300)
                admin_profile_e6 = Entry(admin_profile_root, width = 25, borderwidth=5)
                admin_profile_e6.place(x=140, y = 300)
                con = pymysql.connect(host = "localhost", user= "root", password="", database= "libdatabase")
                cursorObj = con.cursor()
                cursorObj.execute("select * from admin where admin_userid = %s", (user_admin))
                row = cursorObj.fetchall()
                if row:
                    for r in row:
                        admin_profile_e1.insert(0,r[0])
                        admin_profile_e2.insert(0,r[1])
                        admin_profile_e3.insert(0,r[2])
                        admin_profile_e4.insert(0,r[3])
                        admin_profile_e5.insert(0,r[4])
                        admin_profile_e6.insert(0,r[5])
                else:
                    messagebox.showinfo("Record Searched", "Record does not exist")
                con.close()

                def exit_profile():
                    admin_profile_root.destroy()
                    admin_functions_root.deiconify()

                admin_profile_btn_exit = Button(admin_profile_root, text = "Exit",
                width = 10, font = ("bold", 12), command = exit_profile)
                admin_profile_btn_exit.place(x=160, y= 340)

                def on_closing_admin_profile():
                    admin_profile_root.destroy()
                    admin_functions_root.deiconify()

                admin_profile_root.protocol("WM_DELETE_WINDOW", on_closing_admin_profile)
                admin_profile_root.mainloop()
            else:
                messagebox.showinfo("Admin not logged in", "Admin is not logged in first login")

        #######################################
        ####### ADD New Students Section
        #student_registration_wizard
        def student_registration_wizard():

            if admin_search_check == True:
                admin_functions_root.withdraw()
                root_st_reg = tk.Tk()
                root_st_reg.title("Student Registration Section")
                root_st_reg.geometry('850x400')
                global search_check
                search_check = False


                stFrame_heading = Label(root_st_reg, text = "Enter the details as follows:", width=30,font =("bold",15))
                stFrame_heading.place(x=100, y = 10)


                stFrame_l1 = Label(root_st_reg , text = "Student ID: ",width=10,font=("bold",12) ).place(x=45, y=100)
                stFrame_e1 = Entry(root_st_reg, width = 25, borderwidth = 5)
                stFrame_e1.place(x=140,y=100)

                stFrame_l2 = Label(root_st_reg, text = "Name: ", width =10, font=("bold",12)).place(x=60,y=140)
                stFrame_e2 = Entry(root_st_reg, width = 25, borderwidth=5)
                stFrame_e2.place(x=140,y=140)

                stFrame_l3 = Label(root_st_reg, text = "Last Name: ",width=10,font=("bold",12)).place(x=40,y=180)
                stFrame_e3 = Entry(root_st_reg, width = 25, borderwidth=5)
                stFrame_e3.place(x=140,y=180)

                stFrame_l4 = Label(root_st_reg, text = "User: ",width =10,font=("bold",12)).place(x=60,y=220)
                stFrame_e4 = Entry(root_st_reg, width = 25, borderwidth=5)
                stFrame_e4.place(x=140, y = 220)

                stFrame_l5 = Label(root_st_reg, text = "Password: ",width=10,font=("bold",12)).place(x=40,y=260)
                stFrame_e5 = Entry(root_st_reg, width = 25, borderwidth=5)
                stFrame_e5.place(x=140, y = 260)

                def add_Student():
                    student_id = stFrame_e1.get()
                    student_name = stFrame_e2.get()
                    student_lname = stFrame_e3.get()
                    student_user = stFrame_e4.get()
                    student_password = stFrame_e5.get()
                    if student_id == "":
                        messagebox.showinfo("Empty ID Box", "Enter Student ID")
                    elif student_name == "":
                        messagebox.showinfo("Empty Name Box", "Enter Student Name")
                    elif student_lname == "":
                        messagebox.showinfo("Empty Last Name Box", "Enter Student's Last Name")
                    elif student_user == "":
                        messagebox.showinfo("Empty user id", "Enter the user ID")
                    elif student_password == "":
                        messagebox.showinfo("Empty password", "Enter the Password")
                    else:
                        con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                        cursorObj = con.cursor()
                        cursorObj.execute("select * from students where student_id = %s", (student_id))
                        row = cursorObj.fetchall()
                        if row:
                            messagebox.showinfo("Record Exists", "User already exists with this student ID")
                        else:
                            cursorObj.execute("insert into students values(%s, %s, %s, %s, %s)",
                            (student_id, student_name, student_lname, student_user, student_password ))
                            con.commit()
                            messagebox.showinfo("Record Status", "Record added successfully")
                        con.close()

                def search_student():
                    student_id = stFrame_e1.get()
                    stFrame_e1.delete(0,END)
                    stFrame_e2.delete(0,END)
                    stFrame_e3.delete(0,END)
                    stFrame_e4.delete(0,END)
                    stFrame_e5.delete(0,END)
                    global search_check
                    search_check = False
                    if student_id == "":
                        messagebox.showinfo('No Id', 'Eneter ID in ID box to search')
                    else:
                        con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                        cursorObj = con.cursor()
                        cursorObj.execute("select * from students where student_id = %s", (student_id))
                        row = cursorObj.fetchall()
                        if row:
                            search_check = True
                            for r in row:
                                stFrame_e1.insert(0,r[0])
                                stFrame_e2.insert(0,r[1])
                                stFrame_e3.insert(0,r[2])
                                stFrame_e4.insert(0,r[3])
                                stFrame_e5.insert(0,r[4])
                            messagebox.showinfo("Record Searched","Record Searched successfully")
                        else:
                            messagebox.showinfo("Record Searched", "Record does not exist")
                        con.close()

                def update_student():
                    global search_check
                    if search_check == False:
                        messagebox.showinfo("Which Record to update", "Please first search the record")
                    else:
                        MsgBox = tk.messagebox.askquestion ('Make Sure update','Are you sure you want to update the record',icon = 'warning')
                        if MsgBox == 'yes':
                            con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                            cursorObj = con.cursor()
                            cursorObj.execute(
                            "update students set name = %s, lname = %s, user = %s, password=%s where student_id = %s",
                            (stFrame_e2.get(), stFrame_e3.get(), stFrame_e4.get(), stFrame_e5.get(), stFrame_e1.get()))
                            con.commit()
                            con.close()
                            messagebox.showinfo("Recored Status", "Record updated successfully")
                        else:
                            messagebox.showinfo("No record change", "No Record was updated")
                        search_check = False

                def delete_student():
                    global search_check
                    if search_check == False:
                        messagebox.showinfo("Which Record to delete", "Please first search the record")
                    else:
                        MsgBox = tk.messagebox.askquestion ('Make Sure update','Are you sure you want to delete the record',icon = 'warning')
                        if MsgBox == 'yes':
                            con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                            ObjCurssor = con.cursor()
                            ObjCurssor.execute("delete from students where student_id = %s", (stFrame_e1.get()))
                            messagebox.showinfo('Record Status', 'Record deleted successfully')

                            stFrame_e1.delete(0, END)
                            stFrame_e2.delete(0, END)
                            stFrame_e3.delete(0, END)
                            stFrame_e4.delete(0, END)
                            stFrame_e5.delete(0, END)

                            con.commit()
                            con.close()
                        else:
                            messagebox.showinfo("No record deleted", "No Record was deleted")
                    search_check = False

                stFrame_btn_add = Button(root_st_reg, text = "Add", width = 10, font= ("bold", 12), command= add_Student)
                stFrame_btn_add.place(x = 350, y = 250)

                stFrame_btn_search = Button(root_st_reg, text = "Search",  width = 10, font= ("bold", 12), command= search_student)
                stFrame_btn_search.place(x = 460, y = 250)

                stFrame_btn_update = Button(root_st_reg, text = "Update", width = 10, font = ("bold", 12), command = update_student)
                stFrame_btn_update.place(x=580, y= 250)

                stFrame_btn_delete = Button(root_st_reg, text = "Delete",  width = 10, font = ("bold", 12), command = delete_student)
                stFrame_btn_delete.place(x=700, y= 250)

                tree = ttk.Treeview(root_st_reg, columns = (1,2,3), height=5, show = "headings")
                tree.place(x=350, y = 100)
                tree.heading(1, text = "ID")
                tree.heading(2, text="Name")
                tree.heading(3, text="Last Name")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 150, anchor = 'center')
                tree.column(3, width = 200, anchor = 'center')

                scroll = ttk.Scrollbar(root_st_reg, orient="vertical", command=tree.yview)
                scroll.place(x=780,y=120)
                tree.configure(yscrollcommand=scroll.set)

                def show():
                    con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                    cur = con.cursor()
                    cur.execute("select * from students")
                    rows = cur.fetchall()
                    tree.delete(*tree.get_children())
                    for row in rows:
                        tree.insert("", tk.END, values=row)
                    con.close()
                def clear():
                    stFrame_e1.delete(0, END)
                    stFrame_e2.delete(0, END)
                    stFrame_e3.delete(0, END)
                    stFrame_e4.delete(0, END)
                    stFrame_e5.delete(0, END)

                def exit():
                    root_st_reg.destroy()
                    admin_functions_root.deiconify()
                stFrame_btn_exit = Button(root_st_reg, text = "Show",  width = 10, font = ("bold", 12), command = show)
                stFrame_btn_exit.place(x=380, y= 300)

                stFrame_btn_exit = Button(root_st_reg, text = "Clear",  width = 10, font = ("bold", 12), command = clear)
                stFrame_btn_exit.place(x=500, y= 300)

                stFrame_btn_exit = Button(root_st_reg, text = "Exit",  width = 10, font = ("bold", 12), command = exit)
                stFrame_btn_exit.place(x=620, y= 300)

                def on_closing_root_st():
                    root_st_reg.destroy()
                    admin_functions_root.deiconify()
                root_st_reg.protocol("WM_DELETE_WINDOW", on_closing_root_st)
                root_st_reg.mainloop()
            else:
                messagebox.showinfo("Admin not logged in", "Admin is not logged in first login")

        ################END ADD Students SECTION####
        #######################################

        #######################################
        ####### ADD BOOKS Section
        #books_registration_wizard
        def books_registration_wizard():
            if admin_search_check == True:
                admin_functions_root.withdraw()
                books_reg = tk.Tk()
                books_reg.title("Books Add Section")
                books_reg.geometry('1150x450')
                global search_check_books
                search_check_books = False


                bookFrame_heading = Label(books_reg, text = "Add Books Section", width=20,
                font= ("bold", 30), relief = RAISED, bg= "royal blue", fg = "White" )
                bookFrame_heading.pack(side = TOP, padx = 5, pady=5)

                bookFrame_l1 = Label(books_reg , text = "Book ID: ", ).place(x=70, y=110)
                bookFrame_e1 = Entry(books_reg, width = 20, borderwidth = 5)
                bookFrame_e1.place(x=140,y=110)

                bookFrame_l2 = Label(books_reg, text = "Title: ").place(x=90,y=150)
                bookFrame_e2 = Entry(books_reg, width = 20, borderwidth=5)
                bookFrame_e2.place(x=140,y=150)

                bookFrame_l3 = Label(books_reg, text = "Author: ").place(x=70,y=190)
                bookFrame_e3 = Entry(books_reg, width = 20, borderwidth=5)
                bookFrame_e3.place(x=140,y=190)

                bookFrame_l4 = Label(books_reg, text = "Publisher: ").place(x=60,y=230)
                bookFrame_e4 = Entry(books_reg, width = 20, borderwidth=5)
                bookFrame_e4.place(x=140, y = 230)

                bookFrame_l5 = Label(books_reg, text = "ISBN: ").place(x=90,y=270)
                bookFrame_e5 = Entry(books_reg, width = 20, borderwidth=5)
                bookFrame_e5.place(x=140, y = 270)

                def add_book():
                    book_id = bookFrame_e1.get()
                    book_title = bookFrame_e2.get()
                    book_author = bookFrame_e3.get()
                    book_publisher = bookFrame_e4.get()
                    book_isbn = bookFrame_e5.get()

                    if book_id == "":
                        messagebox.showinfo("Empty ID Box", "Enter Book ID")
                    elif book_title == "":
                        messagebox.showinfo("Empty Book Name Box", "Enter Title of Book")
                    elif book_author == "":
                        messagebox.showinfo("Empty Author Name", "Enter Author Name")
                    elif book_publisher == "":
                        messagebox.showinfo("Empty Publisher Name", "Enter Publisher Name")
                    elif book_isbn =="":
                        messagebox.showinfo("Empty ISBN", "Enter ISBN Number")
                    else:
                        con = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                        cursorObj = con.cursor()
                        cursorObj.execute("select * from books where book_id = %s", (book_id))
                        row = cursorObj.fetchall()
                        if row:
                            messagebox.showinfo("Book Record Exists", "The book record with ID already exists")
                        else:
                            cursorObj.execute("insert into books values(%s, %s, %s, %s, %s)",
                            (book_id, book_title, book_author, book_publisher, book_isbn))
                            con.commit()
                            messagebox.showinfo("Record Status", "Record added successfully")

                        con.close()

                def book_search():
                    book_id = bookFrame_e1.get()
                    bookFrame_e1.delete(0,END)
                    bookFrame_e2.delete(0,END)
                    bookFrame_e3.delete(0,END)
                    bookFrame_e4.delete(0,END)
                    bookFrame_e5.delete(0,END)
                    global search_check_books
                    search_check_books = False

                    if book_id == "":
                        messagebox.showinfo('No Id', 'Eneter Book ID in ID box to search')
                    else:
                        con = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                        cursorObj = con.cursor()
                        cursorObj.execute("select * from books where book_id = %s", (book_id))
                        row = cursorObj.fetchall()
                        if row:
                            for r in row:
                                bookFrame_e1.insert(0,r[0])
                                bookFrame_e2.insert(0,r[1])
                                bookFrame_e3.insert(0,r[2])
                                bookFrame_e4.insert(0,r[3])
                                bookFrame_e5.insert(0,r[4])
                            messagebox.showinfo("Record Searched","Record Searched successfully")
                            search_check_books = True
                        else:
                            messagebox.showinfo("Record Searched", "Record does not exist")
                        con.close()

                def update_book():
                    global search_check_books
                    if search_check_books == False:
                        messagebox.showinfo("Which Record to update", "Please first search the record")
                    else:
                        MsgBox = tk.messagebox.askquestion ('Make Sure update','Are you sure you want to update the record',icon = 'warning')
                        if MsgBox == 'yes':
                            con = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                            cursorObj = con.cursor()
                            cursorObj.execute(
                            "update books set title = %s, author = %s, publisher= %s, isbn = %s where book_id = %s",
                            (bookFrame_e2.get(), bookFrame_e3.get(), bookFrame_e4.get(),
                            bookFrame_e5.get(), bookFrame_e1.get()))
                            con.commit()
                            con.close()
                            messagebox.showinfo("Recored Status", "Record updated successfully")
                        else:
                            messagebox.showinfo("No record change", "No Record was updated")
                    search_check_books = False

                def delete_book():
                    global search_check_books
                    if search_check_books == False:
                        messagebox.showinfo("Which Record to delete", "Please first search the record")
                    else:
                        MsgBox = tk.messagebox.askquestion ('Make Sure update','Are you sure you want to delete the record',icon = 'warning')
                        if MsgBox == 'yes':
                            con = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                            ObjCurssor = con.cursor()
                            ObjCurssor.execute("delete from books where book_id = %s", (bookFrame_e1.get()))
                            messagebox.showinfo('Record Status', 'Record deleted successfully')

                            bookFrame_e1.delete(0, END)
                            bookFrame_e2.delete(0, END)
                            bookFrame_e3.delete(0, END)
                            bookFrame_e4.delete(0, END)
                            bookFrame_e5.delete(0, END)

                            con.commit()
                            con.close()
                        else:
                            messagebox.showinfo("No record deleted", "No Record was deleted")
                    search_check_books = False

                bookFrame_btn_add = Button(books_reg, text = "Add",  width = 10, font= ("bold", 12), command= add_book)
                bookFrame_btn_add.place(x = 380, y = 280)

                bookFrame_btn_search = Button(books_reg, text = "Search",  width = 10, font= ("bold", 12), command= book_search)
                bookFrame_btn_search.place(x = 500, y = 280)

                bookFrame_btn_update = Button(books_reg, text = "Update",  width = 10, font = ("bold", 12), command = update_book)
                bookFrame_btn_update.place(x=620, y= 280)

                bookFrame_btn_delete = Button(books_reg, text = "Delete", width = 10, font = ("bold", 12), command = delete_book)
                bookFrame_btn_delete.place(x=740, y= 280)

                tree = ttk.Treeview(books_reg, columns = (1,2,3,4,5), height=5, show = "headings")
                tree.place(x=320, y = 110)
                tree.heading(1, text = "Book ID")
                tree.heading(2, text="Title")
                tree.heading(3, text="Author")
                tree.heading(4, text="Publisher")
                tree.heading(5, text="ISBN")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 200, anchor = 'center')
                tree.column(3, width = 150, anchor = 'center')
                tree.column(4, width = 150, anchor = 'center')
                tree.column(5, width = 150, anchor = 'center')

                scroll = ttk.Scrollbar(books_reg, orient="vertical", command=tree.yview)
                scroll.place(x=1050,y=130)
                tree.configure(yscrollcommand=scroll.set)

                def show():
                    con = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                    cur = con.cursor()
                    cur.execute("select * from books")
                    rows = cur.fetchall()
                    if rows:
                        tree.delete(*tree.get_children())
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No record found", "There no records to show for books")
                    con.close()

                def clear():
                    bookFrame_e1.delete(0,END)
                    bookFrame_e2.delete(0,END)
                    bookFrame_e3.delete(0,END)
                    bookFrame_e4.delete(0,END)
                    bookFrame_e5.delete(0,END)

                def exit():
                    books_reg.destroy()
                    admin_functions_root.deiconify()

                bookFrame_btn_delete = Button(books_reg, text = "Show", width = 10, font = ("bold", 12), command = show)
                bookFrame_btn_delete.place(x=860, y= 280)

                bookFrame_btn_delete = Button(books_reg, text = "Clear", width = 10, font = ("bold", 12), command = clear)
                bookFrame_btn_delete.place(x=560, y= 340)

                bookFrame_btn_exit = Button(books_reg, text = "Exit", width = 10, font = ("bold", 12), command = exit)
                bookFrame_btn_exit.place(x=680, y= 340)

                def on_closing_issue_books():
                    books_reg.destroy()
                    admin_functions_root.deiconify()

                books_reg.protocol("WM_DELETE_WINDOW", on_closing_issue_books)
                books_reg.mainloop()
            else:
                messagebox.showinfo("Admin not logged in", "Admin is not logged in first login")

        ################END ADD BOOKS SECTION####
        #######################################

        ################END Books Issue detaisl SECTION####
        #######################################
        #admin_booksIssue_details
        def admin_booksIssue_details():
            if admin_search_check == True:

                admin_functions_root.withdraw()
                booksIssue_details_root = tk.Tk()
                booksIssue_details_root.title("Books Issued Details")
                booksIssue_details_root.geometry('1000x400')
                booksIssue_title_label = Label(booksIssue_details_root , text = "Books Issued Details",
                width=20,font=("bold",20), relief = RAISED, bg= "royal blue", fg = "white" )
                booksIssue_title_label.pack(side = TOP, padx=5, pady=5)


                frame1_issue_books = Frame(booksIssue_details_root, bd=4, relief = RIDGE, bg= "crimson")
                frame1_issue_books.place(x=310, y=90)
                combo1 = ttk.Combobox(frame1_issue_books, width = 20, height = 10, font = ("bold", 12),
                values = ["Weekly", "Monthly", "Yearly"])
                combo1.grid(row=0, column=1, padx = 5, pady = 5)
                combo1.current(0)
                scroll = ttk.Scrollbar(booksIssue_details_root, orient="vertical")
                tree = ttk.Treeview(booksIssue_details_root, columns = (1,2,3,4,5,6,7),
                height=5, show = "headings", yscrollcommand = scroll.set)
                tree.place(x=50, y = 150)
                tree.heading(1, text = "Stdudent ID")
                tree.heading(2, text = "Student Name")
                tree.heading(3, text = "Book ID")
                tree.heading(4, text = "Book Title")
                tree.heading(5, text = "Start Date")
                tree.heading(6, text = "End Date")
                tree.heading(7, text = "Status")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 150, anchor = 'center')
                tree.column(3, width = 100, anchor = 'center')
                tree.column(4, width = 200, anchor = 'center')
                tree.column(5, width = 100, anchor = 'center')
                tree.column(6, width = 100, anchor = 'center')
                tree.column(7, width = 150, anchor = 'center')
                scroll.place(x=930,y=180)
                scroll.config(command = tree.yview)

                def comboprint():
                    combo1.current()
                    today = date.today()
                    con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                    ObjCurssor = con.cursor()
                    if combo1.get() == "Weekly":
                        tree.delete(*tree.get_children())
                        date_sevendays_ago = today - datetime.timedelta(days=7)
                        ObjCurssor.execute("select * from issue_books where start_date >= %s", (date_sevendays_ago))
                        rows = ObjCurssor.fetchall()
                        if rows:
                            for row in rows:
                                tree.insert("", tk.END, values=row)
                        else:
                            messagebox.showinfo("No Weekly Records found", "No Weekly issuded or returned books found")

                    elif combo1.get() == "Monthly":
                        tree.delete(*tree.get_children())
                        date_month_ago = today- datetime.timedelta(days=30)
                        ObjCurssor.execute("select * from issue_books where start_date >= %s", (date_month_ago))
                        rows = ObjCurssor.fetchall()
                        if rows:
                            for row in rows:
                                tree.insert("", tk.END, values=row)
                        else:
                            messagebox.showinfo("No Monthly Records found", "No Monthly issuded or returned books found")
                    else:
                        tree.delete(*tree.get_children())
                        date_year_ago = today- datetime.timedelta(days=365)
                        ObjCurssor.execute("select * from issue_books where start_date >= %s", (date_year_ago))
                        rows = ObjCurssor.fetchall()
                        if rows:
                            for row in rows:
                                tree.insert("", tk.END, values=row)
                        else:
                            messagebox.showinfo("No yearly Records found", "No Yearly issuded or returned books found")

                    con.close()

                IssueBooks_btn1 = Button(frame1_issue_books, text = "Show",
                width = 15,font = ("bold", 12), command= comboprint)
                IssueBooks_btn1.grid(row=0, column=0, padx = 5, pady =5)

                def showall():
                    con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                    ObjCurssor = con.cursor()
                    ObjCurssor.execute("select * from issue_books")
                    rows = ObjCurssor.fetchall()
                    if rows:
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No Records found", "No issuded or returned books found")


                frame2_issue_books = Frame(booksIssue_details_root, bd=4, relief = RIDGE, bg= "crimson")
                frame2_issue_books.place(x=330, y=320)

                IssueBooks_btn2 = Button(frame2_issue_books, text = "Show All",
                width = 15, font = ("bold", 12), command = showall)
                IssueBooks_btn2.grid(row=0, column=0, padx=5, pady=5)

                def issue_books_exit():
                    booksIssue_details_root.destroy()
                    admin_functions_root.deiconify()
                IssueBooks_btn_exit = Button(frame2_issue_books, text = "Exit",
                width = 15,font = ("bold", 12), command= issue_books_exit)
                IssueBooks_btn_exit.grid(row=0,column=1,padx = 5, pady=5)

                def Onclosing_booksIssued_details():
                    booksIssue_details_root.destroy()
                    admin_functions_root.deiconify()

                booksIssue_details_root.protocol("WM_DELETE_WINDOW", Onclosing_booksIssued_details)
                booksIssue_details_root.mainloop()
            else:
                messagebox.showinfo("Admin not logged in", "Admin is not logged in first login")

        def reports():
            admin_functions_root.withdraw()
            reports_root = tk.Tk()
            reports_root.geometry('350x460')

            def available_books():
                reports_root.withdraw()
                available_books_root = tk.Tk()
                available_books_root.geometry('700x380')

                frame_allbooks = Frame(available_books_root,  bg ="royal blue",relief = RAISED, bd=8, width=350, height=200)
                frame_allbooks.place(x=40, y =20)
                #frame_exit_allbooks = Frame(available_books_root,
                #bg ="royal blue",relief = RAISED, bd=8, width=350, height=200)
                #frame_allbooks.place(x=100, y =360)

                Label_allbooks_title = Label(frame_allbooks, text = "Available Books",
                font=("bold", 18), bg = "royal blue", fg="Black").grid(row=1,column=1, padx = 10, pady = 10)

                #Label_exit_allbooks_title = Label(frame_exit_allbooks, text = "Available Books",
                #font=("bold", 18), bg = "royal blue", fg="Black").grid(row=0,column=0, padx = 10, pady = 10)

                tree = ttk.Treeview(frame_allbooks, columns = (1,2,3,4,5), height=5, show = "headings")
                tree.grid(row=2, column = 1, padx = 5, pady = 10, sticky=E)
                tree.heading(1, text = "Book ID")
                tree.heading(2, text="Title")
                tree.heading(3, text="Author")
                tree.heading(4, text = "Publisher")
                tree.heading(5, text = "ISBN")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 200, anchor = 'center')
                tree.column(3, width = 100, anchor = 'center')
                tree.column(4, width = 100, anchor = 'center')
                tree.column(5, width = 100, anchor = 'center')

                scroll1 = ttk.Scrollbar(frame_allbooks, orient="vertical", command=tree.yview)
                scroll1.grid(row=2, column = 2,  sticky=W)
                tree.configure(yscrollcommand=scroll1.set)

                conn = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                cur = conn.cursor()
                cur.execute("select * from books")
                rows = cur.fetchall()
                for row in rows:
                    tree.insert("", tk.END, values=row)
                conn.close()
                def exit_allbooks():
                    available_books_root.destroy()
                    reports_root.deiconify()
                admin_btn1 = Button(frame_allbooks, text= "Exit", bg = 'White', width = 15, font = ("bold",15),
                command = exit_allbooks)
                admin_btn1.grid(row=3, column=1, padx =10, pady =10, sticky=E)
                def Onclosing_available_books():
                    available_books_root.destroy()
                    reports_root.deiconify()

                available_books_root.protocol("WM_DELETE_WINDOW", Onclosing_available_books)
                available_books_root.mainloop()

            adminFrame_sec = Frame(reports_root,  bg ="Cyan",relief = RAISED, bd=8, width=200, height=200)
            adminFrame_sec.place(x=60, y =20)

            reporstExitFrame = Frame(reports_root, bg = "Cyan", relief = RAISED, bd = 8, width =100, height = 100)
            reporstExitFrame.place(x =60, y=350)

            def daily_reports():

                reports_root.withdraw()
                daily_reports_root = tk.Tk()
                daily_reports_root.geometry('1000x400')
                daily_reports_root.title("Books Issued Today")

                booksIssue_daily_title_label = Label(daily_reports_root , text = "Books Issued Today",
                width=20,font=("bold",20), relief = RAISED, bg= "royal blue", fg = "white" )
                booksIssue_daily_title_label.pack(side = TOP, padx=5, pady=5)

                frame1_issue_dailybooks = Frame(daily_reports_root, bd=4, relief = RIDGE, bg= "crimson")
                frame1_issue_dailybooks.place(x=50, y=60)

                scroll = ttk.Scrollbar(frame1_issue_dailybooks, orient="vertical")
                tree = ttk.Treeview(frame1_issue_dailybooks, columns = (1,2,3,4,5,6,7),
                height=5, show = "headings", yscrollcommand = scroll.set)
                #tree.place(x=50, y = 150)
                tree.grid(row = 0, column=0, padx = 5, pady =5, sticky = E)
                tree.heading(1, text = "Stdudent ID")
                tree.heading(2, text = "Student Name")
                tree.heading(3, text = "Book ID")
                tree.heading(4, text = "Book Title")
                tree.heading(5, text = "Start Date")
                tree.heading(6, text = "End Date")
                tree.heading(7, text = "Status")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 150, anchor = 'center')
                tree.column(3, width = 100, anchor = 'center')
                tree.column(4, width = 200, anchor = 'center')
                tree.column(5, width = 100, anchor = 'center')
                tree.column(6, width = 100, anchor = 'center')
                tree.column(7, width = 150, anchor = 'center')
                #scroll.place(x=930,y=180)
                scroll.grid(row=0, column=0, padx = 5, pady = 5, sticky = E)
                scroll.config(command = tree.yview)


                today = date.today()
                tree.delete(*tree.get_children())
                con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                ObjCurssor = con.cursor()
                ObjCurssor.execute("select * from issue_books where start_date = %s", (today))
                rows = ObjCurssor.fetchall()
                def show_daily():

                    if rows:
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No Daily Records found", "No books issuded Today or returned books found")
                    con.close()
                def exit_daily():
                    daily_reports_root.destroy()
                    reports_root.deiconify()
                show_daily_btn1 = Button(frame1_issue_dailybooks, text= "Show", bg = 'White',
                width = 15, font = ("bold",15),
                command = show_daily)
                show_daily_btn1.grid(row=1, column=0, padx = 10, pady = 10, sticky = E)

                exit_daily_btn1 = Button(frame1_issue_dailybooks, text= "Exit", bg = 'White',
                width = 15, font = ("bold",15),
                command = exit_daily)
                exit_daily_btn1.grid(row=2, column=0, padx = 10, pady = 10, sticky = E)

                def Onclosing_daily_reports():
                    daily_reports_root.destroy()
                    reports_root.deiconify()
                daily_reports_root.protocol("WM_DELETE_WINDOW", Onclosing_daily_reports)
                daily_reports_root.mainloop()

            def weekly_reports():

                reports_root.withdraw()
                weekly_reports_root = tk.Tk()
                weekly_reports_root.geometry('1000x400')
                weekly_reports_root.title("Books Issued Weekly")

                booksIssue_weekly_title_label = Label(weekly_reports_root , text = "Books Issued Weekly",
                width=20,font=("bold",20), relief = RAISED, bg= "royal blue", fg = "white" )
                booksIssue_weekly_title_label.pack(side = TOP, padx=5, pady=5)

                frame1_issue_weeklybooks = Frame(weekly_reports_root, bd=4, relief = RIDGE, bg= "crimson")
                frame1_issue_weeklybooks.place(x=50, y=60)

                scroll = ttk.Scrollbar(frame1_issue_weeklybooks, orient="vertical")
                tree = ttk.Treeview(frame1_issue_weeklybooks, columns = (1,2,3,4,5,6,7),
                height=5, show = "headings", yscrollcommand = scroll.set)
                #tree.place(x=50, y = 150)
                tree.grid(row = 0, column=0, padx = 5, pady =5, sticky = E)
                tree.heading(1, text = "Stdudent ID")
                tree.heading(2, text = "Student Name")
                tree.heading(3, text = "Book ID")
                tree.heading(4, text = "Book Title")
                tree.heading(5, text = "Start Date")
                tree.heading(6, text = "End Date")
                tree.heading(7, text = "Status")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 150, anchor = 'center')
                tree.column(3, width = 100, anchor = 'center')
                tree.column(4, width = 200, anchor = 'center')
                tree.column(5, width = 100, anchor = 'center')
                tree.column(6, width = 100, anchor = 'center')
                tree.column(7, width = 150, anchor = 'center')
                #scroll.place(x=930,y=180)
                scroll.grid(row=0, column=0, padx = 5, pady = 5, sticky = E)
                scroll.config(command = tree.yview)


                today = date.today()
                date_sevendays_ago = today - datetime.timedelta(days=7)
                tree.delete(*tree.get_children())
                con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                ObjCurssor = con.cursor()
                ObjCurssor.execute("select * from issue_books where start_date >= %s", (date_sevendays_ago))
                rows = ObjCurssor.fetchall()
                def show_weekly():

                    if rows:
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No Daily Records found", "No books issuded Today or returned books found")
                    con.close()
                def exit_weekly():
                    weekly_reports_root.destroy()
                    reports_root.deiconify()
                show_weekly_btn1 = Button(frame1_issue_weeklybooks, text= "Show", bg = 'White',
                width = 15, font = ("bold",15),
                command = show_weekly)
                show_weekly_btn1.grid(row=1, column=0, padx = 10, pady = 10, sticky = E)

                exit_weekly_btn1 = Button(frame1_issue_weeklybooks, text= "Exit", bg = 'White',
                width = 15, font = ("bold",15),
                command = exit_weekly)
                exit_weekly_btn1.grid(row=2, column=0, padx = 10, pady = 10, sticky = E)

                def Onclosing_weekly_reports():
                    weekly_reports_root.destroy()
                    reports_root.deiconify()
                weekly_reports_root.protocol("WM_DELETE_WINDOW", Onclosing_weekly_reports)
                weekly_reports_root.mainloop()

            def monthly_reports():

                reports_root.withdraw()
                monthly_reports_root = tk.Tk()
                monthly_reports_root.geometry('1000x400')
                monthly_reports_root.title("Books Issued Monthly")

                booksIssue_monthly_title_label = Label(monthly_reports_root , text = "Books Issued Monthly",
                width=20,font=("bold",20), relief = RAISED, bg= "royal blue", fg = "white" )
                booksIssue_monthly_title_label.pack(side = TOP, padx=5, pady=5)

                frame1_issue_monthlybooks = Frame(monthly_reports_root, bd=4, relief = RIDGE, bg= "crimson")
                frame1_issue_monthlybooks.place(x=50, y=60)

                scroll = ttk.Scrollbar(frame1_issue_monthlybooks, orient="vertical")
                tree = ttk.Treeview(frame1_issue_monthlybooks, columns = (1,2,3,4,5,6,7),
                height=5, show = "headings", yscrollcommand = scroll.set)
                #tree.place(x=50, y = 150)
                tree.grid(row = 0, column=0, padx = 5, pady =5, sticky = E)
                tree.heading(1, text = "Stdudent ID")
                tree.heading(2, text = "Student Name")
                tree.heading(3, text = "Book ID")
                tree.heading(4, text = "Book Title")
                tree.heading(5, text = "Start Date")
                tree.heading(6, text = "End Date")
                tree.heading(7, text = "Status")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 150, anchor = 'center')
                tree.column(3, width = 100, anchor = 'center')
                tree.column(4, width = 200, anchor = 'center')
                tree.column(5, width = 100, anchor = 'center')
                tree.column(6, width = 100, anchor = 'center')
                tree.column(7, width = 150, anchor = 'center')
                #scroll.place(x=930,y=180)
                scroll.grid(row=0, column=0, padx = 5, pady = 5, sticky = E)
                scroll.config(command = tree.yview)


                today = date.today()
                date_month_ago = today - datetime.timedelta(days=30)
                tree.delete(*tree.get_children())
                con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                ObjCurssor = con.cursor()
                ObjCurssor.execute("select * from issue_books where start_date >= %s", (date_month_ago))
                rows = ObjCurssor.fetchall()
                def show_monthly():

                    if rows:
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No Daily Records found", "No books issuded Today or returned books found")
                    con.close()
                def exit_monthly():
                    monthly_reports_root.destroy()
                    reports_root.deiconify()
                show_monthly_btn1 = Button(frame1_issue_monthlybooks, text= "Show", bg = 'White',
                width = 15, font = ("bold",15),
                command = show_monthly)
                show_monthly_btn1.grid(row=1, column=0, padx = 10, pady = 10, sticky = E)

                exit_monthly_btn1 = Button(frame1_issue_monthlybooks, text= "Exit", bg = 'White',
                width = 15, font = ("bold",15),
                command = exit_monthly)
                exit_monthly_btn1.grid(row=2, column=0, padx = 10, pady = 10, sticky = E)

                def Onclosing_monthly_reports():
                    monthly_reports_root.destroy()
                    reports_root.deiconify()
                monthly_reports_root.protocol("WM_DELETE_WINDOW", Onclosing_monthly_reports)
                monthly_reports_root.mainloop()

            def yearly_reports():

                reports_root.withdraw()
                yearly_reports_root = tk.Tk()
                yearly_reports_root.geometry('1000x400')
                yearly_reports_root.title("Books Issued Yearly")

                booksIssue_yearly_title_label = Label(yearly_reports_root , text = "Books Issued Yearly",
                width=20,font=("bold",20), relief = RAISED, bg= "royal blue", fg = "white" )
                booksIssue_yearly_title_label.pack(side = TOP, padx=5, pady=5)

                frame1_issue_yearlybooks = Frame(yearly_reports_root, bd=4, relief = RIDGE, bg= "crimson")
                frame1_issue_yearlybooks.place(x=50, y=60)

                scroll = ttk.Scrollbar(frame1_issue_yearlybooks, orient="vertical")
                tree = ttk.Treeview(frame1_issue_yearlybooks, columns = (1,2,3,4,5,6,7),
                height=5, show = "headings", yscrollcommand = scroll.set)
                #tree.place(x=50, y = 150)
                tree.grid(row = 0, column=0, padx = 5, pady =5, sticky = E)
                tree.heading(1, text = "Stdudent ID")
                tree.heading(2, text = "Student Name")
                tree.heading(3, text = "Book ID")
                tree.heading(4, text = "Book Title")
                tree.heading(5, text = "Start Date")
                tree.heading(6, text = "End Date")
                tree.heading(7, text = "Status")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 150, anchor = 'center')
                tree.column(3, width = 100, anchor = 'center')
                tree.column(4, width = 200, anchor = 'center')
                tree.column(5, width = 100, anchor = 'center')
                tree.column(6, width = 100, anchor = 'center')
                tree.column(7, width = 150, anchor = 'center')
                #scroll.place(x=930,y=180)
                scroll.grid(row=0, column=0, padx = 5, pady = 5, sticky = E)
                scroll.config(command = tree.yview)


                today = date.today()
                date_year_ago = today - datetime.timedelta(days=365)
                tree.delete(*tree.get_children())
                con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                ObjCurssor = con.cursor()
                ObjCurssor.execute("select * from issue_books where start_date >= %s", (date_year_ago))
                rows = ObjCurssor.fetchall()
                def show_yearly():

                    if rows:
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No yearly Records found", "No books issuded yearly or returned books found")
                    con.close()
                def exit_yearly():
                    yearly_reports_root.destroy()
                    reports_root.deiconify()
                show_yearly_btn1 = Button(frame1_issue_yearlybooks, text= "Show", bg = 'White',
                width = 15, font = ("bold",15),
                command = show_yearly)
                show_yearly_btn1.grid(row=1, column=0, padx = 10, pady = 10, sticky = E)

                exit_yearly_btn1 = Button(frame1_issue_yearlybooks, text= "Exit", bg = 'White',
                width = 15, font = ("bold",15),
                command = exit_yearly)
                exit_yearly_btn1.grid(row=2, column=0, padx = 10, pady = 10, sticky = E)

                def Onclosing_yearly_reports():
                    yearly_reports_root.destroy()
                    reports_root.deiconify()
                yearly_reports_root.protocol("WM_DELETE_WINDOW", Onclosing_yearly_reports)
                yearly_reports_root.mainloop()

            admin_btn1 = Button(adminFrame_sec, text= "Available Books", bg = 'White', width = 15, font = ("bold",15),
            command = available_books)
            admin_btn1.grid(row=0, column=0, padx =10, pady =10, sticky=W)

            admin_btn2 = Button(adminFrame_sec, text= "Daily Reports", bg = 'White', width = 15, font = ("bold",15),
            command = daily_reports)
            admin_btn2.grid(row=1, column=0, padx =10, pady =10, sticky=E)

            admin_btn3 = Button(adminFrame_sec, text= "Weekly Reports", bg = 'White', width = 15, font = ("bold",15),
            command = weekly_reports)
            admin_btn3.grid(row=2, column=0, padx =10, pady =10, sticky=W)

            admin_btn4 = Button(adminFrame_sec, text= "Monthly Reports", bg = 'White', width = 15, font = ("bold",15),
            command = monthly_reports)
            admin_btn4.grid(row=3, column=0, padx =10, pady =10, sticky=E)

            admin_btn5 = Button(adminFrame_sec, text= "Yearly Reports", bg = 'White', width = 15, font = ("bold",15),
            command = yearly_reports)
            admin_btn5.grid(row=4, column=0, padx =10, pady =10, sticky=E)

            def exit_reports():
                reports_root.destroy()
                admin_functions_root.deiconify()
            admin_btn5 = Button(reporstExitFrame, text= "Exit", bg = 'White', width = 15, font = ("bold",15),
            command = exit_reports)
            admin_btn5.grid(row=4, column=0, padx =10, pady =10, sticky=E)


            def on_closing_root_st():
                reports_root.destroy()
                admin_functions_root.deiconify()

            reports_root.protocol("WM_DELETE_WINDOW", on_closing_root_st)
            reports_root.mainloop()


        #admin_logout
        def admin_logout():
            global admin_search_check
            admin_search_check = False
            messagebox.showinfo("Admin Logout", "Thank you Admin, you are logged out")
            admin_functions_root.destroy()
            admin_login_root.deiconify()

        l1= Label(admin_functions_root, text="Admin Section",
        width=20,font=("bold", 20), relief = RAISED, bg= "royal blue",fg = "White") # First Label
        l1.pack(side = TOP, padx = 10, pady= 10)

        adminFrame_sec = Frame(admin_functions_root,  bg ="Yellow",relief = RAISED, bd=8, width=200, height=200)
        adminFrame_sec.place(x=60, y =100)


        admin_btn1 = Button(adminFrame_sec, text= "Admin Profile", bg = 'White', width = 15, font = ("bold",15),
        command = admin_profile)
        admin_btn1.grid(row=0, column=0, padx =10, pady =10, sticky=W)

        admin_btn2 = Button(adminFrame_sec, text= "Add new Students", bg = 'White', width = 15, font = ("bold",15),
        command = student_registration_wizard)
        admin_btn2.grid(row=0, column=1, padx =10, pady =10, sticky=E)

        admin_btn3 = Button(adminFrame_sec, text= "Add Books", bg = 'White', width = 15, font = ("bold",15),
        command = books_registration_wizard)
        admin_btn3.grid(row=1, column=0, padx =10, pady =10, sticky=W)

        admin_btn4 = Button(adminFrame_sec, text= "Reports", bg = 'White', width = 15, font = ("bold",15),
        command = reports)
        admin_btn4.grid(row=1, column=1, padx =10, pady =10, sticky=E)

        admin_btn5 = Button(adminFrame_sec, text= "Admin Logout", bg = 'White', width = 15, font = ("bold",15),
        command = admin_logout)
        admin_btn5.grid(row=2, column=1, padx =10, pady =10, sticky=E)


        def on_closing_root_st():
            global admin_search_check
            MsgBox = tk.messagebox.askquestion ("Logout?, Make Sure ",'Are you sure you want to logout',icon = 'warning')
            if MsgBox == 'yes':
                admin_functions_root.destroy()
                admin_login_root.deiconify()
                admin_search_check = False
            else:
                messagebox.showinfo("It's OK", "You are still logged in")
        admin_functions_root.protocol("WM_DELETE_WINDOW", on_closing_root_st)
        admin_functions_root.mainloop()
    #admin_search_check = False
    def get_admin_login():
        global user_admin
        global password_admin
        global admin_search_check
        admin_user1 = adminFrame_e1.get()
        admin_password1 = adminFrame_e2.get()
        user_admin = admin_user1
        password_admin = admin_password1
        if admin_search_check == True:
            messagebox.showinfo("Admin already logged in", "Admin is already logged in")

        elif admin_user1 == "" and admin_password1 == "":
                messagebox.showinfo('No Admin user or password', 'Eneter Admin user or password')
        else:
            con = pymysql.connect(host ="localhost", user="root", password="", database="libdatabase")
            cursorObj = con.cursor()
            cursorObj.execute("select admin_userid, admin_password from admin where admin_userid = %s and admin_password = %s",
            (admin_user1, admin_password1))
            row = cursorObj.fetchall()
            if row:
                admin_search_check = True
                messagebox.showinfo("Admin Login ","Welcome Admin, You are now Logged In")
                admin_functions()

            else:
                messagebox.showinfo("Invalid Admin User ID or password", "Invalid Admin User ID or password")
            con.close()

    login_btn =  Button(frame_admin_login, text = "Login",bg='White' ,width = 8, font = ("bold", 15),
    command=get_admin_login)
    login_btn.grid(row=2,column=1,rowspan = 5, padx=10,pady =10,sticky=E)
    def on_closing_root_st():
        admin_login_root.destroy()
        first_root.deiconify()
    admin_login_root.protocol("WM_DELETE_WINDOW", on_closing_root_st)
    admin_login_root.mainloop()
#___________________Admin Section Ends Here with logout screen___________


#__________________Student Section Starts Here ___________________________
student_search_check = False
def student_sec():
    first_root.withdraw()
    student_login_root = tk.Tk()
    student_login_root.geometry('400x300')

    l1= Label(student_login_root, text="Student Login",
    width=15,font=("bold", 20), relief = RAISED, bg= "royal blue",fg = "White") # First Label
    l1.pack(side = TOP, padx = 10, pady= 10)

    frame_student_login = Frame(student_login_root,  bg ="Yellow",relief = RAISED, bd=8, width=350, height=250)
    frame_student_login.place(x=60, y =100)

    studentFrame_l1 = Label(frame_student_login, text="User ID",font=("bold", 15),bg="Yellow" , fg = "Black")
    studentFrame_l1.grid(row=0,column=0,padx=10,pady =10, sticky = E)

    studentFrame_e1 = Entry(frame_student_login, width = 25, borderwidth = 5)
    studentFrame_e1.grid(row=0, column=1,padx=10,pady =10) # First Entry box

    studentFrame_l2 = Label(frame_student_login, text="Password",font=("bold", 15),bg="Yellow"  ,  fg = "Black")
    studentFrame_l2.grid(row=1,column=0,padx=10,pady =10,sticky = E)

    studentFrame_e2 = Entry(frame_student_login, width = 25, borderwidth = 5, show="*")
    studentFrame_e2.grid(row=1,column=1,padx=10,pady =10) # Second Entry box

    def student_functions():
        global student_id
        student_login_root.withdraw()
        student_functions_root = tk.Tk()
        student_functions_root.geometry('600x320')
        l1= Label(student_functions_root, text="Student Section",
        width=20,font=("bold", 20), relief = RAISED, bg= "royal blue",fg = "White") # First Label
        l1.pack(side = TOP, padx = 10, pady= 10)

        studentFrame_sec = Frame(student_functions_root,  bg ="Yellow",relief = RAISED, bd=8, width=200, height=200)
        studentFrame_sec.place(x=60, y =100)

        studentFrame_sec1 = Frame(student_functions_root,  bg ="Yellow",relief = RAISED, bd=8, width=200, height=200)
        studentFrame_sec1.place(x=160, y =200)

        def my_library_record():
            student_functions_root.withdraw()
            my_library_record_root = tk.Tk()
            my_library_record_root.geometry('900x400')
            my_library_record_root.title("My Library Record")
            global e_date
            global s_date
            my_library_record_label = Label(my_library_record_root , text = "My Library Record",
            width=20,font=("bold",20), relief = RAISED, bg= "royal blue", fg = "white" )
            my_library_record_label.pack(side = TOP, padx=5, pady=5)

            frame0_mylibrary = Frame(my_library_record_root, bd=4, relief = RIDGE, bg= "crimson")
            frame0_mylibrary.place(x=310, y=80)

            combo1 = ttk.Combobox(frame0_mylibrary, width = 20, height = 10, font = ("bold", 12),
            values = ["All", "Issued Books", "Returned Books"], state = 'readonly')
            combo1.grid(row=0, column=0, padx = 5, pady = 5)
            combo1.current(0)

            frame1_mylibrary = Frame(my_library_record_root, bd=4, relief = RIDGE, bg= "crimson")
            frame1_mylibrary.place(x=50, y=130)

            scroll = ttk.Scrollbar(frame1_mylibrary, orient="vertical")
            tree = ttk.Treeview(frame1_mylibrary, columns = (1,2,3,4,5,6),
            height=5, show = "headings", yscrollcommand = scroll.set)
            #tree.place(x=50, y = 150)
            tree.grid(row = 0, column=0, padx = 5, pady =5, sticky = E)
            tree.heading(1,text = "Book ID")
            tree.heading(2, text = "Book Title")
            tree.heading(3, text = "Publisher")
            tree.heading(4, text = "Issue Date")
            tree.heading(5, text = "Return Date")
            tree.heading(6, text = "status")

            tree.column(1, width = 75, anchor = 'center')
            tree.column(2, width = 200, anchor = 'center')
            tree.column(3, width = 150, anchor = 'center')
            tree.column(4, width = 100, anchor = 'center')
            tree.column(5, width = 100, anchor = 'center')
            tree.column(6, width = 150, anchor = 'center')

            scroll.grid(row=0, column=1, padx = 5, pady = 5, sticky = E)
            scroll.config(command = tree.yview)

            def show_monthly():
                tree.delete(*tree.get_children())
                today = date.today()
                con = pymysql.connect(host = "localhost", user="root", password="", database="libdatabase")
                ObjCurssor = con.cursor()
                var1 = combo1.get()
                if var1 == 'All':
                    ObjCurssor.execute("select book_id, book_title, publisher, start_date,"+
                    " end_date, status from issue_books where student_id =%s",
                    (student_id))
                    rows = ObjCurssor.fetchall()
                    if rows:
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No Records found", "There is no record of this student")
                elif var1 == 'Issued Books':
                    ObjCurssor.execute("select book_id, book_title, publisher, "+
                    "start_date, end_date, status from issue_books where student_id = %s and status =%s",
                    (student_id, "issued"))
                    rows = ObjCurssor.fetchall()
                    if rows:
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No Records found", "There is no record of this student")
                else:
                    ObjCurssor.execute("select book_id, book_title, publisher, "+
                    "start_date, end_date, status from issue_books where student_id = %s and status =%s",
                    (student_id, "Returned within due date"))
                    rows = ObjCurssor.fetchall()
                    if rows:
                        for row in rows:
                            tree.insert("", tk.END, values=row)
                    else:
                        messagebox.showinfo("No Records found", "There is no record of this student")

                con.close()
            def exit_mylibrary():
                my_library_record_root.destroy()
                student_functions_root.deiconify()
            show_monthly_btn1 = Button(frame1_mylibrary, text= "Show detials", bg = 'White',
            width = 15, font = ("bold",15),
            command = show_monthly)
            show_monthly_btn1.grid(row=1, column=0, padx = 10, pady = 10, sticky = W)

            exit_mylibrary_btn = Button(frame1_mylibrary, text= "Exit", bg = 'White',
            width = 15, font = ("bold",15),
            command = exit_mylibrary)
            exit_mylibrary_btn.grid(row=1, column=0, padx = 10, pady = 10, sticky = E)

            def Onclosing_mylibrary():
                my_library_record_root.destroy()
                student_functions_root.deiconify()
            my_library_record_root.protocol("WM_DELETE_WINDOW", Onclosing_mylibrary)
            my_library_record_root.mainloop()

        def book_shelf():
            student_functions_root.withdraw()
            book_shelf_root = tk.Tk()
            book_shelf_root.geometry('1080x500')

            bookshelf_main_label = Label(book_shelf_root , text = "Book Shelf and Issue Books",
            width=30,font=("bold",20), relief = RAISED, bg= "crimson", fg = "white" )
            bookshelf_main_label.pack(side = TOP, padx=5, pady=5)


            book_shelf_frame = Frame(book_shelf_root,  bg ="royal blue",relief = RAISED, bd=8, width=350, height=200)
            book_shelf_frame.place(x=50, y =100)


            frame2_title = Label(book_shelf_frame, text = "Books Search", font=("bold", 18), bg = "royal blue", fg="Black").grid(row=1,column=2, padx = 5, pady = 5)
            frame2_l1 = Label(book_shelf_frame, text="Title",font=("bold",15),bg="royal blue" , fg = "Black").grid(row=2,column=1,padx=5,pady =5, sticky = E)
            frame2_e1 = Entry(book_shelf_frame, width = 25, borderwidth = 5)
            frame2_e1.grid(row=2, column=2,padx=5,pady =5)

            frame2_l2 = Label(book_shelf_frame, text="Author",font=("bold", 15),bg="royal blue"  ,  fg = "Black").grid(row=3,column=1,padx=5,pady =5,sticky = E)
            frame2_e2 = Entry(book_shelf_frame, width = 25, borderwidth = 5)
            frame2_e2.grid(row=3,columnspan=5,column=2,padx=5,pady =5)
            frame2_l3 = Label(book_shelf_frame, text="Publisher",font=("bold", 15),bg="royal blue"  ,  fg = "Black").grid(row=4,column=1,padx=5,pady =5,sticky = E)
            frame2_e3 = Entry(book_shelf_frame, width = 25, borderwidth = 5)
            frame2_e3.grid(row=4,columnspan=5,column=2,padx=5,pady =5)

            frame2_l4 = Label(book_shelf_frame, text="ISBN",font=("bold", 15),bg="royal blue"  ,  fg = "Black").grid(row=5,column=1,padx=5,pady =5,sticky = E)
            frame2_e4 = Entry(book_shelf_frame, width = 25, borderwidth = 5)
            frame2_e4.grid(row=5,columnspan=5,column=2,padx=5,pady =5)

            def book_search_main():
                con = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                cursorObj = con.cursor()
                book_title=frame2_e1.get()
                frame2_e1.delete(0,END)
                frame2_e2.delete(0,END)
                frame2_e3.delete(0,END)
                frame2_e4.delete(0,END)
                cursorObj.execute("select * from books where title = %s", (book_title))
                row = cursorObj.fetchall()
                if row:
                    search_check = True
                    for r in row:
                        frame2_e1.insert(0,r[1])
                        frame2_e2.insert(0,r[2])
                        frame2_e3.insert(0,r[3])
                        frame2_e4.insert(0,r[4])
                    messagebox.showinfo("Record Searched","Record Searched successfully")
                else:
                    messagebox.showinfo("Record Searched", "Record does not exist")
                con.close()

            def clear_book_search_main():
                frame2_e1.delete(0,END)
                frame2_e2.delete(0,END)
                frame2_e3.delete(0,END)
                frame2_e4.delete(0,END)

            clear_search_btn = Button (book_shelf_frame, text ="Clear",  width = 8, font =("bold", 15), command = clear_book_search_main)
            clear_search_btn.grid(row=6, column=1, padx = 5, pady = 5, sticky=W)

            search_btn = Button (book_shelf_frame, text ="Search",  width = 10, font =("bold", 15), command = book_search_main)
            search_btn.grid(row=6, column=2, padx = 5, pady = 5, sticky=E)

            book_shelf_frame1 = Frame(book_shelf_root,  bg ="royal blue",relief = RAISED, bd=8, width=350, height=200)
            book_shelf_frame1.place(x=370, y =100)
            frame3_title = Label(book_shelf_frame1, text = "Books Shelf", font=("bold", 18), bg = "royal blue", fg="Black")
            frame3_title.grid(row=0,column=0, padx = 5, pady = 5)
            tree = ttk.Treeview(book_shelf_frame1, columns = (1,2,3,4,5), height=5, show = "headings")
            tree.grid(row=2, column = 0, padx = 5, pady = 10, sticky=E)
            tree.heading(1, text = "Book ID")
            tree.heading(2, text="Title")
            tree.heading(3, text="Author")
            tree.heading(4, text = "Publisher")
            tree.heading(5, text = "ISBN")

            tree.column(1, width = 75, anchor = 'center')
            tree.column(2, width = 200, anchor = 'center')
            tree.column(3, width = 100, anchor = 'center')
            tree.column(4, width = 100, anchor = 'center')
            tree.column(5, width = 100, anchor = 'center')

            scroll1 = ttk.Scrollbar(book_shelf_frame1, orient="vertical", command=tree.yview)
            scroll1.grid(row=2, column = 1,  sticky=W)
            tree.configure(yscrollcommand=scroll1.set)

            conn = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
            cur = conn.cursor()
            cur.execute("select * from books")
            rows = cur.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
            conn.close()

            ### issue books SECTION
            ######################
            def books_issue_wizard():
                book_shelf_root.withdraw()
                books_issue = tk.Tk()
                books_issue.title("Books Issue Section")
                books_issue.geometry('1200x500')
                global search_check_books
                search_check_books = False

                book_title = frame2_e1.get()

                Label(books_issue, text="Book Issue Section",width=15,font=("bold", 20),  fg = "Blue").place(x=500,y=10)

                Label(books_issue, text="First, Search Book in previous window to issue Book",
                        width=50,font=("bold", 15),  fg = "Black").place(x=50,y=70)

                bookFrame_l1 = Label(books_issue , text = "Book ID: ", ).place(x=40, y=150)
                bookFrame_e1 = Entry(books_issue, width = 20, borderwidth = 5)
                bookFrame_e1.place(x=110,y=150)

                bookFrame_l2 = Label(books_issue, text = "Title: ").place(x=60,y=190)
                bookFrame_e2 = Entry(books_issue, width = 20, borderwidth=5)
                bookFrame_e2.place(x=110,y=190)

                bookFrame_l3 = Label(books_issue, text = "Author: ").place(x=40,y=230)
                bookFrame_e3 = Entry(books_issue, width = 20, borderwidth=5)
                bookFrame_e3.place(x=110,y=230)

                bookFrame_l4 = Label(books_issue, text = "Publisher: ").place(x=30,y=270)
                bookFrame_e4 = Entry(books_issue, width = 20, borderwidth=5)
                bookFrame_e4.place(x=110, y = 270)

                bookFrame_l5 = Label(books_issue, text = "ISBN: ").place(x=60,y=310)
                bookFrame_e5 = Entry(books_issue, width = 20, borderwidth=5)
                bookFrame_e5.place(x=110, y = 310)

                bookFrame_l6 = Label(books_issue , text = "Student ID: " ).place(x=310, y=150)
                bookFrame_e6 = Entry(books_issue, width = 20, borderwidth=5)
                bookFrame_e6.place(x=390, y = 150)

                bookFrame_l7 = Label(books_issue, text = "Student Name: ").place(x=290,y = 200)
                bookFrame_e7 = Entry(books_issue, width = 20, borderwidth=5)
                bookFrame_e7.place(x=390,y=200)

                Label(books_issue, text="Books issued to the Student, To view Click Show",
                        width=40,font=("bold", 15),  fg = "Black").place(x=650,y=150)

                ttk.Label(books_issue, text='Choose Start date').place(x=280, y=250)
                cal1 = DateEntry(books_issue, dateformat = 4, width=12, background='darkblue',
                                        foreground='white', borderwidth=2)
                cal1.place(x=390, y=250)

                ttk.Label(books_issue, text = 'Choose End date').place(x=280,y=300)
                cal2 = DateEntry(books_issue, datefomat =4,  width = 12, background = 'darkblue', foreground='white', borderwidth=2)
                cal2.place(x = 390, y = 300)

                def issue_and_DateCheck():
                    if bookFrame_e1.get() == "":
                        messagebox.showinfo("Search not performed", "The Book can't be issued, search is not performed")
                    else:
                        con = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                        cursorObj = con.cursor()
                        cursorObj.execute("select * from issue_books where book_id = %s and status = %s",
                        (bookFrame_e1.get(), "issued"))
                        row = cursorObj.fetchall()

                        if row:
                            messagebox.showinfo("Book Issued", "This book is  issued already, Thanks")
                        else:
                            start_date = cal1.get_date()
                            end_date = cal2.get_date()

                            if start_date >= end_date:
                                messagebox.showinfo('Date Check', 'Date is not choosen appropriately')
                            else:

                                book_id = bookFrame_e1.get()
                                book_title = bookFrame_e2.get()
                                student_id1 = bookFrame_e6.get()
                                student_name1 = bookFrame_e7.get()
                                book_status = 'issued'
                                cursorObj.execute("INSERT INTO issue_books values(%s, %s, %s, %s, %s, %s, %s)",
                                (int(student_id1), student_name1, int(book_id), book_title, start_date,
                                        end_date, book_status))
                                con.commit()

                                messagebox.showinfo("Book Issue Status", "Book Issued successfully")
                        con.close()

                con = pymysql.connect(host = "localhost", user="root", password= "", database="libdatabase")
                cursorObj = con.cursor()
                book_title=frame2_e1.get()
                bookFrame_e1.delete(0,END)
                bookFrame_e2.delete(0,END)
                bookFrame_e3.delete(0,END)
                bookFrame_e4.delete(0,END)
                bookFrame_e5.delete(0,END)
                cursorObj.execute("select * from books where title = %s", (book_title))
                row = cursorObj.fetchall()

                search_check = True
                for r in row:
                    bookFrame_e1.insert(0,r[0])
                    bookFrame_e2.insert(0,r[1])
                    bookFrame_e3.insert(0,r[2])
                    bookFrame_e4.insert(0,r[3])
                    bookFrame_e5.insert(0,r[4])
                con.close()
                if bookFrame_e1.get() == "":
                    Label(books_issue, text="The Book can't be issued, search is not performed",
                            width=50,font=("bold", 15),  fg = "red").place(x=50,y=420)


                bookFrame_e6.delete(0,END)
                bookFrame_e7.delete(0,END)

                con = pymysql.connect(host = "localhost", user = "root", password="", database= "libdatabase")
                cursorObj = con.cursor()

                cursorObj.execute("select * from students where student_id = %s", (student_id))
                row = cursorObj.fetchall()

                for r in row:
                    bookFrame_e6.insert(0,r[0])
                    bookFrame_e7.insert(0,r[1])
                con.close()
                Student_ID = r[0]
                tree = ttk.Treeview(books_issue, columns = (1,2,3,4,5), height=5, show = "headings")
                tree.place(x=550, y = 210)
                tree.heading(1, text = "Book ID")
                tree.heading(2, text = "Book Title")
                tree.heading(3, text = "Start Date")
                tree.heading(4, text = "End Date")
                tree.heading(5, text = "Book Status")

                tree.column(1, width = 75, anchor = 'center')
                tree.column(2, width = 150, anchor = 'center')
                tree.column(3, width = 100, anchor = 'center')
                tree.column(4, width = 100, anchor = 'center')
                tree.column(5, width = 150, anchor = 'center')
                scroll = ttk.Scrollbar(books_issue, orient="vertical", command=tree.yview)
                scroll.place(x=1135,y=240)
                tree.configure(yscrollcommand=scroll.set)

                def show():
                    tree.delete(*tree.get_children())
                    conn = pymysql.connect(host = "localhost", user="root", password="",database="libdatabase")
                    cur = conn.cursor()
                    cur.execute("select book_id, book_title, start_date, end_date, status from issue_books where student_id = %s",
                        (int(Student_ID)))
                    rows = cur.fetchall()

                    for row in rows:
                        tree.insert("", tk.END, values=row)
                    conn.close()

                def return_book():
                    if bookFrame_e1.get() == "":
                        messagebox.showinfo("Search is not performed", "First search the book in the previous screen")
                    else:
                        con = pymysql.connect(host = "localhost", user = "root", password= "", database= "libdatabase")
                        ObjCurssor = con.cursor()
                        ObjCurssor.execute("select * from issue_books where student_id = %s and (status = %s or status = %s)",
                        (bookFrame_e6.get(), "Returned after due date", "Returned within due date"))
                        row1 = ObjCurssor.fetchall()
                        if row1:
                            messagebox.showinfo("Book already returnd", "This Book was returned already")
                        else:
                            MsgBox = tk.messagebox.askquestion ('Make Sure return book','Are you sure you want to return the book',icon = 'warning')
                            if MsgBox == 'yes':
                                ObjCurssor.execute("select end_date from issue_books where book_id = %s", int(bookFrame_e1.get()))
                                row = ObjCurssor.fetchall()
                                for r in row:
                                    end_date = r[0]
                                if end_date < date.today():
                                    messagebox.showinfo("retun date expired", "Book return date has been expired")
                                    return_status = "Returned after due date"
                                    ObjCurssor.execute("update issue_books set status = %s where book_id = %s",
                                    (return_status, int(bookFrame_e1.get())))
                                    con.commit()
                                else:
                                    return_status = "Returned within due date"
                                    ObjCurssor.execute("update issue_books set status = %s where book_id = %s",
                                        (return_status, int(bookFrame_e1.get())))
                                    con.commit()
                                messagebox.showinfo('Book Status', 'Book returned successfully')
                            else:
                                messagebox.showinfo("No book returned", "No any book was made returned")
                        con.close()

                def exit():
                    books_issue.destroy()
                    book_shelf_root.deiconify()

                bookFrame_btn_issue = Button(books_issue, text = "Issue Book",  width = 10, font = ("bold", 12), command = issue_and_DateCheck)
                bookFrame_btn_issue.place(x=310, y= 370)

                bookFrame_btn_show = Button(books_issue, text = "Show",  width = 10, font = ("bold", 12), command = show)
                bookFrame_btn_show.place(x=430, y= 370)

                bookFrame_btn_rtnbook = Button(books_issue, text = "Return Book",
                width = 10, font = ("bold", 12), command = return_book)
                bookFrame_btn_rtnbook.place(x=550, y= 370)

                bookFrame_btn_exit = Button(books_issue, text = "Exit", width = 10, font = ("bold", 12), command = exit)
                bookFrame_btn_exit.place(x=670, y= 370)

                def on_closing_book_issue():
                    books_issue.destroy()
                    book_shelf_root.deiconify()

                books_issue.protocol("WM_DELETE_WINDOW", on_closing_book_issue)
                books_issue.mainloop()
            ###### END OF ISSUE BOOKS SECTION ######
            ########################################


            def refresh_shelf():
                conn = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
                cur = conn.cursor()
                cur.execute("select * from books")
                rows = cur.fetchall()
                tree.delete(*tree.get_children())
                for row in rows:
                    tree.insert("", tk.END, values=row)
                messagebox.showinfo('Book Shelf', 'Book Shelf is refreshed')
                conn.close()


            issue_btn = Button (book_shelf_frame1, text ="Issue Books", width = 10,
            font =("bold", 12), command = books_issue_wizard)
            issue_btn.grid(row=3, column=0, padx = 5, pady = 5, sticky=W)
            refresh_books_btn = Button (book_shelf_frame1,
            text ="Refresh Shelf", width = 12, font =("bold", 12), command=refresh_shelf)
            refresh_books_btn.grid(row=3, column=0, padx = 5, pady = 5 ,sticky=E)


            book_shelf_frame2 = Frame(book_shelf_root,  bg ="crimson",relief = RAISED, bd=8, width=350, height=200)
            book_shelf_frame2.place(x=500, y =380)

            def exit_shelf():
                book_shelf_root.destroy()
                student_functions_root.deiconify()

            Exit_btn = Button (book_shelf_frame2, text ="Exit",  width = 10, font =("bold", 15), command = exit_shelf)
            Exit_btn.grid(row=0, column=0, padx = 10, pady = 10, sticky=E)

            def Onclosing_shelf():
                book_shelf_root.destroy()
                student_functions_root.deiconify()

            book_shelf_root.protocol("WM_DELETE_WINDOW", Onclosing_shelf)
            book_shelf_root.mainloop()


        def student_logout():
            global student_search_check
            student_search_check = False
            messagebox.showinfo("student Logout", "You are logged out, Have a nice day!")
            student_functions_root.destroy()
            student_login_root.deiconify()



        student_btn1 = Button(studentFrame_sec, text= "My Library Record", bg = 'White', width = 20, font = ("bold",15),
        command = my_library_record)
        student_btn1.grid(row=0, column=0, padx =10, pady =10, sticky=W)

        student_btn2 = Button(studentFrame_sec, text= "Book Shelf", bg = 'White', width = 15, font = ("bold",15),
        command = book_shelf)
        student_btn2.grid(row=0, column=1, padx =10, pady =10, sticky=E)

        admin_btn5 = Button(studentFrame_sec1, text= "Student Logout", bg = 'White', width = 15, font = ("bold",15),
        command = student_logout)
        admin_btn5.grid(row=1, column=1, padx =10, pady =10, sticky=E)


        def Onclosing_stFunctions_root():
            global student_search_check
            MsgBox = tk.messagebox.askquestion ("Logout?, Make Sure ",'Are you sure, want to logout',icon = 'warning')
            if MsgBox == 'yes':
                student_functions_root.destroy()
                student_login_root.deiconify()
                student_search_check = False
            else:
                messagebox.showinfo("It's OK", "You are still logged in")
        student_functions_root.protocol("WM_DELETE_WINDOW", Onclosing_stFunctions_root)
        student_functions_root.mainloop()

    def get_student_login():
        global student_id
        global user1
        global password1
        global student_search_check
        user = studentFrame_e1.get()
        password = studentFrame_e2.get()
        if student_search_check == True:
            messagebox.showinfo("Student already logged in", "Student is already logged in")

        elif user == "" and password == "":
                messagebox.showinfo('No user or password', 'Eneter user or password')
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="libdatabase")
            cursorObj = con.cursor()

            cursorObj.execute("select * from students where user = %s and password = %s",
            (user, password))
            row = cursorObj.fetchall()
            if row:
                student_search_check = True
                for r in row:
                    student_id = r[0]
                    user1 = r[3]
                    password1 = r[4]
                    messagebox.showinfo("User searched ","You are now Logged In")
                    student_functions()
            else:
                messagebox.showinfo("Invalid User ID or password", "Invalid User ID or password")
            con.close()


    st_login_btn =  Button(frame_student_login, text = "Login",bg='White' ,width = 8, font = ("bold", 15),
    command= get_student_login)
    st_login_btn.grid(row=2,column=1,rowspan = 5, padx=10,pady =10,sticky=E)

    def on_closing_student_sec():
        student_login_root.destroy()
        first_root.deiconify()

    student_login_root.protocol("WM_DELETE_WINDOW", on_closing_student_sec)
    student_login_root.mainloop()

#__________________Student Section Ends Here _____________________________
admin_section_btn =  Button(frame1, text = "ADMIN Section",bg='White'
 ,width = 15, font = ("bold", 15), command=admin_sec)
admin_section_btn.grid(row=0,column=0,padx=10,pady =10,sticky=E)

student_section_btn =  Button(frame2, text = "Student section",bg='White'
,width = 15, font = ("bold", 15), command= student_sec)
student_section_btn.grid(row=0,column=0,padx=10,pady =10,sticky=E)

mainroot_exit_btn =  Button(frame3, text = "Exit",bg='White' ,fg ='Red', width = 15, font = ("bold", 15), command=first_root.destroy)
mainroot_exit_btn.grid(row=0,column=0,padx=10,pady =10,sticky=E)


first_root.mainloop()
