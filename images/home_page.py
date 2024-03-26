from tkinter import *
from PIL import ImageTk, Image


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # Background Image
        self.bg_frame = Image.open('./background2.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # Login Frame
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=300, y=110)

        # EduVault Title
        self.txt = "Welcome to EduVault!"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Helvetica', 25, 'bold'), bg="#040405",
                             fg='white', bd=5, relief=FLAT)
        self.heading.place(x=80, y=30, width=500, height=30)

        # Left Side Image
        self.side_image = Image.open('./vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)
        
        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('./hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)
        
        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="You Are a..!", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=630, y=240)

        # Label asking user For student
        self.lgn_button = Image.open('./btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=300)
        self.login = Button(self.lgn_button_label, text='STUDENT', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        
        # Label asking user for INSTITUTE
        self.lgn_button = Image.open('./btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=380)
        self.login = Button(self.lgn_button_label, text='INSTITUTE', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        
        # Label asking user for Admin
        self.lgn_button = Image.open('./btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=460)
        self.login = Button(self.lgn_button_label, text='ADMIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        
         # Footer
        self.footer_frame = Frame(self.window, bg='#040405', width=1166, height=30)
        self.footer_frame.pack(side=BOTTOM, fill='x')

        self.footer_label = Label(self.footer_frame, text='© 2024 EduVault. All rights reserved.', font=("Helvetica", 10), bg='#040405', fg='white')
        self.footer_label.pack(pady=5)

        

  


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()


