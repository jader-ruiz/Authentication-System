import customtkinter as ctk
from tkinter import messagebox
import services.auth as auth

class DeleteUser:

    def __init__(self, parent_window, user,on_success=None):
        self.parent_window = parent_window
        self.user = user
        self.on_success = on_success

        self.delete_user = ctk.CTkToplevel(parent_window)
        
        self.interface()
        self.frames()
        self.widgets()
        self.caution()

    def interface(self):
        self.delete_user.geometry("400x150")
        self.delete_user.title("Delete User")
        self.delete_user.resizable(False, False)

    def frames(self):
        self.header_frame = ctk.CTkFrame(master=self.delete_user)
        self.header_frame.pack(fill="x")

        self.main_frame = ctk.CTkFrame(master=self.delete_user)
        self.main_frame.pack(fill="both",expand=True)

        self.frame_main = ctk.CTkFrame(master=self.main_frame)
        self.frame_main.pack(pady=(30,0))

    def widgets(self):
        self.c_labels()
        self.c_button()

    def c_labels(self):
        self.font_main_title = ctk.CTkFont(family='Arial',size=20,weight="bold")
        self.main_label = ctk.CTkLabel(
            master=self.header_frame,
            text="Are you sure?",
            font=self.font_main_title
        )
        self.main_label.pack(pady=10)

    def c_button(self):
        self.yes_button = ctk.CTkButton(
            master=self.frame_main,
            text="Yes",
            command=self.yes_button_c
        )
        self.yes_button.pack(
            side="left",
            padx=(0,10)
        )

        self.no_button = ctk.CTkButton(
            master=self.frame_main,
            text="No",
            command=self.no_button_c
        )
        self.no_button.pack(side="left")

    def yes_button_c(self):
        user_id = self.user[0]
        result = auth.delete_user(user_id)

        if result == "success":
            messagebox.showinfo(
                "Success",
                "The user has been delete"
            )
        self.delete_user.destroy()
        
        if self.on_success:
            self.on_success()

    def no_button_c(self):
        self.parent_window.deiconify()
        self.delete_user.destroy()

    def close_dashboard(self):
        self.delete_user.destroy()
        self.parent_window.deiconify()
    
    def caution(self):
        self.delete_user.protocol("WM_DELETE_WINDOW", self.close_dashboard)