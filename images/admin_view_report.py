import tkinter as tk
from tkinter import messagebox
import time
from report import *

# set value of n (no of pending approvals)
global n
n = 6

report = Report()
report_list = report.view_report()

class Example(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)

        data = [
            [1, report_list[0][0], report_list[0][1], report_list[0][2], report_list[0][3]],
            [2, report_list[1][0], report_list[1][1], report_list[1][2], report_list[1][3]],
            [3, report_list[2][0], report_list[2][1], report_list[2][2], report_list[2][3]],
            [4, report_list[3][0], report_list[3][1], report_list[3][2], report_list[3][3]],
            [5, report_list[4][0], report_list[4][1], report_list[4][2], report_list[4][3]],
            [6, report_list[5][0], report_list[5][1], report_list[5][2], report_list[5][3]]
        ]

        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self,
                 text="Sr. No",
                 fg="#FFFFFF",
                 padx=30,
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#000000").grid(row=0, column=0, sticky="ew")

        tk.Label(self,
                 text="Report ID",
                 fg="#FFFFFF",
                 padx=30,
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#000000").grid(row=0, column=1, sticky="ew")

        tk.Label(self,
                 text="Reported By   ",
                 padx=30,
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#000000").grid(row=0, column=2, sticky="ew")

        tk.Label(self,
                 text="         Reported To          ",
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#000000").grid(row=0, column=3, sticky="ew")

        tk.Label(self,
                 text="  Message  ",
                 fg="#FFFFFF",
                 font=("yu gothic ui bold", 20 * -1),
                 bg="#000000").grid(row=0, column=4, sticky="ew")

        row = 1

        for (nr, report_id, reported_by, reported_to, message) in data:

            nr_label = tk.Label(self, text=str(nr),
                                fg="#FFFFFF",
                                font=("yu gothic ui bold", 20 * -1),
                                bg="#000000")

            report_id_label = tk.Label(self,
                                        text=str(report_id),
                                        fg="#FFFFFF",
                                        font=("yu gothic ui bold", 20 * -1),
                                        bg="#000000")

            reported_by_label = tk.Label(self,
                                          text=str(reported_by),
                                          fg="#FFFFFF",
                                          font=("yu gothic ui bold", 20 * -1),
                                          bg="#000000")

            reported_to_label = tk.Label(self,
                                          text=str(reported_to),
                                          fg="#FFFFFF",
                                          font=("yu gothic ui bold", 20 * -1),
                                          bg="#000000")

            def message_button_click(msg):
                messagebox.showinfo("Message", msg)

            buttonImage1 = tk.PhotoImage(file="assets\\message_resize.png")
            action_button1 = tk.Button(self,
                                       image=buttonImage1,
                                       borderwidth=0,
                                       highlightthickness=0,
                                       relief="flat",
                                       activebackground="#272A37",
                                       cursor="hand2",
                                       command=lambda msg=message: message_button_click(msg))
            action_button1.image = buttonImage1

            nr_label.grid(row=row, column=0, sticky="ew")
            report_id_label.grid(row=row, column=1, sticky="ew")
            reported_by_label.grid(row=row, column=2, sticky="ew")
            reported_to_label.grid(row=row, column=3, sticky="ew")
            action_button1.grid(row=row, column=4, sticky="ew")

            row += 1


def open_admin_view_report():
    root = tk.Tk()

    height = (n) * 38 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.configure(bg="#525561")

    Example(root).pack(side="top", fill="both", expand=True, padx=10, pady=10)

    root.mainloop()
if __name__ == "__main__":
    open_admin_view_report()
