import tkinter as tk
from tkinter import messagebox
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


    

def validate_student_name():
    student_name = student_name_entry.get()
    if len(student_name) < 1:
        def open_profile_window():
            user_info = fetch_user_info()

    # Create a new window for the profile with increased size
    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")
    profile_window.geometry("500x500")  # Increased size

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

    # Create a label for the greeting
    greeting_label = tk.Label(profile_window, text=f"Welcome {student_name} !", fg="white", bg="#525561", font=("times New roman", 20))
    greeting_label.pack(anchor="w", padx=10, pady=10)

    # Display user information in labels with spacing between lines
    for key, value in user_info.items():
        label = tk.Label(profile_window, text=f"{key}: {value}", bg="#525561", fg="white", font=("Arial", 12))
        label.pack(anchor="w", padx=10, pady=(5, 0))  # Add vertical spacing between lines

    # ================ Header Text Down ====================
    headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
    headerText_image_label3 = Label(
        profile_window,  # Changed to profile_window instead of bg_image
        image=headerText_image_down,
        bg="#272A37"
    )
    headerText_image_label3.place(x=5, y=10)

    headerText3 = Label(
        profile_window,  # Changed to profile_window instead of bg_image
        text="Powered by EduVault",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    headerText3.place(x=700, y=530)

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

# Run the Tkinter event loop
root.mainloop()