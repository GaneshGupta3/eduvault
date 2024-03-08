import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()

# Set the background color to black
root.configure(bg="black")

# Set the size of the window
root.geometry("1166x600")

# Function to fetch user information from the database (placeholder)
def fetch_user_info():
    # Placeholder function to fetch user information from the database
    # Replace this with your actual database retrieval logic
    user_info = {
        "First Name": "John",
        "Last Name": "Doe",
        "Email": "john@example.com",
        "Aadhar Number": "123456789012",
        "Contact Number": "9876543210"
    }
    return user_info

def open_profile_window():
    user_info = fetch_user_info()

    # Create a new window for the profile
    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")
    profile_window.geometry("400x300")

    # Display user information in labels
    for i, (key, value) in enumerate(user_info.items()):
        label = tk.Label(profile_window, text=f"{key}: {value}")
        label.pack(anchor="w", padx=10, pady=5)

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

# Rest of your code remains unchanged

# Create a Button widget for "View Profile"
view_profile_button = tk.Button(root, text="View Profile", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                cursor='hand2', activebackground='#3047ff', fg='white', command=open_profile_window)
view_profile_button.pack(anchor="w", padx=10, pady=(20, 20))

# Run the Tkinter event loop
root.mainloop()


import tkinter as tk
from PIL import Image, ImageTk

# Function to fetch student name from the database (placeholder)
def fetch_student_name():
    # Placeholder code to fetch student's name from the database
    return "Shivam Prajapati"  # Replace this with actual retrieval logic from your database

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
image_path = "images/hyy.png"
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

# Create a Button widget for LOGIN
login_button = tk.Button(root, text="View Profile", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                         cursor='hand2', activebackground='#3047ff', fg='white')
login_button.pack(anchor="w", padx=10, pady=(20, 10))

# Create Button widgets for View Document, Share Document, and Change Password
view_document_button = tk.Button(root, text="View Document", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                 cursor='hand2', activebackground='#3047ff', fg='white')
view_document_button.pack(anchor="w", padx=10, pady=(10, 10))

share_document_button = tk.Button(root, text="Share Document", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                  cursor='hand2', activebackground='#3047ff', fg='white')
share_document_button.pack(anchor="w", padx=10, pady=(10, 10))

change_password_button = tk.Button(root, text="Change Password", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                   cursor='hand2', activebackground='#3047ff', fg='white')
change_password_button.pack(anchor="w", padx=10, pady=(10, 10))

# Create a label for the footer
footer_label = tk.Label(root, text="© 2024 EduVault. All rights reserved.", fg="white", bg="black", font=("Arial", 12))
footer_label.pack(side="bottom", pady=10)

# Run the Tkinter event loop
root.mainloop()