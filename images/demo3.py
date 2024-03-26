import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage, Entry, Label, Button
from PIL import Image, ImageTk

# Function to fetch student name from the database (placeholder)
def fetch_student_name():
    # Placeholder code to fetch student's name from the database
    return "Shivam Prajapati"  # Replace this with actual retrieval logic from your database

# Function to fetch user information from the database (placeholder)
def fetch_user_info():
    # Placeholder function to fetch user information from the database
    # Replace this with your actual database retrieval logic
    user_info = {
        "First Name": "Shivam",
        "Last Name": "Prajapati",
        "Email": "shivam@example.com",
        "Contact Number": "9876543210"
    }
    return user_info

def open_profile_window():
    user_info = fetch_user_info()

    # Create a new window for the profile with increased size
    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")
    profile_window.geometry("600x400")  # Increased size

    # Set background color
    profile_window.configure(bg="#525561")

    # Load the background image
    bg_image = Image.open("assets//image_1.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label for the background image
    bg_label = tk.Label(profile_window, image=bg_photo, bg="#525561")
    bg_label.image = bg_photo  # Retain a reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Fetch student's name from the database
    student_name = fetch_student_name()

    # Display user information in labels
    for key, value in user_info.items():
        label = tk.Label(profile_window, text=f"{key}: {value}", bg="#525561", fg="white", font=("Arial", 12))
        label.pack(anchor="w", padx=10, pady=5)

def validate_student_name():
    student_name = student_name_entry.get()
    if len(student_name) < 1:
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
    if not validate_student_name():
        messagebox.showerror("Error", "Please enter student Name!")
        return
    if not validate_email():
        messagebox.showerror("Error", "Please enter a valid Email ID ending with '.com'!")
        return
    if not validate_contact_number():
        messagebox.showerror("Error", "Please enter a proper Contact number!")
        return
    
    # Get user input data
    student_name = student_name_entry.get()
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

def update_profile():
    # Placeholder function to update the profile in the database
    # Replace this with your actual update logic
    messagebox.showinfo("Update Profile", "Profile Updated Successfully!")

# Create the main window
root = tk.Tk()

# Set the background color to black
root.configure(bg="black")

# Set the size of the window
root.geometry("1166x600")

# Create a frame for the image and greeting
frame = tk.Frame(root, bg="black")
frame.pack(anchor="nw", padx=10, pady=10)

# Load the image
image_path = "assets\\hyy.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label for the image
image_label = tk.Label(frame, image=photo, bg="black")
image_label.photo = photo  # Retain a reference to avoid garbage collection
image_label.pack(side="left")

# Fetch student's name from the database
student_name = fetch_student_name()

# Create a label for the greeting
greeting_label = tk.Label(frame, text=f"Hii {student_name} !", fg="white", bg="black", font=("times New roman", 20))
greeting_label.pack(side="left", padx=10)

# Create a Button widget for "View Profile"
view_profile_button = tk.Button(root, text="View Profile", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                cursor='hand2', activebackground='#3047ff', fg='white', command=open_profile_window)
view_profile_button.pack(anchor="w", padx=10, pady=(20, 40))

# Create Button widgets for View Document, Share Document, and Change Password
view_document_button = tk.Button(root, text="View Document", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                 cursor='hand2', activebackground='#3047ff', fg='white')
view_document_button.pack(anchor="w", padx=10, pady=(10, 40))

share_document_button = tk.Button(root, text="Share Document", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                  cursor='hand2', activebackground='#3047ff', fg='white')
share_document_button.pack(anchor="w", padx=10, pady=(10, 40))

change_password_button = tk.Button(root, text="Change Password", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                   cursor='hand2', activebackground='#3047ff', fg='white')
change_password_button.pack(anchor="w", padx=10, pady=(10, 40))

# Create an "Update Profile" button
update_profile_button = tk.Button(root, text="Update Profile", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                  cursor='hand2', activebackground='#3047ff', fg='white', command=update_profile)
update_profile_button.pack(anchor="w", padx=10, pady=(10, 20))

# Adding the provided UI components

# Create a window
window = tk.Tk()
window.title("Create Institute Account")
window.geometry("1240x650")

# Set the position of the window
height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#525561")

# Load the background image
backgroundImage = PhotoImage(file="assets\\image_1.png")
bg_image = Label(window, image=backgroundImage, bg="#525561")
bg_image.place(x=120, y=28)

# Header Text
headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label1 = Label(bg_image, image=headerText_image_left, bg="#272A37")
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(bg_image, text="Welcome !", fg="#FFFFFF", font=("yu gothic ui bold", 20), bg="#272A37")
headerText1.place(x=110, y=45)

# Create Account Header
createAccount_header = Label(bg_image, text="Create Institute Account", fg="#FFFFFF", font=("yu gothic ui Bold", 28), bg="#272A37")
createAccount_header.place(x=75, y=80)

# Institute Name Section
institute_name_image = PhotoImage(file="assets\\input_img.png")
institute_name_image_Label = Label(bg_image, image=institute_name_image, bg="#272A37")
institute_name_image_Label.place(x=80, y=175)

institute_name_text = Label(institute_name_image_Label, text="Institute Name:", fg="#FFFFFF", font=("yu gothic ui SemiBold", 13), bg="#3D404B")
institute_name_text.place(x=50, y=0)

institute_name_entry = Entry(institute_name_image_Label, bd=0, bg="#3D404B", highlightthickness=0, font=("yu gothic ui SemiBold", 16))
institute_name_entry.place(x=8, y=17, width=356, height=27)

# Email Section
email_image = PhotoImage(file="assets\\email.png")
email_image_Label = Label(bg_image, image=email_image, bg="#272A37")
email_image_Label.place(x=80, y=245)

email_text = Label(email_image_Label, text="Email ID:", fg="#FFFFFF", font=("yu gothic ui SemiBold", 13), bg="#3D404B")
email_text.place(x=25, y=0)

email_entry = Entry(email_image_Label, bd=0, bg="#3D404B", highlightthickness=0, font=("yu gothic ui SemiBold", 16))
email_entry.place(x=8, y=17, width=354, height=27)

# Contact Number Section
contact_image = PhotoImage(file="assets\\input_img.png")
contact_image_Label = Label(bg_image, image=contact_image, bg="#272A37")
contact_image_Label.place(x=80, y=315)

contact_text = Label(contact_image_Label, text="Contact Number:", fg="#FFFFFF", font=("yu gothic ui SemiBold", 13), bg="#3D404B")
contact_text.place(x=25, y=0)

contact_entry = Entry(contact_image_Label, bd=0, bg="#3D404B", highlightthickness=0, font=("yu gothic ui SemiBold", 16))
contact_entry.place(x=8, y=17, width=354, height=27)

# TAN Number Section
tan_image = PhotoImage(file="assets\\input_img.png")
tan_image_Label = Label(bg_image, image=tan_image, bg="#272A37")
tan_image_Label.place(x=350, y=315)

tan_text = Label(tan_image_Label, text="TAN Number:", fg="#FFFFFF", font=("yu gothic ui SemiBold", 13), bg="#3D404B")
tan_text.place(x=25, y=0)

tan_entry = Entry(tan_image_Label, bd=0, bg="#3D404B", highlightthickness=0, font=("yu gothic ui SemiBold", 16))
tan_entry.place(x=8, y=17, width=354, height=27)

# Password Name Section
password_image = PhotoImage(file="assets\\input_img.png")
password_image_Label = Label(bg_image, image=password_image, bg="#272A37")
password_image_Label.place(x=80, y=385)

password_text = Label(password_image_Label, text="Email Password:", fg="#FFFFFF", font=("yu gothic ui SemiBold", 13), bg="#3D404B")
password_text.place(x=25, y=0)

password_entry = Entry(password_image_Label, bd=0, bg="#3D404B", highlightthickness=0, font=("yu gothic ui SemiBold", 16))
password_entry.place(x=8, y=17, width=354, height=27)

# Submit Button
submit_buttonImage = PhotoImage(file="assets\\button_1.png")
submit_button = Button(bg_image, image=submit_buttonImage, borderwidth=0, highlightthickness=0, relief="flat", activebackground="#272A37", cursor="hand2", command=submit_form)
submit_button.place(x=130, y=460, width=333, height=65)

# Back Button
back_button = Button(bg_image, text="Back", bg="#3D404B", fg="#FFFFFF", font=("yu gothic ui", 12), borderwidth=0, highlightthickness=0, activebackground="#272A37", cursor="hand2")
back_button.place(x=210, y=535, width=160, height=30)

# Header Text Down
headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label3 = Label(bg_image, image=headerText_image_down, bg="#272A37")
headerText_image_label3.place(x=650, y=530)

headerText3 = Label(bg_image, text="Powered by EduVault", fg="#FFFFFF", font=("yu gothic ui bold", 20), bg="#272A37")
headerText3.place(x=700, y=530)

window.resizable(False, False)
window.mainloop()

