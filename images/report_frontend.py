from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from institute_homepage import *
from report import *


def open_report_page(userid,root):
    window = tk.Toplevel(root)

    

    height = 650
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")

    # ================Background Image ====================
    backgroundImage = PhotoImage(file="assets\\institute_view_docs_bg.png")
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
        bg="#000000"
    )
    headerText_image_label1.place(x=60, y=45)

    headerText1 = Label(
        bg_image,
        text="File a Report",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#000000"
    )
    headerText1.place(x=110, y=45)


    # ================ Enter uid ====================
    image1 = PhotoImage(file="assets\\input_img.png")
    image1_Label = Label(
        bg_image,
        image=image1,
        bg="#000000"
    )
    image1_Label.place(x=60, y=90)

    uid_text = Label(
        image1_Label,
        text="Enter UID",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3d404b"
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

    # ================ Line ====================
    image2 = PhotoImage(file="assets\\line.png")
    image2_Label = Label(
        bg_image,
        image=image2,
        bg="#272A37"
    )
    image2_Label.place(x=60, y=190)

    # ================  report ====================
    image3 = PhotoImage(file="assets\\institute_docs_msg.png")
    image3_Label = Label(
        bg_image,
        image=image3,
        bg="#000000"
    )
    image3_Label.place(x=60, y=220)

    msg_text = Label(
        image3_Label,
        text="Elaborate Report: ",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 16),
        bg="#3d404b"
    )
    msg_text.place(x=25, y=0)

    msg_entry = Text(
        image3_Label,
        bd=0,
        bg="#3d404b",
        fg='#ffffff',
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 13),
    )
    msg_entry.place(x=8, y=42, width=580, height=227)


    # =============== Button1 ====================
    def report():
        report = Report()
        student_uid = uid_entry.get()
        msg = msg_entry.get("1.0", "end-1c")
        report.submit_report(userid,student_uid,msg)
        print("report submitted")
    buttonImage1 = PhotoImage(file="assets\\report.png")
    button1 = Button(
        bg_image,
        image=buttonImage1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=report
    )
    button1.place(x=200, y=550, width=320, height=65)

    # ================back button ====================#
    def load_institute_homepage():
        window.destroy()
    
        open_institute_homepage()

        
    buttonImage2 = PhotoImage(file="assets\\back.png")
    button2 = Button(
        bg_image,
        image=buttonImage2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=load_institute_homepage
    )
    button2.place(x=130, y=560, width=60, height=55)


    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    open_report_page("I902523114842")