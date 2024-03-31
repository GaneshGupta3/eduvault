import tkinter as tk
from tkinter import messagebox
import time
from fetch_documents_list import *

# Set value of n (no of pending approvals)
global n
n = 6

class Example(tk.LabelFrame):
    def __init__(self, user_id, category, *args, **kwargs):
        document_list = fetch_documents(user_id, category)
        tk.LabelFrame.__init__(self, *args, **kwargs)

        self.documents = document_list[:n]  # Limiting to first n documents

        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self,
                 text="marksheet Name",
                 fg="#FFFFFF",
                 padx=30,
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=0, sticky="ew")

        tk.Label(self,
                 text="Size (in kb)",
                 padx=30,
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=1, sticky="ew")

        tk.Label(self,
                 text="  View  ",
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=3, sticky="ew")

        tk.Label(self,
                 text="  Delete ",
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=4, sticky="ew")

        row = 1

        for document in self.documents:
            document_name = document[1]
            document_size = document[4] / 1000  # Size in kb
            file_id = document[0]

            nr_label = tk.Label(self, text=str(document_name),
                                fg="#FFFFFF",
                                font=("yu gothic ui bold", 20 * -1),
                                bg="#272A37")

            size_label = tk.Label(self,
                                  text=str(document_size),
                                  fg="#FFFFFF",
                                  font=("yu gothic ui bold", 20 * -1),
                                  bg="#272A37")

            buttonImage1 = tk.PhotoImage(file="assets\\approval_view.png")
            action_button1 = tk.Button(self,
                                       image=buttonImage1,
                                       borderwidth=0,
                                       highlightthickness=0,
                                       relief="flat",
                                       activebackground="#272A37",
                                       cursor="hand2",
                                       command=lambda fid=file_id: self.view_document(user_id, fid))

            action_button1.image = buttonImage1

            buttonImage2 = tk.PhotoImage(file="assets\\delete.png")
            action_button2 = tk.Button(self,
                                       image=buttonImage2,
                                       borderwidth=0,
                                       highlightthickness=0,
                                       relief="flat",
                                       activebackground="#272A37",
                                       cursor="hand2",
                                       command=lambda fid=file_id: self.delete_document(user_id, fid))

            action_button2.image = buttonImage2

            nr_label.grid(row=row, column=0, sticky="ew")
            size_label.grid(row=row, column=1, sticky="ew")

            action_button1.grid(row=row, column=3, sticky="ew")
            action_button2.grid(row=row, column=4, sticky="ew")

            row += 1

    def view_document(self, user_id, file_id):
        # Implement view document functionality here
        retrieve_file(user_id, file_id)

    def delete_document(self, user_id, file_id):
        # Implement delete document functionality here
        print("Deleting document with user ID:", user_id, "and file ID:", file_id)

def open_marksheets(user_id, category):
    root = tk.Tk()
    root.title("Marksheet page")
    height = (n) * 42 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.configure(bg="#525561")

    Example(user_id, category, root).pack(side="top", fill="both", expand=True, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    open_marksheets("S353356847444", "Marksheets")
