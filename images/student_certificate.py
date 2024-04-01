# import tkinter as tk
# from tkinter import messagebox
# import time
# from fetch_documents_list import *
# from file_operations_interface import *

# # set value of n (no of pending approvals)
# global n
# n = 6

# class Example(tk.LabelFrame):
#     def __init__(self, user_id, category, *args, **kwargs):
#         document_list = fetch_documents(user_id, category)
#         print(document_list)
#         tk.LabelFrame.__init__(self, *args, **kwargs)

#         data = [
#             [document_list[0][1], document_list[0][4] / 1000, document_list[0][0]],
#             [document_list[1][1], document_list[1][4] / 1000, document_list[1][0]],
#             [document_list[2][1], document_list[2][4] / 1000, document_list[2][0]],
#             [document_list[3][1], document_list[3][4] / 1000, document_list[3][0]],
#             [document_list[4][1], document_list[4][4] / 1000, document_list[4][0]],
#             [document_list[5][1], document_list[5][4] / 1000, document_list[5][0]]
#         ]

#         self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
#         self.grid_columnconfigure(1, weight=1)

#         tk.Label(self,
#                  text="Certificate Name",
#                  fg="#FFFFFF",
#                  padx=30,
#                  font=("yu gothic ui bold", 20 * -1),
#                  bg="#272A37").grid(row=0, column=0, sticky="ew")

#         tk.Label(self,
#                  text="Size (in kb)",
#                  padx=30,
#                  fg="#FFFFFF",
#                  font=("yu gothic ui bold", 20 * -1),
#                  bg="#272A37").grid(row=0, column=1, sticky="ew")

#         tk.Label(self,
#                  text="  View  ",
#                  fg="#FFFFFF",
#                  font=("yu gothic ui bold", 20 * -1),
#                  bg="#272A37").grid(row=0, column=3, sticky="ew")

#         tk.Label(self,
#                  text="  Delete ",
#                  fg="#FFFFFF",
#                  font=("yu gothic ui bold", 20 * -1),
#                  bg="#272A37").grid(row=0, column=4, sticky="ew")

#         row = 1

#         for (nr, name, file_id) in data:

#             nr_label = tk.Label(self, text=str(nr),
#                                 fg="#FFFFFF",
#                                 font=("yu gothic ui bold", 20 * -1),
#                                 bg="#272A37")

#             name_label = tk.Label(self,
#                                    text=str(name),
#                                    fg="#FFFFFF",
#                                    font=("yu gothic ui bold", 20 * -1),
#                                    bg="#272A37")

#             buttonImage1 = tk.PhotoImage(file="assets\\approval_view.png")
#             action_button1 = tk.Button(self,
#                                        image=buttonImage1,
#                                        borderwidth=0,
#                                        highlightthickness=0,
#                                        relief="flat",
#                                        activebackground="#272A37",
#                                        cursor="hand2",
#                                        command=lambda uid=user_id, fid=file_id: self.view_certificate(uid, fid))

#             action_button1.image = buttonImage1

#             buttonImage2 = tk.PhotoImage(file="assets\\delete.png")
#             action_button2 = tk.Button(self,
#                                        image=buttonImage2,
#                                        borderwidth=0,
#                                        highlightthickness=0,
#                                        relief="flat",
#                                        activebackground="#272A37",
#                                        cursor="hand2",
#                                        command=lambda uid=user_id, fid=file_id: self.delete_certificate(uid, fid))

#             action_button2.image = buttonImage2

#             nr_label.grid(row=row, column=0, sticky="ew")
#             name_label.grid(row=row, column=1, sticky="ew")

#             action_button1.grid(row=row, column=3, sticky="ew")
#             action_button2.grid(row=row, column=4, sticky="ew")

#             row += 1

#     def view_certificate(self, user_id, file_id):
#         # Add functionality to view the certificate using user_id and file_id
#         retrieve_file(user_id, file_id)

#     def delete_certificate(self, user_id, file_id):
#         # Add functionality to delete the certificate using user_id and file_id
#         print("Deleting certificate with User ID:", user_id, "and File ID:", file_id)

# def open_certificates(user_id, category):
#     root = tk.Tk()
#     root.title("Certificate page")
#     height = (n) * 42 + 35
#     width = 1240
#     x = (root.winfo_screenwidth() // 2) - (width // 2)
#     y = (root.winfo_screenheight() // 4) - (height // 4)
#     root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     root.configure(bg="#525561")
#     Example(user_id, category, root).pack(side="top", fill="both", expand=True, padx=10, pady=10)
#     root.mainloop()

# if __name__ == "__main__":
#     open_certificates("S353356847444", "Certificates")


import tkinter as tk
from tkinter import messagebox
import time
from fetch_documents_list import *
from file_operations_interface import *

# set value of n (no of pending approvals)
# global n
# n = 6

class Example(tk.LabelFrame):
    def __init__(self, user_id, category, *args, **kwargs):
        document_list = fetch_documents(user_id, category)
        docs_count = count_documents(user_id,category)
        print(document_list)
        tk.LabelFrame.__init__(self, *args, **kwargs)

        # data = [
        #     [document_list[0][1], document_list[0][4] / 1000, document_list[0][0]],
        #     [document_list[1][1], document_list[1][4] / 1000, document_list[1][0]],
        #     [document_list[2][1], document_list[2][4] / 1000, document_list[2][0]],
        #     [document_list[3][1], document_list[3][4] / 1000, document_list[3][0]],
        #     [document_list[4][1], document_list[4][4] / 1000, document_list[4][0]],
        #     [document_list[5][1], document_list[5][4] / 1000, document_list[5][0]]
        # ]

        data = []

        for i in range(min(docs_count, len(document_list))):
            document = document_list[i]
            file_name = document[1]
            file_size_kb = document[4] / 1000
            file_id = document[0]
            data.append([
                file_name,
                file_size_kb,
                file_id
            ])

        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self,
                 text="Certificate Name",
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

        for (nr, name, file_id) in data:

            nr_label = tk.Label(self, text=str(nr),
                                fg="#FFFFFF",
                                font=("yu gothic ui bold", 20 * -1),
                                bg="#272A37")

            name_label = tk.Label(self,
                                   text=str(name),
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
                                       command=lambda uid=user_id, fid=file_id: self.view_certificate(uid, fid))

            action_button1.image = buttonImage1

            buttonImage2 = tk.PhotoImage(file="assets\\delete.png")
            action_button2 = tk.Button(self,
                                       image=buttonImage2,
                                       borderwidth=0,
                                       highlightthickness=0,
                                       relief="flat",
                                       activebackground="#272A37",
                                       cursor="hand2",
                                       command=lambda uid=user_id, fid=file_id: self.delete_certificate(uid, fid))

            action_button2.image = buttonImage2

            nr_label.grid(row=row, column=0, sticky="ew")
            name_label.grid(row=row, column=1, sticky="ew")

            action_button1.grid(row=row, column=3, sticky="ew")
            action_button2.grid(row=row, column=4, sticky="ew")

            row += 1

    def view_certificate(self, user_id, file_id):
        # Add functionality to view the certificate using user_id and file_id
        retrieve_file(user_id, file_id)

    def delete_certificate(self, user_id, file_id):
        # Add functionality to delete the certificate using user_id and file_id
        print("Deleting certificate with User ID:", user_id, "and File ID:", file_id)

def open_certificates(user_id, category):
    root = tk.Tk()
    root.title("Certificate page")
    docs_count = count_documents(user_id,category)
    height = (docs_count) * 42 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.configure(bg="#525561")
    Example(user_id, category, root).pack(side="top", fill="both", expand=True, padx=10, pady=10)
    root.mainloop()

if __name__ == "__main__":
    open_certificates("S353356847444", "Certificates")