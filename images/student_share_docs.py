import tkinter as tk
from tkinter import messagebox
import time
from fetch_documents_list import *
from file_operations_interface import *
from student_share_docs_after_gui import *
# set value of n (no of pending approvals)
global n
n = 6


class Example(tk.LabelFrame):
    def __init__(self, user_id, *args, **kwargs):
        document_list = fetch_documents_for_sharing(user_id)
        for documents in document_list:
            print(documents)

        tk.LabelFrame.__init__(self, *args, **kwargs)

        self.selected_documents = []

        data = [
            [document_list[0][1], document_list[0][4] / 1000, document_list[0][0]],
            [document_list[1][1], document_list[1][4] / 1000, document_list[1][0]],
            [document_list[2][1], document_list[2][4] / 1000, document_list[2][0]],
            [document_list[3][1], document_list[3][4] / 1000, document_list[3][0]],
            [document_list[4][1], document_list[4][4] / 1000, document_list[4][0]],
            [document_list[5][1], document_list[5][4] / 1000, document_list[5][0]]
        ]

        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self,
                 text="Document Name",
                 fg="#FFFFFF",
                 padx=30,
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=1, sticky="ew")

        tk.Label(self,
                 text="Size (in kb)",
                 padx=30,
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=2, sticky="ew")

        tk.Label(self,
                 text="  Share  ",
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=3, sticky="ew")

        tk.Label(self,
                 text=" ",
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=0, sticky="ew")
        


        buttonImage1 = tk.PhotoImage(file="assets\\share.png")
        self.action_button1 = tk.Button(self,
                                        image=buttonImage1,
                                        borderwidth=0,
                                        highlightthickness=0,
                                        relief="flat",
                                        activebackground="#272A37",
                                        cursor="hand2",
                                        command=lambda user_id=user_id: self.share_documents(user_id))
        self.action_button1.image = buttonImage1

        row = 1

        for (nr, name, document_id) in data:
            nr_label = tk.Label(self, text=str(nr),
                                fg="#FFFFFF",
                                font=("yu gothic ui bold", 20 * -1),
                                bg="#272A37")

            name_label = tk.Label(self,
                                  text=str(name),
                                  fg="#FFFFFF",
                                  font=("yu gothic ui bold", 20 * -1),
                                  bg="#272A37")
            

            tk.Label(self,
                    text=" ",
                    fg="#FFFFFF",
                    font=("yu gothic ui bold", 20 * -1),
                    bg="#272A37").grid(row=row-1, column=3, sticky="ew")


            self.selected_documents.append(tk.IntVar(value=0))
            C1 = tk.Checkbutton(self,
                                activebackground="#272A37",
                                activeforeground="#272A37",
                                bg="#272A37", bd=6,
                                variable=self.selected_documents[-1],
                                onvalue=document_id,
                                offvalue=0)

            nr_label.grid(row=row, column=1, sticky="ew")
            name_label.grid(row=row, column=2, sticky="ew")
            C1.grid(row=row, column=0, sticky="ew")

            row += 1

        self.action_button1.grid(row=n, column=3, sticky="ew")

    def share_documents(self,user_id):
        selected_ids = [var.get() for var in self.selected_documents if var.get() != 0]
        if selected_ids:
            messagebox.showinfo("Share Documents", f"Selected documents for sharing: {', '.join(map(str, selected_ids))}")
            open_student_share_docs_after_gui(selected_ids,user_id)
        else:
            messagebox.showwarning("Share Documents", "No documents selected for sharing.")


def open_student_share_docs(window,user_id):
    root = tk.Toplevel(window)
    root.title("student share docs")
    height = (n) * 39 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.configure(bg="#525561")
    Example(user_id, root).pack(side="top", fill="both", expand=True, padx=10, pady=10)
    root.mainloop()


if __name__ == "__main__":
    open_student_share_docs("S353356847444")

# import tkinter as tk

# from tkinter import messagebox
# import time

# #set value of n (no of pending approvals)
# global n
# n = 6


# class Example(tk.LabelFrame):
#     def __init__(self, *args, **kwargs):
#         tk.LabelFrame.__init__(self, *args, **kwargs)

#         data = [
#             # Nr. Name  Active
#             ["dsfsvfdbtt",123],
#             ["dscdvsfvfsdv",234],["dsfvbtb",678],
#             ["fdfgbgf",456],["dsfbdfgnn",12],
#             ["dvrgbdfgb",123]
#             ]


#         self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
#         self.grid_columnconfigure(1, weight=1)

#         tk.Label(self,
#                 text="Document Name",
#                 fg="#FFFFFF",
#                 padx=30, 
#                 font=("yu gothic ui bold", 20 * -1),
#                 bg="#272A37").grid(row=0, column=1, sticky="ew")
        
#         tk.Label(self, 
#                 text="Size (in kb)",
#                 padx=30,
#                 fg="#FFFFFF",
#                 font=("yu gothic ui bold", 20 * -1),
#                 bg="#272A37").grid(row=0, column=2, sticky="ew")

#         tk.Label(self,
#                 text="  View  ",
#                 fg="#FFFFFF",
#                 font=("yu gothic ui bold", 20 * -1),
#                 bg="#272A37").grid(row=0, column=3, sticky="ew")
        
#         tk.Label(self,
#                 text=" ",
#                 fg="#FFFFFF",
#                 font=("yu gothic ui bold", 20 * -1),
#                 bg="#272A37").grid(row=0, column=0, sticky="ew")

#         buttonImage1 = tk.PhotoImage(file="assets\\share.png")
#         action_button1 = tk.Button(self,
#                                   image=buttonImage1,
#                                   borderwidth=0,
#                                   highlightthickness=0,
#                                   relief="flat",
#                                   activebackground="#272A37",
#                                   cursor="hand2"
#                                   )
#         action_button1.image=buttonImage1
            

        

#         row = 1

#         for (nr, name) in data:
          
#             nr_label = tk.Label(self,text=str(nr),
#                                 fg="#FFFFFF",
#                                 font=("yu gothic ui bold", 20 * -1),
#                                 bg="#272A37")

#             name_label = tk.Label(self, 
#                                   text=str(name),
#                                   fg="#FFFFFF",
#                                   font=("yu gothic ui bold", 20 * -1),
#                                   bg="#272A37")
            
#             test_label = tk.Label(self,text= " ",
#                                 fg="#FFFFFF",
#                                 font=("yu gothic ui bold", 20 * -1),
#                                 bg="#272A37")
            
#             C1 = tk.Checkbutton(self,
#                                 activebackground="#272A37", 
#                                 activeforeground="#272A37",
#                                 bg="#272A37",bd=6,
#                                 onvalue = 1, 
#                                 offvalue = 0)


    

#             nr_label.grid(row=row, column=1, sticky="ew")
#             name_label.grid(row=row, column=2, sticky="ew")
#             test_label.grid(row=row - 1, column=3, sticky="ew")
#             C1.grid(row = row, column = 0, sticky= "ew")

#             row += 1
            
#         action_button1.grid(row=n, column=3, sticky="ew")

        
              

       

      
# def open_student_shate_docs(root):

#     # root = tk.Tk()
#     window = tk.Toplevel(root)
#     window.title("Share Documents")
#     # window.geometry("1166x600") # Increased size

#     # Set background color
#     window.configure(bg="#272A37")
#     height = (n)*39 + 35
#     width = 1240
#     x = (window.winfo_screenwidth() // 2) - (width // 2)
#     y = (window.winfo_screenheight() // 4) - (height // 4)
#     window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

#     window.configure(bg="#525561")


#     Example(window).pack(side="top", fill="both", expand=True, padx=10, pady=10)


#     window.mainloop()


# if __name__ == "__main__":
#     open_student_shate_docs()