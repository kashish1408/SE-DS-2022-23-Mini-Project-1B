from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql

#functionality part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def issue_book():
    def issue_data():
        indexing = bookTable.focus()
        print(indexing)
        content = bookTable.item(indexing)
        content_id = content['values'][0]
        query = 'delete from books where book_id=%s'
        mycursor.execute(query, content_id)
        con.commit()
        messagebox.showinfo('Issued', f'Book ID {content_id} is issued successfully',parent=issue_window)
        issue_window.destroy()
        query = 'select * from books'
        mycursor.execute(query)
        query = 'select * from books'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        bookTable.delete(*bookTable.get_children())
        for data in fetched_data:
            bookTable.insert('', END, values=data)

    issue_window = Toplevel()
    issue_window.title('Issue Books')
    issue_window.grab_set()
    issue_window.resizable(False, False)
    idLabel = Label(issue_window, text='Book ID', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(issue_window, font=('times new roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(issue_window, text='Book Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(issue_window, font=('times new roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    authorLabel = Label(issue_window, text='Book Author', font=('times new roman', 20, 'bold'))
    authorLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    authorEntry = Entry(issue_window, font=('times new roman', 15, 'bold'), width=24)
    authorEntry.grid(row=2, column=1, pady=15, padx=10)

    studentLabel = Label(issue_window, text='Student Name', font=('times new roman', 20, 'bold'))
    studentLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    studentEntry = Entry(issue_window, font=('times new roman', 15, 'bold'), width=24)
    studentEntry.grid(row=3, column=1, pady=15, padx=10)

    studentidLabel = Label(issue_window, text='Student ID', font=('times new roman', 20, 'bold'))
    studentidLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    studentidEntry = Entry(issue_window, font=('times new roman', 15, 'bold'), width=24)
    studentidEntry.grid(row=4, column=1, pady=15, padx=10)

    departmentLabel = Label(issue_window, text='Department', font=('times new roman', 20, 'bold'))
    departmentLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    departmentEntry = Entry(issue_window, font=('times new roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=5, column=1, pady=15, padx=10)

    yearLabel = Label(issue_window, text='Year', font=('times new roman', 20, 'bold'))
    yearLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    yearEntry = Entry(issue_window, font=('times new roman', 15, 'bold'), width=24)
    yearEntry.grid(row=6, column=1, pady=15, padx=10)

    issue_book_button = ttk.Button(issue_window, text='ISSUE BOOK',command=issue_data)
    issue_book_button.grid(row=7, columnspan=2, pady=15)

    indexing=bookTable.focus()
    print(indexing)
    content=bookTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    authorEntry.insert(0,listdata[2])



def view_book():
    query = 'select * from books'
    mycursor.execute(query)
    query = 'select * from books'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    bookTable.delete(*bookTable.get_children())
    for data in fetched_data:
        bookTable.insert('', END, values=data)


def delete_book():
    indexing=bookTable.focus()
    print(indexing)
    content=bookTable.item(indexing)
    content_id=content['values'][0]
    query='delete from books where book_id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Book ID {content_id} is deleted successfully')
    query='select * from books'
    mycursor.execute(query)
    query='select * from books'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    bookTable.delete(*bookTable.get_children())
    for data in fetched_data:
        bookTable.insert('',END,values=data)



def search_book():
    def search_data():
        query='select * from books where book_id=%s or book_name=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get()))
        bookTable.delete(*bookTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            bookTable.insert('',END,values=data)



    search_window = Toplevel()
    search_window.title('Search Books')
    search_window.grab_set()
    search_window.resizable(False, False)
    idLabel = Label(search_window, text='Book ID', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Book Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    authorLabel = Label(search_window, text='Book Author', font=('times new roman', 20, 'bold'))
    authorLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    authorEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    authorEntry.grid(row=2, column=1, pady=15, padx=10)

    search_book_button = ttk.Button(search_window, text='SEARCH BOOK', command=search_data)
    search_book_button.grid(row=3, columnspan=2, pady=15)

def add_book():
    def add_data():
      if idEntry.get()=='' or nameEntry.get()=='' or authorEntry.get()=='':
        messagebox.showerror('Error','All Fields are required',parent=add_window)

      else:
          currentdate = time.strftime('%d/%m/%y')
          try:
              query='insert into books values(%s,%s,%s,%s)'
              mycursor.execute(query,(idEntry.get(),nameEntry.get(),authorEntry.get(),currentdate))
              con.commit()
              messagebox.showinfo('Success','Data added successfully',parent=add_window)
              add_window.destroy()
          except:
              messagebox.showerror('Error','ID cannot be repeated',parent=add_window)
              return

      query='select * from books'
      mycursor.execute(query)
      fetched_data=mycursor.fetchall()
      bookTable.delete(*bookTable.get_children())
      for data in fetched_data:
          bookTable.insert('',END,values=data)



    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)
    idLabel=Label(add_window,text='Book ID',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('times new roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(add_window, text='Book Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    nameEntry = Entry(add_window, font=('times new roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    authorLabel = Label(add_window, text='Book Author', font=('times new roman', 20, 'bold'))
    authorLabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    authorEntry = Entry(add_window, font=('times new roman', 15, 'bold'), width=24)
    authorEntry.grid(row=2, column=1, pady=15, padx=10)

    add_book_button=ttk.Button(add_window,text='ADD BOOK',command=add_data)
    add_book_button.grid(row=3,columnspan=2,pady=15)

def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='Kashh@athu0814')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database technolibrary'
            mycursor.execute(query)
            query='use technolibrary'
            mycursor.execute(query)
            query='create table books(book_id int not null primary key, book_name varchar(50),book_author varchar(30), date varchar(50))'
            mycursor.execute(query)
        except:
            query='use technolibrary'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addBookButton.config(state=NORMAL)
        searchBookButton.config(state=NORMAL)
        deleteBookButton.config(state=NORMAL)
        issueBookButton.config(state=NORMAL)
        viewBookButton.config(state=NORMAL)



    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    root.resizable(False,False)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('times new roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('times new roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('times new roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)




def clock():
    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f' Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)



#GUI Part
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(False,False)
root.title("Techno Library")

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Techno Library'
sLabel=Label(root,text=s,font=('arial',28,'italic bold'))
sLabel.place(x=400,y=0)

connectButton=ttk.Button(root,text='Connect to Database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student (1).png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addBookButton=ttk.Button(leftFrame,text='Add Book',width=25,state=NORMAL,command=add_book)
addBookButton.grid(row=1,column=0,pady=20)

searchBookButton=ttk.Button(leftFrame,text='Search Book',width=25,state=NORMAL,command=search_book)
searchBookButton.grid(row=2,column=0,pady=20)

deleteBookButton=ttk.Button(leftFrame,text='Delete Book',width=25,state=NORMAL,command=delete_book)
deleteBookButton.grid(row=3,column=0,pady=20)

issueBookButton=ttk.Button(leftFrame,text='Issue Book',width=25,state=NORMAL,command=issue_book)
issueBookButton.grid(row=4,column=0,pady=20)

viewBookButton=ttk.Button(leftFrame,text='View Book',width=25,state=NORMAL,command=view_book)
viewBookButton.grid(row=5,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=6,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

bookTable=ttk.Treeview(rightFrame,columns=('Book ID','Book Name','Book Author','Added Date'),
                    xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=bookTable.xview)
scrollBarY.config(command=bookTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

bookTable.pack(expand=1,fill=BOTH)

bookTable.heading('Book ID',text='Book ID')
bookTable.heading('Book Name',text='Book Name')
bookTable.heading('Book Author',text='Book Author')
bookTable.heading('Added Date',text='Added Date')

bookTable.config(show='headings')




root.mainloop()