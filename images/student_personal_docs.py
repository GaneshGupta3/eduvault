import tkinter as tk

from tkinter import messagebox
import time
from fetch_documents_list import *

#set value of n (no of pending approvals)
global n
n = 6


class Example(tk.LabelFrame):
    def __init__(self, user_id,category,*args, **kwargs):
        document_list = fetch_documents(user_id,category)
        print(document_list)
        tk.LabelFrame.__init__(self, *args, **kwargs)

        data = [
            # Nr. Name  Active
            [document_list[0][1],document_list[0][4]/1000],
            [document_list[1][1],document_list[1][4]/1000],[document_list[2][1],document_list[2][4]/1000],
            [document_list[3][1],document_list[3][4]/1000],[document_list[4][1],document_list[4][4]/1000],
            [document_list[5][1],document_list[5][4]/1000]
            ]


        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self,
                text="Document Name",
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

        for (nr, name) in data:
          
            nr_label = tk.Label(self,text=str(nr),
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
                                      cursor="hand2"
                                      )
            action_button1.image=buttonImage1
            
            buttonImage2 = tk.PhotoImage(file="assets\\delete.png")
            action_button2 = tk.Button(self,
                                      image=buttonImage2,
                                      borderwidth=0,
                                      highlightthickness=0,
                                      relief="flat",
                                      activebackground="#272A37",
                                      cursor="hand2"
                                      )
            action_button2.image=buttonImage2
            
          

            nr_label.grid(row=row, column=0, sticky="ew")
            name_label.grid(row=row, column=1, sticky="ew")
       
            action_button1.grid(row=row, column=3, sticky="ew")
            action_button2.grid(row=row, column=4, sticky="ew")

            row += 1
      


def open_personal_docs(user_id,category):
    root = tk.Tk()
    
    height = (n)*42 + 35
    width = 1240
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.configure(bg="#525561")


    Example(user_id,category,root).pack(side="top", fill="both", expand=True, padx=10, pady=10)


    root.mainloop()


if __name__ == "__main__":
    open_personal_docs("S353356847444","Personal Documents")
    