from tkinter import Tk,Frame,Label,Button,BOTTOM,FLAT,Entry,Canvas
from tkinter import messagebox
from tkinter import messagebox as mb
import datetime
import hashlib
import random
from dbConnection import *
from uidGenerator import *
from password import *
from Institue_login import *
from tkinter import PhotoImage








def load_register():
    def checkInstitute(tan):
        dbobj = db()
        mydb,cursor = dbobj.dbconnect("credentials")
        sql_query = "SELECT * FROM institute WHERE tan = %s"
        cursor.execute(sql_query, (tan,))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False

    def instituteInsert(uid,name,tan,email,phone,password):
        dbobj = db()
        mydb,cursor = dbobj.dbconnect("credentials")
        
        institute_query = "INSERT INTO institute (uid,name,tan,email,phone,verified,suspended) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        institute_data = (uid,name,tan,email,phone,0,0)
        cursor.execute(institute_query, institute_data)
        login_query = "INSERT INTO login (uid,`key`, hash) VALUES (%s, %s, %s)"
        login_data = (uid, "key", password)
        cursor.execute(login_query, login_data)
        
        mydb.commit()
        mydb.close()
        
        userID = uid
        successMessage =f"Registration Successful. Your User ID is {userID}"
        mb.showinfo("Success",successMessage)


        

    def saveinfo():
            institute_name = institute_name_entry.get()
            institute_email = email_entry.get()
            institute_phone = contact_entry.get()
            institute_tan = tan_entry.get()
            institute_password = password_entry.get()

            uidobj = uid(institute_tan,0)
            generated_uid = uidobj.generate_unique_12_digit_number()
            passFuncobj = passFunc("key",institute_password,institute_password)
            boiledPass = passFuncobj.generateBoilpass()

            if not (checkInstitute(institute_tan)):
                instituteInsert(generated_uid,institute_name,institute_tan,institute_email,institute_phone,boiledPass)
            else:
                mb.showerror("Warning", f"The TAN number '{institute_tan}' is already registered")

    def instituteSignup():
        saveinfo()












    def validate_institute_name():
        institute_name = institute_name_entry.get()
        if len(institute_name) < 1:
            return False
        return True

    def validate_email():
        email = email_entry.get()
        if not email.endswith('.com'):
            return False
        return True

    def validate_contact_number():
        contact_number = contact_entry.get()
        if len(contact_number) != 10 or not contact_number.isdigit():
            return False
        return True

    def submit_form():
        if not validate_institute_name():
            messagebox.showerror("Error", "Please enter Institute Name!")
            return
        if not validate_email():
            messagebox.showerror("Error", "Please enter a valid Email ID ending with '.com'!")
            return
        if not validate_contact_number():
            messagebox.showerror("Error", "Please enter a proper Contact number!")
            return
        instituteSignup()
        
        # Get user input data
        institute_name = institute_name_entry.get()
        email = email_entry.get()
        contact_number = contact_entry.get()
        tan_number = tan_entry.get()
        password = password_entry.get()
        
        # Display success message with user input data
        message = f"The Institute Account has been Successfully Created!\n\n"
        message += f"Institute Name: {institute_name}\n"
        message += f"Email: {email}\n"
        message += f"Contact Number: {contact_number}\n"
        message += f"TAN Number: {tan_number}\n"

        messagebox.showinfo("Success", message)

    window = Tk()

    def load_login_page():
        window.destroy()
        page()


    height = 650
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")

    # ================Background Image ====================
    backgroundImage = PhotoImage(file="assets\\image_1.png")
    bg_image = Label(
        window,
        image=backgroundImage,
        bg="#525561"
    )
    bg_image.place(x=120, y=28)

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
        text="Welcome !",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    headerText1.place(x=110, y=45)

    # ================ CREATE ACCOUNT HEADER ====================
    createAccount_header = Label(
        bg_image,
        text="Create Institute Account",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 28 * -1),
        bg="#272A37"
    )
    createAccount_header.place(x=75, y=80)

    # ================ Institute Name Section ====================
    institute_name_image = PhotoImage(file="assets\\input_img.png")
    institute_name_image_Label = Label(
        bg_image,
        image=institute_name_image,
        bg="#272A37"
    )
    institute_name_image_Label.place(x=80, y=175)

    institute_name_text = Label(
        institute_name_image_Label,
        text="Institute Name:",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    institute_name_text.place(x=50, y=0)

    institute_name_entry = Entry(
        institute_name_image_Label,
        bd=0,
        bg="#3D404B",
        fg = "white",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    institute_name_entry.place(x=8, y=17, width=356, height=27)

    # ================ Email Section ====================
    email_image = PhotoImage(file="assets\\email.png")
    email_image_Label = Label(
        bg_image,
        image=email_image,
        bg="#272A37"
    )
    email_image_Label.place(x=80, y=245)

    email_text = Label(
        email_image_Label,
        text="Email ID:",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    email_text.place(x=25, y=0)

    email_entry = Entry(
        email_image_Label,
        bd=0,
        bg="#3D404B",
        fg = "white",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    email_entry.place(x=8, y=17, width=354, height=27)

    # ================ Contact Number Section ====================
    contact_image = PhotoImage(file="assets\\input_img.png")
    contact_image_Label = Label(
        bg_image,
        image=contact_image,
        bg="#272A37"
    )
    contact_image_Label.place(x=80, y=315)

    contact_text = Label(
        contact_image_Label,
        text="Contact Number:",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    contact_text.place(x=25, y=0)

    contact_entry = Entry(
        contact_image_Label,
        bd=0,
        bg="#3D404B",
        fg = "white",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    contact_entry.place(x=8, y=17, width=354, height=27)

    # ================ TAN Number Section ====================
    tan_image = PhotoImage(file="assets\\input_img.png")
    tan_image_Label = Label(
        bg_image,
        image=tan_image,
        bg="#272A37"
    )
    tan_image_Label.place(x=350, y=315)

    tan_text = Label(
        tan_image_Label,
        text="University registration No:",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    tan_text.place(x=25, y=0)

    tan_entry = Entry(
        tan_image_Label,
        bd=0,
        bg="#3D404B",
        fg = "white",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    tan_entry.place(x=8, y=17, width=354, height=27)

    # ================ Password Name Section ====================
    password_image = PhotoImage(file="assets\\input_img.png")
    password_image_Label = Label(
        bg_image,
        image=password_image,
        bg="#272A37"
    )
    password_image_Label.place(x=80, y=385)

    password_text = Label(
        password_image_Label,
        text="Email Password:",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    password_text.place(x=25, y=0)

    password_entry = Entry(
        password_image_Label,
        bd=0,
        bg="#3D404B",
        fg = "white",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    password_entry.place(x=8, y=17, width=354, height=27)

    # =============== Submit Button ====================
    submit_buttonImage = PhotoImage(file="assets\\button_1.png")
    submit_button = Button(
        bg_image,
        image=submit_buttonImage,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=submit_form
    )
    submit_button.place(x=130, y=460, width=333, height=65)


    # =============== Back Button ====================
    back_button = Button(
        bg_image,
        text="Back to login page",
        bg="#3D404B",
        fg="#FFFFFF",
        font=("yu gothic ui", 12),
        borderwidth=0,
        highlightthickness=0, 
        activebackground="#272A37",
        cursor="hand2",
        command= load_login_page
    )
    back_button.place(x=210, y=535, width=160, height=30)


    # ================ Header Text Down ====================
    headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
    headerText_image_label3 = Label(
        bg_image,
        image=headerText_image_down,
        bg="#272A37"
    )
    headerText_image_label3.place(x=650, y=530)

    headerText3 = Label(
        bg_image,
        text="Powered by EduVault",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    headerText3.place(x=700, y=530)

    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    load_register()