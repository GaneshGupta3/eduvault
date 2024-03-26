import tkinter as tk
from PIL import Image, ImageTk




from current_user_info import *
from dbConnection import *





def main(user_id):
    currentuser = currentUserInfo(user_id,"S")
# Function to fetch student name from the database (placeholder)
    def fetch_student_name():
    # Placeholder code to fetch student's name from the database
        return currentuser.name  # Replace this with actual retrieval logic from your database

# Function to fetch user information from the database (placeholder)
    def fetch_user_info():
    # Placeholder function to fetch user information from the database
    # Replace this with your actual database retrieval logic
        
        user_info = {
        "Name": currentuser.name ,
        "Email": currentuser.email,
        "Contact Number": currentuser.phone
        }
        return user_info

    def open_profile_window():
        user_info = fetch_user_info()

    # Create a new window for the profile with increased size
        profile_window = tk.Toplevel(root)
        profile_window.title("Profile")
        profile_window.geometry("800x400")  # Increased size

    # Set background color
        profile_window.configure(bg="#272A37")

    # Load the background image
        bg_image = Image.open("assets//image_1.png")
        bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label for the background image
        bg_label = tk.Label(profile_window, image=bg_photo, bg="#272A37")
        bg_label.image = bg_photo  # Retain a reference to avoid garbage collection
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Fetch student's name from the database
        student_name = currentuser.name

    # Load the header text image
        header_text_image = Image.open("assets//headerText_image.png")
        header_text_photo = ImageTk.PhotoImage(header_text_image)

        # Create a frame to hold the image and greeting label
        header_frame = tk.Frame(profile_window, bg="#272A37")
        header_frame.pack(anchor="w", padx=10, pady=10)

    # Create a label for the header text image
        header_text_label = tk.Label(header_frame, image=header_text_photo, bg="#272A37")
        header_text_label.image = header_text_photo  # Retain a reference to avoid garbage collection
        header_text_label.pack(side="left")

    # Create a label for the greeting
        greeting_label = tk.Label(header_frame, text=f"Welcome {student_name} !", fg="white", bg="#272A37", font=("yu gothic ui bold", 20))
        greeting_label.pack(side="left", padx=(10, 0), pady=(0, 10))

    # Display user information in labels with spacing between lines
        for key, value in user_info.items():
            label = tk.Label(profile_window, text=f"{key}: {value}\n", bg="#272A37", fg="white", font=("yu gothic ui bold", 14))
            label.pack(anchor="w", padx=10, pady=(0, 10))  # Add vertical spacing between lines

    def open_share_documents_window():
        share_documents_window = tk.Toplevel(root)
        share_documents_window.title("Share Documents")
        share_documents_window.geometry("900x600")

        background_image = Image.open("images/background2.png")
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(share_documents_window, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    
        frame = tk.Frame(share_documents_window, bg="#B6B6B4")
        frame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.6, anchor="n")

    # Load the header text image
        header_text_image = Image.open("assets//headerText_image.png")
        header_text_photo = ImageTk.PhotoImage(header_text_image)

    # Create a frame to hold the image and welcome label
        header_frame = tk.Frame(share_documents_window, bg="#B6B6B4")
        header_frame.pack(anchor="w", padx=10, pady=10)

    # Create a label for the header text image
        header_text_label = tk.Label(header_frame, image=header_text_photo, bg="#B6B6B4")
        header_text_label.image = header_text_photo  # Retain a reference to avoid garbage collection
        header_text_label.pack(side="left")

    # Create a label for the welcome message
        welcome_label = tk.Label(header_frame, text="Welcome to Share Documents!", fg="#002244", bg="#B6B6B4", font=("yu gothic ui", 20))
        welcome_label.pack(side="left", padx=(10, 0))

    # Add column names
        column_names_frame = tk.Frame(share_documents_window, bg="#B6B6B4")
        column_names_frame.place(relx=0.05, rely=0.15, relwidth=0.9)

        doc_name_column_label = tk.Label(column_names_frame, text="\nDOCUMENT NAMES\t", fg="#002244", bg="#B6B6B4", font=("yu gothic ui", 14, "bold"))
        doc_name_column_label.grid(row=0, column=0, padx=(0, 50))

        doc_size_column_label = tk.Label(column_names_frame, text="\n\tSIZE", fg="#002244", bg="#B6B6B4", font=("yu gothic ui", 14, "bold"))
        doc_size_column_label.grid(row=0, column=5, padx=(0, 50))

    # Dummy data for demonstration
        documents_data = [
        {"name": "Document1.pdf", "size": "1.2 MB"},
        {"name": "Document2.docx", "size": "800 KB"},
        {"name": "Document3.jpg", "size": "500 KB"}
    ]
    
    # List to store checkbox variables
        checkbox_vars = []

    # Create labels and checkboxes for each document with name, size, and a view button
        for index, doc_data in enumerate(documents_data, start=1):
        # Create a checkbox variable for each document
            checkbox_var = tk.IntVar()
            checkbox_vars.append(checkbox_var)
        
        # Create checkbox with larger size
            checkbox = tk.Checkbutton(share_documents_window, variable=checkbox_var, bg="#B6B6B4", activebackground="#B6B6B4", height=2, width=5)
            checkbox.place(relx=0.05, rely=0.3 + index * 0.1)
        
            doc_name_label = tk.Label(share_documents_window, text=doc_data["name"], fg="#002244", bg="#B6B6B4", font=("yu gothic ui", 14,"bold"))
            doc_name_label.place(relx=0.1, rely=0.3 + index * 0.1)

            doc_size_label = tk.Label(share_documents_window, text=doc_data["size"], fg="#002244", bg="#B6B6B4", font=("yu gothic ui", 14,"bold"))
            doc_size_label.place(relx=0.5, rely=0.3 + index * 0.1)

            view_button = tk.Button(share_documents_window, text="View", font=("yu gothic ui", 14, "bold"), bd=0, bg='#3047ff',
                                    cursor='hand2', activebackground='#3047ff', fg='white')
            view_button.place(relx=0.8, rely=0.3 + index * 0.1)

    # Add a Share button
        share_button = tk.Button(share_documents_window, text="Share", font=("yu gothic ui", 14, "bold"), bd=0, bg='#000042',
                              cursor='hand2', activebackground='#7B68EE', fg='white')
        share_button.place(relx=0.3, rely=0.9)

    # Add a back button
        back_button = tk.Button(share_documents_window, text="Back", font=("yu gothic ui", 14, "bold"), bd=0, bg='#000042',
                            cursor='hand2', activebackground='#3047ff', fg='white', command=share_documents_window.destroy)
        back_button.place(relx=0.6, rely=0.9)
    
    # Add a note message
        note_label = tk.Label(share_documents_window, text="Note: The documents selected by checkbox will be shared", fg="#002244", bg="#B6B6B4", font=("yu gothic ui", 12,"bold"))
        note_label.place(relx=0.05, rely=0.8)


    def open_document_window():
        document_window = tk.Toplevel(root)
        document_window.title("View Documents")
        document_window.geometry("800x500")

        background_image = Image.open("images/background1.png")
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(document_window, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = tk.Frame(document_window, bg="#B6B6B4")
        frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor="n")
    
    # Add image to the header line
        email_icon_image = Image.open("assets//headerText_image.png")
        email_icon_photo = ImageTk.PhotoImage(email_icon_image)

        header_frame = tk.Frame(document_window, bg="#002244")
        header_frame.pack(fill="x")

        email_icon_label = tk.Label(header_frame, image=email_icon_photo, bg="#002244")
        email_icon_label.image = email_icon_photo
        email_icon_label.pack(side="left", padx=(10, 5))

        header_label = tk.Label(header_frame, text="Your Documents!", fg="white", bg="#002244", font=("yu gothic ui bold", 22))
        header_label.pack(side="left", padx=(0, 10), pady=10)
 
        personal_label = tk.Label(frame, text="Personal Documents:", fg="black", bg="#B6B6B4", font=("yu gothic ui bold", 18))
        personal_label.grid(row=0, column=0, padx=10, pady=10)

        view_personal_button = tk.Button(frame, text="View", bg="#3047ff", fg="white", font=("Arial", 14), command=view_personal_docs)
        view_personal_button.grid(row=0, column=1, padx=10, pady=10)

        marksheets_label = tk.Label(frame, text="Marksheets:", fg="black", bg="#B6B6B4", font=("yu gothic ui bold", 18))
        marksheets_label.grid(row=1, column=0, padx=10, pady=10)
 
        view_marksheets_button = tk.Button(frame, text="View", bg="#3047ff", fg="white", font=("Arial", 14), command=view_marksheets)
        view_marksheets_button.grid(row=1, column=1, padx=10, pady=10)
 
        certificates_label = tk.Label(frame, text="Certificates:", fg="black", bg="#B6B6B4", font=("yu gothic ui bold", 18))
        certificates_label.grid(row=2, column=0, padx=10, pady=10)

        view_certificates_button = tk.Button(frame, text="View", bg="#3047ff", fg="white", font=("Arial", 14), command=view_certificates)
        view_certificates_button.grid(row=2, column=1, padx=10, pady=10)

    def view_personal_docs():
         print("View Personal Documents")

    def view_marksheets():
         print("View Marksheets")

    def view_certificates():
         print("View Certificates")


# Create the main window
    root = tk.Tk()
    root.geometry("1166x600")
    root.configure(bg="black")

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

    view_profile_button = tk.Button(root, text="View Profile", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                cursor='hand2', activebackground='#3047ff', fg='white', command=open_profile_window)
    view_profile_button.pack(anchor="w", padx=10, pady=(20, 40))

    view_document_button = tk.Button(root, text="View Document", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                 cursor='hand2', activebackground='#3047ff', fg='white', command=open_document_window)
    view_document_button.pack(anchor="w", padx=10, pady=(10, 40))

    share_document_button = tk.Button(root, text="Share Document", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                  cursor='hand2', activebackground='#3047ff', fg='white', command=open_share_documents_window)
    share_document_button.pack(anchor="w", padx=10, pady=(10, 40))

    change_password_button = tk.Button(root, text="Change Password", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                   cursor='hand2', activebackground='#3047ff', fg='white')
    change_password_button.pack(anchor="w", padx=10, pady=(10, 40))

    root.mainloop()
if __name__ =='__main__':
    main()