from tkinter import messagebox
import customtkinter as ctk
import services.auth as auth

class Register:

    def __init__(self,login):

        self.login = login
        self.register = ctk.CTkToplevel(login.root)
        self.interface()
        self.frames()
        self.widgets()
        self.caution()

    def interface(self):
        self.register.geometry("750x600")
        self.register.title("Register")
        self.register.resizable(False, False)

    def frames(self):
        self.header_frame = ctk.CTkFrame(master=self.register)
        self.header_frame.pack(fill="x")

        self.main_frame = ctk.CTkFrame(master=self.register)
        self.main_frame.pack(fill="both",expand=True)

        self.register_frame = ctk.CTkFrame(master=self.main_frame,fg_color="transparent")
        self.register_frame.pack(pady=(20,0))

        self.bottom_frame = ctk.CTkFrame(master=self.register)
        self.bottom_frame.pack(fill="x")

    def widgets(self):
        self.create_label()
        self.create_button()
        self.create_entry()
        

    def create_label(self):
        self.font_main_title = ctk.CTkFont(family='Arial',size=20,weight="bold")
        self.main_title = ctk.CTkLabel(master=self.header_frame,text="REGISTER USER",font=self.font_main_title)
        self.main_title.pack(pady=10)

        self.font_label = ctk.CTkFont(family='Arial',size=12,weight="bold")

        self.username_label = ctk.CTkLabel(master=self.register_frame,text="Username",font=self.font_label)
        self.username_label.grid(row=0,column=0)

        self.email_label = ctk.CTkLabel(master=self.register_frame,text="Email",font=self.font_label)
        self.email_label.grid(row=2,column=0)

        self.password_label = ctk.CTkLabel(master=self.register_frame,text="Password",font=self.font_label)
        self.password_label.grid(row=4,column=0)

        self.password_confirm_label = ctk.CTkLabel(master=self.register_frame,text="Confirm Password",font=self.font_label)
        self.password_confirm_label.grid(row=6,column=0)

    def create_entry(self):
        self.username_entry = ctk.CTkEntry(master=self.register_frame,width=300)
        self.username_entry.grid(row=1,column=0,pady=(0, 25))

        self.email_entry = ctk.CTkEntry(master=self.register_frame,width=300)
        self.email_entry.grid(row=3,column=0,pady=(0, 25))

        self.password_entry = ctk.CTkEntry(master=self.register_frame,width=300)
        self.password_entry.grid(row=5,column=0,pady=(0, 25))

        self.password_confirm_entry = ctk.CTkEntry(master=self.register_frame,width=300)
        self.password_confirm_entry.grid(row=7,column=0,pady=(0, 25))


    def create_button(self):

        self.close_button = ctk.CTkButton(master=self.bottom_frame,text="Close",command=self.close_register)
        self.close_button.pack(pady=20)

        self.register_button = ctk.CTkButton(master=self.register_frame,text="Register",command=self.handle_register)
        self.register_button.grid(row=8,column=0)

    def handle_register(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        password_confirm = self.password_confirm_entry.get().strip()

        result = auth.register_user(username, email, password, password_confirm)
        
        if result == "empty_fields":
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )

        elif result == "password_mismatch":
            messagebox.showwarning(
                "Passwords Don't Match",
                "The passwords do not match"
            )

        elif result == "invalid_email":
            messagebox.showwarning(
                "Error Email",
                "The format email is invalid"
            )

        elif result == "already_username":
            messagebox.showwarning(
                "Already Information",
                "Username Already Exists"
            )

        elif result == "already_email":
            messagebox.showwarning(
                "Already Information",
                "Email Already Exists"
            )

        elif result == "success":
            messagebox.showinfo(
                "Registration Complete",
                "Success"
            )

        self.register.destroy()
        self.login.root.deiconify()

        
    def close_register(self):
        self.register.destroy()
        self.login.root.deiconify()

    def caution(self):
        self.register.protocol("WM_DELETE_WINDOW", self.close_register)
        
    