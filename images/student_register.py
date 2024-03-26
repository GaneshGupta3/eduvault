from tkinter import *
from tkinter import messagebox















from tkcalendar import DateEntry
import datetime
from password import passFunc
from uidGenerator import uid
from dbConnection import *
from storage_quota import *



def checkStudent(aadhaar_number):
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    sql_query = "SELECT * FROM student WHERE aadhaar_number = %s"
    cursor.execute(sql_query, (aadhaar_number,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False
        
        

def studentInsert(uid,full_name, email, dob_value, gender, contact_no, aadhaar_no, password):
    
    dbobj = db()
    mydb,cursor = dbobj.dbconnect("credentials")
    
     # Insert data into the login table
    login_query = "INSERT INTO login (uid,`key`, hash) VALUES (%s, %s, %s)"
    # For simplicity, assuming 'key' is the username and 'hash' is the password hash
    login_data = (uid, "key", password)  # Replace 'password_hash' with the actual hashed password
    cursor.execute(login_query, login_data)
    
    
    # Insert data into the student table
    student_query = "INSERT INTO student (uid, name, gender, dob, phone, email, aadhaar_number,suspended) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    student_data = (uid, full_name, gender, dob_value, contact_no, email, aadhaar_no,0)
    cursor.execute(student_query, student_data)
    
   
    
     # Commit changes and close the connection
    mydb.commit()
    mydb.close()
    
    userID = uid
    successMessage =f"Registration Successful. Your User ID is {userID}"
    messagebox.showinfo("Success",successMessage)
    
    
    
def saveinfo():
        # Get all the user inputs
    #         first_name = firstName_entry.get()
    # last_name = lastName_entry.get()
    # email = emailName_entry.get()
    # aadhar_number = aadhar_entry.get()
    # contact_number = contact_entry.get()
    
    
        full_name = firstName_entry.get()+lastName_entry.get()
        email = emailName_entry.get()
        dob_value = "31/01/2004"
        gender = "Male" #if var.get() == 1 else "Female"
        contact_number = contact_entry.get()
        aadhaar_number = aadhar_entry.get()
        password = confirm_passwordName_entry.get()
        
        uidobj = uid(aadhaar_number,1)
        generated_uid = uidobj.generate_unique_12_digit_number()
        passFuncobj = passFunc("key",password,password)
        boiledPass = passFuncobj.generateBoilpass()
        if not (checkStudent(aadhaar_number)):
            studentInsert(generated_uid,full_name, email, dob_value, gender, contact_number, aadhaar_number, boiledPass)
            storageobj = StorageQuota(generated_uid)
            storageobj.initialise_storage_quota()
        else:
            messagebox.showerror("User Already Exists", f"The Aadhaar number '{aadhaar_number}' is already registered")


def studentSignup():
    saveinfo()










def validate_aadhar_number():
    aadhar_number = aadhar_entry.get()
    if len(aadhar_number) != 12 or not aadhar_number.isdigit():
        return False
    return True

def validate_contact_number():
    contact_number = contact_entry.get()
    if len(contact_number) != 10 or not contact_number.isdigit():
        return False
    return True

def validate_email():
    email = emailName_entry.get()
    if not email.endswith('.com'):
        return False
    return True

def submit_form():
    if not validate_aadhar_number():
        messagebox.showerror("Error", "Please enter a proper Aadhar number!")
        return
    if not validate_contact_number():
        messagebox.showerror("Error", "Please enter a proper Contact number!")
        return
    if not validate_email():
        messagebox.showerror("Error", "Please enter a valid Email ID ending with '.com'!")
        return
    
    # Get user input data
    first_name = firstName_entry.get()
    last_name = lastName_entry.get()
    email = emailName_entry.get()
    aadhar_number = aadhar_entry.get()
    contact_number = contact_entry.get()
    
    # Display success message with user input data
    message = f"The Account has been Successfully Created!\n\n"
    message += f"First Name: {first_name}\n"
    message += f"Last Name: {last_name}\n"
    message += f"Email ID: {email}\n"
    message += f"Aadhar Number: {aadhar_number}\n"
    message += f"Contact Number: {contact_number}"
    
    messagebox.showinfo("Success", message)
    studentSignup()

window = Tk()

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
    text="Create Student Account",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
createAccount_header.place(x=75, y=100)

# ================ First Name Section ====================
firstName_image = PhotoImage(file="assets\\input_img.png")
firstName_image_Label = Label(
    bg_image,
    image=firstName_image,
    bg="#272A37"
)
firstName_image_Label.place(x=80, y=202)

firstName_text = Label(
    firstName_image_Label,
    text="First name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
firstName_text.place(x=25, y=0)

firstName_icon = PhotoImage(file="assets\\name_icon.png")
firstName_icon_Label = Label(
    firstName_image_Label,
    image=firstName_icon,
    bg="#3D404B"
)
firstName_icon_Label.place(x=159, y=15)

firstName_entry = Entry(
    firstName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
firstName_entry.place(x=8, y=17, width=140, height=27)

# ================ Last Name Section ====================
lastName_image = PhotoImage(file="assets\\input_img.png")
lastName_image_Label = Label(
    bg_image,
    image=lastName_image,
    bg="#272A37"
)
lastName_image_Label.place(x=293, y=202)

lastName_text = Label(
    lastName_image_Label,
    text="Last name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
lastName_text.place(x=25, y=0)

lastName_icon = PhotoImage(file="assets\\name_icon.png")
lastName_icon_Label = Label(
    lastName_image_Label,
    image=lastName_icon,
    bg="#3D404B"
)
lastName_icon_Label.place(x=159, y=15)

lastName_entry = Entry(
    lastName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
lastName_entry.place(x=8, y=17, width=140, height=27)

# ================ Email Name Section ====================
emailName_image = PhotoImage(file="assets\\email.png")
emailName_image_Label = Label(
    bg_image,
    image=emailName_image,
    bg="#272A37"
)
emailName_image_Label.place(x=80, y=271)

emailName_text = Label(
    emailName_image_Label,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
emailName_text.place(x=25, y=0)

emailName_icon = PhotoImage(file="assets\\email-icon.png")
emailName_icon_Label = Label(
    emailName_image_Label,
    image=emailName_icon,
    bg="#3D404B"
)
emailName_icon_Label.place(x=370, y=15)

emailName_entry = Entry(
    emailName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
emailName_entry.place(x=8, y=17, width=354, height=27)

# ================ Password Name Section ====================
passwordName_image = PhotoImage(file="assets\\input_img.png")
passwordName_image_Label = Label(
    bg_image,
    image=passwordName_image,
    bg="#272A37"
)
passwordName_image_Label.place(x=80, y=341)

passwordName_text = Label(
    passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
passwordName_text.place(x=25, y=0)

passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
passwordName_icon_Label = Label(
    passwordName_image_Label,
    image=passwordName_icon,
    bg="#3D404B"
)
passwordName_icon_Label.place(x=159, y=15)

passwordName_entry = Entry(
    passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
passwordName_entry.place(x=8, y=17, width=140, height=27)

# ================ Confirm Password Name Section ====================
confirm_passwordName_image = PhotoImage(file="assets\\input_img.png")
confirm_passwordName_image_Label = Label(
    bg_image,
    image=confirm_passwordName_image,
    bg="#272A37"
)
confirm_passwordName_image_Label.place(x=293, y=341)

confirm_passwordName_text = Label(
    confirm_passwordName_image_Label,
    text="Confirm Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
confirm_passwordName_text.place(x=25, y=0)

confirm_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
confirm_passwordName_icon_Label = Label(
    confirm_passwordName_image_Label,
    image=confirm_passwordName_icon,
    bg="#3D404B"
)
confirm_passwordName_icon_Label.place(x=159, y=15)

confirm_passwordName_entry = Entry(
    confirm_passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

# ================ Aadhar Number Section ====================
aadhar_image = PhotoImage(file="assets\\input_img.png")
aadhar_image_Label = Label(
    bg_image,
    image=aadhar_image,
    bg="#272A37"
)
aadhar_image_Label.place(x=80, y=410)

aadhar_text = Label(
    aadhar_image_Label,
    text="Aadhar Number",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
aadhar_text.place(x=25, y=0)

aadhar_icon = PhotoImage(file="assets\\name_icon.png")
aadhar_icon_Label = Label(
    aadhar_image_Label,
    image=aadhar_icon,
    bg="#3D404B"
)
aadhar_icon_Label.place(x=159, y=15)

aadhar_entry = Entry(
    aadhar_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
aadhar_entry.place(x=8, y=17, width=140, height=27)

# ================ Contact Number Section ====================
contact_image = PhotoImage(file="assets\\input_img.png")
contact_image_Label = Label(
    bg_image,
    image=contact_image,
    bg="#272A37"
)
contact_image_Label.place(x=293, y=410)

contact_text = Label(
    contact_image_Label,
    text="Contact Number",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
contact_text.place(x=25, y=0)

contact_icon = PhotoImage(file="assets\\name_icon.png")
contact_icon_Label = Label(
    contact_image_Label,
    image=contact_icon,
    bg="#3D404B"
)
contact_icon_Label.place(x=159, y=15)

contact_entry = Entry(
    contact_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
contact_entry.place(x=8, y=17, width=140, height=27)

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
submit_button.place(x=130, y=480, width=333, height=65)



# =============== Back Button ====================
back_button = Button(
    bg_image,
    text="Back",
    bg="#3D404B",
    fg="#FFFFFF",
    font=("yu gothic ui", 12),
    borderwidth=0,
    highlightthickness=0, 
    activebackground="#272A37",
    cursor="hand2"
)
back_button.place(x=210, y=555, width=160, height=30)




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

def student_register():
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    student_register()