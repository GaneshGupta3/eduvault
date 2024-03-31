
import mysql.connector
import tkinter as tk
from current_user_info import *
from admin import *

from tkinter import messagebox
import time

def view(uid):
     print(uid)
     currentuserinfo = currentUserInfo(uid,"I")
     name = currentuserinfo.name
     tan = currentuserinfo.tan
     email = currentuserinfo.email
     phone = currentuserinfo.phone

     info_message = f"UID: {uid}\nName: {name}\nTAN: {tan}\nEmail: {email}\nPhone: {phone}"
     messagebox.showinfo("Information", info_message)

admin = Admin
institutes_not_approved = admin.pending_approval_list()
print(institutes_not_approved)
def approve(uid):
    admin = Admin()
    admin.grant_approval(uid)

#set value of n (no of pending approvals)
global n
n = 6


class Example(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)

        data = [
            # Nr. Name  Active
            [1,institutes_not_approved[0][0], institutes_not_approved[0][1]],
            [2,institutes_not_approved[1][0], institutes_not_approved[1][1]],[3,institutes_not_approved[2][0], institutes_not_approved[2][1]],
            [4,institutes_not_approved[3][0], institutes_not_approved[3][1]],[5,institutes_not_approved[4][0], institutes_not_approved[4][1]],
            [6,institutes_not_approved[5][0], institutes_not_approved[5][1]]
            ]


        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self,
                text="Sr. No",
                fg="#FFFFFF",
                padx=30, 
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=0, sticky="ew")
        
        tk.Label(self, 
                text="Name",
                padx=30,
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=1, sticky="ew")
        
        tk.Label(self,
                text="UID",
                padx=100,
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=2, sticky="ew")

        tk.Label(self,
                text="  View  ",
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=3, sticky="ew")

        tk.Label(self,
                text="  Approve  ",
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=4, sticky="ew")

        row = 1

        for (nr, name, uid) in data:
          
            nr_label = tk.Label(self,text=str(nr),
                                fg="#FFFFFF",
                                font=("yu gothic ui bold", 20 * -1),
                                bg="#272A37")

            name_label = tk.Label(self, 
                                  text=str(name),
                                  fg="#FFFFFF",
                                  font=("yu gothic ui bold", 20 * -1),
                                  bg="#272A37")

            uid_label = tk.Label(self, 
                                  text=str(uid),
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
                                      command=lambda uid=uid: view(uid)
                                      )
            action_button1.image=buttonImage1
            
            buttonImage2 = tk.PhotoImage(file="assets\\approval_approve.png")
            action_button2 = tk.Button(self,
                                      image=buttonImage2,
                                      borderwidth=0,
                                      highlightthickness=0,
                                      relief="flat",
                                      activebackground="#272A37",
                                      cursor="hand2",
                                      command=lambda uid=uid: approve(uid)
                                      )
            action_button2.image=buttonImage2
            
          

            nr_label.grid(row=row, column=0, sticky="ew")
            name_label.grid(row=row, column=1, sticky="ew")
            uid_label.grid(row=row, column=2, sticky="ew")
            action_button1.grid(row=row, column=3, sticky="ew")
            action_button2.grid(row=row, column=4, sticky="ew")

            row += 1
      

def load_admin_approval():
    root = tk.Tk()
    root.title("admin approval page")
    height = (n)*42 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.configure(bg="#525561")


    Example(root).pack(side="top", fill="both", expand=True, padx=10, pady=10)


    root.mainloop()

if __name__ == "__main__":
    load_admin_approval()