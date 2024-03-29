from tkinter import *
# from tkinter import messagebox


from institute_view_docs import *
from report_frontend import *

def open_institute_homepage():
    window = Tk()

    def viewDocuments():
        print("calling load view docs")
        window.destroy()
        load_institute_view_docs()

    def report():
        window.destroy()
        load_report_page()

    height = 650
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")

    # ================Background Image ====================
    backgroundImage = PhotoImage(file="assets\\institute_bg.png")
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
        text="Institute Home Page",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#000000"
    )
    headerText1.place(x=110, y=45)

    # =============== Button1 ====================
    buttonImage1 = PhotoImage(file="assets\\institute_b1.png")
    button1 = Button(
        bg_image,
        image=buttonImage1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=viewDocuments
    )
    button1.place(x=50, y=120, width=500, height=65)

    # =============== Button2 ====================
    buttonImage3 = PhotoImage(file="assets\\institute_reports.png")
    button3 = Button(
        bg_image,
        image=buttonImage3,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=report
    )
    button3.place(x=50, y=220, width=500, height=65)


    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    open_institute_homepage()