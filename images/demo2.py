import tkinter as tk

def main():
    root = tk.Tk()
    root.title("EduVault")
    root.configure(bg='#1e1e1e')  # Greyish black color
    
    # Add the image
    image = tk.PhotoImage(file="images//hyy.png")
    image_label = tk.Label(root, image=image, bg='#1e1e1e')
    image_label.image = image  # Keep a reference to the image
    image_label.pack(side="top", anchor="nw", padx=10, pady=10)  # Adjust padx and pady as needed
    
    # Add buttons
    button_frame = tk.Frame(root, bg='#1e1e1e')
    button_frame.pack(side='top', anchor='nw', padx=10, pady=(0, 10))

    view_profile_button = tk.Button(button_frame, text="View Profile", bg='white', fg='#1e1e1e', font=('Helvetica', 12))
    view_profile_button.pack(side='left', padx=(0, 10))

    update_profile_button = tk.Button(button_frame, text="Update Profile", bg='white', fg='#1e1e1e', font=('Helvetica', 12))
    update_profile_button.pack(side='left', padx=(0, 10))

    delete_account_button = tk.Button(button_frame, text="Delete Account", bg='white', fg='#1e1e1e', font=('Helvetica', 12))
    delete_account_button.pack(side='left', padx=(0, 10))

    # Create a frame for file rows
    file_frame = tk.Frame(root, bg='#1e1e1e')
    file_frame.pack(side='top', anchor='nw', padx=10, pady=(0, 10))

    # Create 15 rows
    for i in range(1, 11):
        # Serial Number label
        serial_label = tk.Label(file_frame, text=str(i), bg='#1e1e1e', fg='white')
        serial_label.grid(row=i, column=0, padx=(0, 10), pady=5)

        # File entry
        file_entry = tk.Entry(file_frame, bg='white')
        file_entry.grid(row=i, column=1, padx=10, pady=5)

        # Upload button
        upload_button = tk.Button(file_frame, text="Upload", bg='#333', fg='white', font=('Helvetica', 10))
        upload_button.grid(row=i, column=2, padx=10, pady=5)

        # Delete button
        delete_button = tk.Button(file_frame, text="Delete", bg='#333', fg='white', font=('Helvetica', 10))
        delete_button.grid(row=i, column=3, padx=10, pady=5)

        # View button
        view_button = tk.Button(file_frame, text="View", bg='#333', fg='white', font=('Helvetica', 10))
        view_button.grid(row=i, column=4, padx=10, pady=5)

        # Share button
        share_button = tk.Button(file_frame, text="Share", bg='#333', fg='white', font=('Helvetica', 10))
        share_button.grid(row=i, column=5, padx=10, pady=5)
    
    # Submit button
    submit_button = tk.Button(root, text="Submit", bg='#4682B4', fg='white', font=('Helvetica', 12))
    submit_button.pack(side='top', pady=10)

    # Create a frame for the footer
    footer_frame = tk.Frame(root, bg='#1e1e1e', pady=10)
    footer_frame.pack(side='bottom', fill='x', anchor='center')
    
    # Add the "EduVault" label to the footer frame
    footer_label = tk.Label(footer_frame, text="© 2024 EduVault All rights reserved.", fg="white", bg='#1e1e1e', font=('Helvetica', 16))
    footer_label.pack()

    root.geometry("1166x600")  # Set window size
    root.mainloop()

if __name__ == "__main__":
    main()
