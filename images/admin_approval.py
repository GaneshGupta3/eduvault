import mysql.connector
import tkinter as tk

from tkinter import messagebox
import time

def view():
     print("view button clicked")

def approve():
    print("approve button clicked")

#set value of n (no of pending approvals)
global n
n = 6


class Example(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)

        data = [
            # Nr. Name  Active
            [1,"abccewjc", "234214123 "],
            [2,"dsjcknsd ", "21413535"],[3,"dcsdvsddf", "34364647"],
            [4," jcdkcn", "4354765"],[5,"fdvdfbf", "24235737"],
            [6,"ckc", "658769870"]
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
                                      command=view
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
                                      command=approve
                                      )
            action_button2.image=buttonImage2
            
          

            nr_label.grid(row=row, column=0, sticky="ew")
            name_label.grid(row=row, column=1, sticky="ew")
            uid_label.grid(row=row, column=2, sticky="ew")
            action_button1.grid(row=row, column=3, sticky="ew")
            action_button2.grid(row=row, column=4, sticky="ew")

            row += 1
      



if __name__ == "__main__":
    root = tk.Tk()
    
    height = (n)*42 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.configure(bg="#525561")


    Example(root).pack(side="top", fill="both", expand=True, padx=10, pady=10)


    root.mainloop()