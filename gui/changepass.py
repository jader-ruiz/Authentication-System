import customtkinter as ctk
from tkinter import messagebox

class ChangePassword:
    def __init__(self,dashboard,user):
        self.dashboard = dashboard
        self.change_password = ctk.CTkToplevel(dashboard.dashboard)
        self.user = user
        self.interface()
        self.frames()
        self.widgets()
        self.caution()

    def interface(self):
        self.change_password.geometry("500x400")
        self.change_password.title("Edit Profile")
        self.change_password.resizable(False, False)

    def frames(self):
        self.header_frame = ctk.CTkFrame(master=self.change_password)
        self.header_frame.pack(fill="x")
        
        self.main_frame = ctk.CTkFrame(master=self.change_password)
        self.main_frame.pack(fill="both",expand=True)
        
        self.c_password_frame = ctk.CTkFrame(master=self.main_frame,fg_color="transparent")
        self.c_password_frame.pack(pady=(20,0))
        
        self.bottom_frame = ctk.CTkFrame(master=self.change_password)
        self.bottom_frame.pack(fill="x")

    def widgets(self):
        self.c_button()
        self.c_entry()
        self.c_labels()

    def c_labels(self):
        self.font_main_title = ctk.CTkFont(family='Arial',size=20,weight="bold")
        self.c_password_title = ctk.CTkLabel(master=self.header_frame,text="CHANGE PASSWORD",font=self.font_main_title)
        self.c_password_title.pack(pady=25)

        self.font_label = ctk.CTkFont(family='Arial',size=12,weight="bold")

        self.current_password = ctk.CTkLabel(master=self.c_password_frame,text="Current Password",font=self.font_label)
        self.current_password.grid(column=0,row=0,pady=(10,0))

        self.new_password = ctk.CTkLabel(master=self.c_password_frame,text="New Password",font=self.font_label)
        self.new_password.grid(column=0,row=2)

    def c_entry(self):
        self.entry_current_password = ctk.CTkEntry(master=self.c_password_frame,width=300)
        self.entry_current_password.grid(column=0,row=1,pady=(0,20))

        self.entry_new_password = ctk.CTkEntry(master=self.c_password_frame,width=300)
        self.entry_new_password.grid(column=0,row=3,pady=(0,20))

    def c_button(self):
        self.save_button = ctk.CTkButton(
            master=self.c_password_frame,
            text="Save"
        )
        self.save_button.grid(column=0,row=4,pady=(5,10))

        self.close_button = ctk.CTkButton(
            master=self.bottom_frame,
            text="Close",
            command=self.close_dashboard
        )
        self.close_button.pack(pady=25)

    def handle_password(self):
        pass

    def close_dashboard(self):
        self.change_password.destroy()
        self.dashboard.dashboard.deiconify()
        
    def caution(self):
        self.change_password.protocol("WM_DELETE_WINDOW", self.close_dashboard)