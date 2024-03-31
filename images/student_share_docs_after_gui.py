import tkinter as tk
from tkinter import messagebox
from file_operations_interface import *
def submit(fileids,userid,institute_id,validity_days):
    # Check if both fields are filled
    if institute_id and validity_days:
        # Check if validity days is a positive integer
        try:
            validity_days = int(validity_days)
            if validity_days > 0:
                messagebox.showinfo("sharing Successful", f"Institute ID: {institute_id}\nValidity Days: {validity_days}\nfile ids:{fileids}\nuser id:{userid}")
                for fileid in fileids :
                    grant_file_access(fileid,userid,institute_id,validity_days)
            else:
                messagebox.showerror("Invalid Input", "Validity days must be a positive integer.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Validity days must be a positive integer.")
    else:
        messagebox.showerror("Missing Information", "Please fill in both fields.")

# Create main window
def open_student_share_docs_after_gui(fileids,userid):
    root = tk.Tk()
    root.title("Institute Information")
    root.geometry("300x150")

    # Create labels
    institute_id_label = tk.Label(root, text="Institute ID:")
    institute_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    validity_days_label = tk.Label(root, text="Validity Days:")
    validity_days_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    # Create entry fields
    institute_id_entry = tk.Entry(root)
    institute_id_entry.grid(row=0, column=1, padx=10, pady=5)

    validity_days_entry = tk.Entry(root)
    validity_days_entry.grid(row=1, column=1, padx=10, pady=5)

    # Create submit button
    def beforesubmit():
        institute_id = institute_id_entry.get()
        validity_days = validity_days_entry.get()
        submit(fileids,userid,institute_id,validity_days)
    submit_button = tk.Button(root, text="share", command=beforesubmit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Run the application
    root.mainloop()

if __name__ == '__main__':
    open_student_share_docs_after_gui([18,19],"S353356847444")