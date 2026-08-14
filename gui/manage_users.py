import customtkinter as ctk
import services.auth as auth


class ManageUsers:

    def __init__(self, parent, user):
        self.parent = parent
        self.user = user

        self.manage_window = ctk.CTkToplevel(parent.dashboard)
        self.manage_window.title("Manage Users")
        self.manage_window.geometry("700x500")

        self.create_widgets()
        self.caution()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            master=self.manage_window,
            text="MANAGE USERS"
        )
        self.title_label.pack(pady=20)

        users = auth.get_all_users()

        for user in users:
            print(user)

    def close_dashboard(self):
        self.manage_window.destroy()
        self.parent.dashboard.deiconify()
    
    def caution(self):
        self.manage_window.protocol("WM_DELETE_WINDOW", self.close_dashboard)