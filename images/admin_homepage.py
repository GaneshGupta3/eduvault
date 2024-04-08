import mysql.connector
from tkinter import Tk, Frame, Label, Button, BOTTOM, FLAT,Entry,Canvas
from tkinter import messagebox
from tkinter import PhotoImage
from admin_approval import *
from admin_suspend_acc import *
from admin_view_report import *


def open_admin_homepage(user_id):
    root = tk.Tk()

    def pendingInstituteApproval():
        # root.destroy()
        load_admin_approval(root)
        
        

    def suspendAccounts():
        # root.destroy()
        
        open_admin_suspend_acc(root)

    def reports():
        # root.destroy()
        open_admin_view_report(root)
        

    height = 650
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.configure(bg="#525561")

    # ================Background Image ====================
    backgroundImage = PhotoImage(file="assets\\admin_bg.png")
    bg_image = Label(
        root,
        image=backgroundImage,
        bg="#525561"
    )
    bg_image.place(x=0, y=0)

    # ================ Header Text Left ====================
    headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
    headerText_image_label1 = Label(
        bg_image,
        image=headerText_image_left,
        bg="#272A37"
    )
    headerText_image_label1.place(x=60, y=45)

    headerText1 = Label(
        bg_image,
        text="Admin's Home Page",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    headerText1.place(x=110, y=45)

    # =============== Button1 ====================
    buttonImage1 = PhotoImage(file="assets\\admin_b1.png")
    button1 = Button(
        bg_image,
        image=buttonImage1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command = pendingInstituteApproval
    )
    button1.place(x=50, y=120, width=500, height=65)


    # =============== Button2 ====================
    buttonImage2 = PhotoImage(file="assets\\admin_b2.png")
    button2 = Button(
        bg_image,
        image=buttonImage2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=suspendAccounts
    )
    button2.place(x=50, y=270, width=500, height=65)


    # =============== Button3 ====================
    buttonImage3 = PhotoImage(file="assets\\admin_reports.png")
    button3 = Button(
        bg_image,
        image=buttonImage3,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=reports
    )
    button3.place(x=50, y=420, width=500, height=65)

    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    open_admin_homepage("A902523114842")