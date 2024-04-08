from tkinter import Tk, Button
from Student_login import open_student_login
from student_register import studentSignup

def open_login_page():
    root.destroy()
    open_student_login()

def open_register_page():
    root.destroy()
    studentSignup()

root = Tk()
root.title("EduVault : Academic Records Management")

# Add buttons to switch between login and register pages
login_button = Button(root, text="Login", command=open_login_page)
login_button.pack(pady=20)

register_button = Button(root, text="Register", command=open_register_page)
register_button.pack(pady=20)

root.mainloop()
