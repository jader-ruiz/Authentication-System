import customtkinter as ctk
from tkinter import messagebox

class DeleteUser:

    def __init__(self,dashboard,user):
        self.dashboard = dashboard
        self.delete_user = ctk.CTkToplevel(dashboard.dashboard)
        self.user = user
        self.interface()
        self.caution()

    def interface(self):
        self.delete_user.geometry("500x100")
        self.delete_user.title("Delete User")
        self.delete_user.resizable(False, False)

    def close_dashboard(self):
        self.delete_user.destroy()
        self.dashboard.dashboard.deiconify()
    
    def caution(self):
        self.delete_user.protocol("WM_DELETE_WINDOW", self.close_dashboard)