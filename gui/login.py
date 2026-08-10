import customtkinter as ctk
import services.auth as auth
from tkinter import messagebox
from gui.dashboard import Dashboard

class Login:

    def __init__(self):
        self.root = ctk.CTk()
        self.interface()
        self.frames()
        self.widgets()

    def interface(self):
        self.root.geometry("750x600")
        self.root.title("Login")
        self.root.resizable(False, False)

    def frames(self):
        self.header_frame = ctk.CTkFrame(master=self.root)
        self.header_frame.pack(fill="x")
        
        self.main_frame = ctk.CTkFrame(master=self.root)
        self.main_frame.pack(fill="both",expand=True)
        
        self.login_frame = ctk.CTkFrame(master=self.main_frame,fg_color="transparent")
        self.login_frame.pack(pady=(20,0))

    def widgets(self):
        self.create_labels()
        self.create_entry()
        self.button_create()
        

    def create_labels(self):
        self.font_main_title = ctk.CTkFont(family='Arial',size=20,weight="bold")
        self.main_title = ctk.CTkLabel(master=self.header_frame,text="LOGIN USER",font=self.font_main_title)
        self.main_title.pack(pady=10)

        self.font_label = ctk.CTkFont(family='Arial',size=12,weight="bold")

        self.username_label = ctk.CTkLabel(master=self.login_frame,text="Username",font=self.font_label)
        self.username_label.grid(row=0,column=0)

        self.password_label = ctk.CTkLabel(master=self.login_frame, text="Password",font=self.font_label)
        self.password_label.grid(row=2,column=0)


    def create_entry(self):
        self.username_entry = ctk.CTkEntry(master=self.login_frame,width=300)
        self.username_entry.grid(row=1,column=0,pady=(0, 25))

        self.password_entry = ctk.CTkEntry(master=self.login_frame,width=300)
        self.password_entry.grid(row=3,column=0,pady=(0,25))

    def button_create(self):
        self.register_button = ctk.CTkButton(
            master=self.login_frame,
            text="Create Account",
            command=self.open_register,
        )
        self.register_button.grid(column=0,row=7)

        self.login_button = ctk.CTkButton(
            master=self.login_frame,
            text="Login",
            command=self.handle_login
        )
        self.login_button.grid(column=0,row=6,pady=(0,15))

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        result = auth.login_user(username,password)

        if result["status"] == "empty_fields":
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )            

        elif result["status"] == "user_not_found":
            messagebox.showwarning(
                "Information not found",
                "The user not found"
            )


        elif result["status"] == "wrong_password":
            messagebox.showwarning(
                "Information doesn't match",
                "Invalid username or password"
            )

        elif result["status"] == "success":
            user = result["user"]
            self.dashboard = Dashboard(self, user)
            self.root.withdraw()

    def open_register(self):
        self.root.withdraw()
        from .register import Register
        Register(self)

    def run(self):
        self.root.mainloop()