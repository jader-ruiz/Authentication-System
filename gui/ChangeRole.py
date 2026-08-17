import customtkinter as ctk
import services.auth as auth
from tkinter import messagebox

class ChangeRole:

    def __init__(self, manage_users, user):

        self.manage_users = manage_users
        self.user = user

        self.change_role = ctk.CTkToplevel(
            manage_users.manage_window
        )

        self.interface()
        self.frames()
        self.widgets()
        self.fill_user_info()
        self.caution()


    def interface(self):

        self.change_role.geometry("400x350")
        self.change_role.title("Change Role")
        self.change_role.resizable(False, False)

    def frames(self):

        self.header_frame = ctk.CTkFrame(
            master=self.change_role
        )
        self.header_frame.pack(fill="x")

        self.main_frame = ctk.CTkFrame(
            master=self.change_role,
            fg_color="transparent"
        )
        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        self.bottom_frame = ctk.CTkFrame(
            master=self.change_role,
            fg_color="transparent"
        )
        self.bottom_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 20)
        )

    def widgets(self):
        self.create_labels()
        self.create_role_menu()
        self.create_buttons()

    def create_labels(self):

        self.title_font = ctk.CTkFont(
            family="Arial",
            size=20,
            weight="bold"
        )

        self.label_font = ctk.CTkFont(
            family="Arial",
            size=13,
            weight="bold"
        )

        self.title_label = ctk.CTkLabel(
            master=self.header_frame,
            text="CHANGE ROLE",
            font=self.title_font
        )

        self.title_label.pack(pady=15)


        self.username_label = ctk.CTkLabel(
            master=self.main_frame,
            text="Username:"
        )

        self.username_label.pack(
            anchor="w",
            pady=(0, 5)
        )


        self.current_role_label = ctk.CTkLabel(
            master=self.main_frame,
            text="Current role:"
        )

        self.current_role_label.pack(
            anchor="w",
            pady=(0, 20)
        )


        self.new_role_label = ctk.CTkLabel(
            master=self.main_frame,
            text="New role:",
            font=self.label_font
        )

        self.new_role_label.pack(
            anchor="w",
            pady=(0, 5)
        )

    def create_role_menu(self):

        self.role_menu = ctk.CTkOptionMenu(
            master=self.main_frame,
            values=["User", "Admin"],
            width=300
        )

        self.role_menu.pack(
            fill="x"
        )

    def fill_user_info(self):

        self.username_label.configure(
            text=f"Username: {self.user[1]}"
        )

        self.current_role_label.configure(
            text=f"Current role: {self.user[3]}"
        )

        self.role_menu.set(
            self.user[3]
        )

    def create_buttons(self):

        self.cancel_button = ctk.CTkButton(
            master=self.bottom_frame,
            text="Cancel",
            command=self.close_dashboard
        )

        self.cancel_button.pack(
            side="left",
            expand=True,
            padx=5
        )


        self.save_button = ctk.CTkButton(
            master=self.bottom_frame,
            text="Save",
            command=self.save_button
        )

        self.save_button.pack(
            side="left",
            expand=True,
            padx=5
        )

    def save_button(self):
        pass
        user_id = self.user[0]
        new_role = self.role_menu.get()

        result = auth.update_role(user_id,new_role)

        if result == "success":
            messagebox.showinfo(
                "Success",
                "The role is changed"
            )
        self.close_dashboard()

    def close_dashboard(self):
        self.change_role.destroy()
        self.manage_users.manage_window.deiconify()
    
    def caution(self):
        self.change_role.protocol("WM_DELETE_WINDOW", self.close_dashboard)