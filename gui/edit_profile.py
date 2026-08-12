import customtkinter as ctk
from tkinter import messagebox
import services.auth as auth

class EditProfile:

    def __init__(self,dashboard,user):
        self.dashboard = dashboard
        self.edit_profile = ctk.CTkToplevel(dashboard.dashboard)
        self.user = user
        self.interface()
        self.frames()
        self.widgets()
        self.fill_entry()
        self.caution()

    def interface(self):
        self.edit_profile.geometry("500x400")
        self.edit_profile.title("Edit Profile")
        self.edit_profile.resizable(False, False)

    def frames(self):
        self.header_frame = ctk.CTkFrame(master=self.edit_profile)
        self.header_frame.pack(fill="x")
        
        self.main_frame = ctk.CTkFrame(master=self.edit_profile)
        self.main_frame.pack(fill="both",expand=True)
        
        self.e_profile_frame = ctk.CTkFrame(master=self.main_frame,fg_color="transparent")
        self.e_profile_frame.pack(pady=(20,0))
        
        self.bottom_frame = ctk.CTkFrame(master=self.edit_profile)
        self.bottom_frame.pack(fill="x")

    def widgets(self):
        self.c_labels()
        self.c_entry()
        self.c_button()

    def c_labels(self):
        self.font_main_title = ctk.CTkFont(family='Arial',size=20,weight="bold")
        self.title_e_profile = ctk.CTkLabel(master=self.header_frame,text="EDIT PROFILE",font=self.font_main_title)
        self.title_e_profile.pack(pady=20)

        self.font_label = ctk.CTkFont(family='Arial',size=12,weight="bold")

        self.username_label = ctk.CTkLabel(master=self.e_profile_frame,text="Username",font=self.font_label)
        self.username_label.grid(column=0,row=0)

        self.email_label = ctk.CTkLabel(master=self.e_profile_frame,text="Email",font=self.font_label)
        self.email_label.grid(column=0,row=2)

    def c_entry(self):
        self.username_entry = ctk.CTkEntry(master=self.e_profile_frame,width=300)
        self.username_entry.grid(column=0,row=1,pady=(0,25))

        self.email_entry = ctk.CTkEntry(master=self.e_profile_frame,width=300)
        self.email_entry.grid(column=0,row=3,pady=(0,25))

    def fill_entry(self):
        self.username_entry.insert(0, self.user["username"])
        self.email_entry.insert(0, self.user["email"])

    def c_button(self):
        self.back_button = ctk.CTkButton(master=self.bottom_frame,text="Back",command=self.close_dashboard)
        self.back_button.pack(pady=15)

        self.save_button = ctk.CTkButton(master=self.e_profile_frame,text="Save",command=self.handle_edit)
        self.save_button.grid(column=0,row=4,pady=(5,0))

    def handle_edit(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()

        result = auth.edit_user(self.user["id"],username,email)

        if result == "empty_fields":
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
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
            self.user["username"] = username
            self.user["email"] = email

            self.dashboard.update_user_info()

            messagebox.showinfo(
                "Success",
                "Update profile"
            )
            
            self.dashboard.deiconify()
            self.edit_profile.destroy()
            
    def close_dashboard(self):
        self.edit_profile.destroy()
        self.dashboard.deiconify()
    
    def caution(self):
        self.edit_profile.protocol("WM_DELETE_WINDOW", self.close_dashboard)