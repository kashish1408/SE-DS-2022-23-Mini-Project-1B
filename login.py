from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Kashish' and passwordEntry.get()=='1234':
       messagebox.showinfo("Success","Welcome")
       window.destroy()
       import lms
    elif usernameEntry.get() == 'ABCD' and passwordEntry.get() == 'xyz123':
       messagebox.showinfo("Success", "Welcome")
       window.destroy()
       import lms

    else:
        messagebox.showerror('Error','Please enter correct credentials')


window = Tk()

window.geometry('1280x700+0+0')
window.title("Login Page of Techno Library")

window.resizable(False, False)

backgroundImage = Image.open("C:\\Users\\Gautam\\Downloads\\bg.jpg")
bg = ImageTk.PhotoImage(backgroundImage)

bgLabel = Label(window, image = bg)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='logo.png')

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue',show='*')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('times new roman',20,'bold'),width=15,fg='white',
                   bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)






window.mainloop()