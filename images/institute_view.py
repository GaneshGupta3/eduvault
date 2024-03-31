import tkinter as tk
from tkinter import messagebox
from current_user_info import *
from admin import *
from institute_file_access import *


from tkinter import messagebox
import time

# set value of n (no of pending approvals)
n = 6


class Example(tk.LabelFrame):
    def __init__(self, institute_id, *args, **kwargs):
        def view(uid,file_id):
            print(uid)
            retrieve_file(uid,file_id)

        tk.LabelFrame.__init__(self, *args, **kwargs)
        instituteHasAccessto = instituteHasAccessTo(institute_id, "I")
        for file in instituteHasAccessto:
            print(file)
        data = [
            # Nr. Name  Active
            [instituteHasAccessto[0][0][0], instituteHasAccessto[0][0][1], instituteHasAccessto[0][0][5]],
            [instituteHasAccessto[1][0][0], instituteHasAccessto[1][0][1], instituteHasAccessto[1][0][5]],
            [instituteHasAccessto[2][0][0], instituteHasAccessto[2][0][1], instituteHasAccessto[2][0][5]],
            [instituteHasAccessto[3][0][0], instituteHasAccessto[3][0][1], instituteHasAccessto[3][0][5]],
            [instituteHasAccessto[4][0][0], instituteHasAccessto[4][0][1], instituteHasAccessto[4][0][5]],
            [instituteHasAccessto[5][0][0], instituteHasAccessto[5][0][1], instituteHasAccessto[5][0][5]]
        ]

        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self,
                 text="File id",
                 fg="#FFFFFF",
                 padx=30,
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=0, sticky="ew")

        tk.Label(self,
                 text="File Name",
                 padx=30,
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=1, sticky="ew")

        tk.Label(self,
                 text="User ID",
                 padx=100,
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=2, sticky="ew")

        tk.Label(self,
                 text="  View  ",
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#272A37").grid(row=0, column=3, sticky="ew")

        row = 1

        for (nr, name, uid) in data:

            nr_label = tk.Label(self, text=str(nr),
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
                                       command=lambda file_id=nr, user_id=uid: view(user_id,file_id)
                                       )
            action_button1.image = buttonImage1

            nr_label.grid(row=row, column=0, sticky="ew")
            name_label.grid(row=row, column=1, sticky="ew")
            uid_label.grid(row=row, column=2, sticky="ew")
            action_button1.grid(row=row, column=3, sticky="ew")

            row += 1


def load_institute_view(institute_id):
    root = tk.Tk()
    root.title("institute document view page")
    height = (n) * 42 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.configure(bg="#525561")

    Example(institute_id, root).pack(side="top", fill="both", expand=True, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    load_institute_view("I138615553989")
