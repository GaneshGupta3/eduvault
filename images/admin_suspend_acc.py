from tkinter import Tk, Frame, Label, Button, BOTTOM, FLAT,Entry,Canvas,StringVar
from tkinter import messagebox
from admin_homepage import *
from tkinter import PhotoImage
from current_user_info import *
from admin import *


def open_admin_suspend_acc():
    
    def fetch():
        to_be_suspended_uid = str(uid_entry.get())
        to_be_suspended_type = str(uid_entry.get()[0])
        print(type(to_be_suspended_uid))
        print(type(to_be_suspended_type))
        currentuserInfo = currentUserInfo(to_be_suspended_uid,to_be_suspended_type)
        currentUserName = currentuserInfo.name
        print(currentUserName)
        print(type(currentUserName))
        name_output_entry.delete(0, "end")
        # Insert the currentUserName
        name_output_entry.insert(0, currentUserName)

        

    def suspend():
        admin = Admin()
        to_be_suspended_uid = str(uid_entry.get())
        admin.suspend_unsuspend(to_be_suspended_uid,1)

    

    window = Tk()
    def back():
        window.destroy()
        open_admin_homepage()

    height = 650
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")

    # ================Background Image ====================
    backgroundImage = PhotoImage(file="assets\\admin_bg.png")
    bg_image = Label(
        window,
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
        text="Suspend an Account",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    headerText1.place(x=110, y=45)

    # ================ Enter uid ====================
    image1 = PhotoImage(file="assets\\input_img.png")
    image1_Label = Label(
        bg_image,
        image=image1,
        bg="#272A37"
    )
    image1_Label.place(x=60, y=90)

    uid_text = Label(
        image1_Label,
        text="Enter UID",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    uid_text.place(x=25, y=0)


    uid_entry = Entry(
        image1_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    uid_entry.place(x=8, y=17, width=140, height=27)

    # =============== Button1 ====================
    buttonImage1 = PhotoImage(file="assets\\fetch.png")
    button1 = Button(
        bg_image,
        image=buttonImage1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=fetch
    )
    button1.place(x=265, y=86, width=333, height=65)

    # ================ Line ====================
    image2 = PhotoImage(file="assets\\line.png")
    image2_Label = Label(
        bg_image,
        image=image2,
        bg="#272A37"
    )
    image2_Label.place(x=60, y=190)

    # ================ Name Output ====================
    image3 = PhotoImage(file="assets\\email.png")
    image3_Label = Label(
        bg_image,
        image=image3,
        bg="#272A37"
    )
    image3_Label.place(x=60, y=250)

    name_text = Label(
        image3_Label,
        text="Name",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    name_text.place(x=25, y=0)

    name_output_entry = Entry(
        image3_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )

    name_output_entry.place(x=8, y=17, width=140, height=27)


    # =============== Button2 ====================

    buttonImage2 = PhotoImage(file="assets\\suspend.png")
    button2 = Button(
        bg_image,
        image=buttonImage2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=suspend
    )
    button2.place(x=100, y=430, width=333, height=65)

    # =============== Button3 ====================
    buttonImage3 = PhotoImage(file="assets\\back.png")
    button3 = Button(
        bg_image,
        image=buttonImage3,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=back
    )
    button3.place(x=40, y=560, width=60, height=60)

    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    open_admin_suspend_acc()