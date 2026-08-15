import customtkinter as ctk
import services.auth as auth


class ManageUsers:

    def __init__(self, parent, user):
        self.parent = parent
        self.user = user

        self.manage_window = ctk.CTkToplevel(parent.dashboard)
        self.manage_window.title("Manage Users")
        self.manage_window.geometry("700x500")

        self.frames()
        self.widgets()
        self.caution()

    def frames(self):
        
        self.header_frame = ctk.CTkFrame(
            master=self.manage_window
        )
        self.header_frame.pack(fill="x")

        self.frame_search = ctk.CTkFrame(
            master=self.manage_window
        )
        self.frame_search.pack(fill="x")

        self.search_frame = ctk.CTkFrame(
            master=self.frame_search
        )
        self.search_frame.pack(pady=10)

        self.frame_users = ctk.CTkFrame(
            master=self.manage_window
        )
        self.frame_users.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        self.users_frame = ctk.CTkFrame(
            master=self.frame_users
        )
        self.users_frame.pack(
            pady=(10,0)
        )

        self.actions_frame = ctk.CTkFrame(
            master=self.manage_window
        )
        self.actions_frame.pack(
            fill="x",
            padx=20,
            pady=15
        )

        self.bottom_frame = ctk.CTkFrame(
            master=self.manage_window
        )
        self.bottom_frame.pack(fill="x")

    def widgets(self):
        self.create_labels()
        self.create_search()
        self.create_users_area()
        self.create_actions()
        self.create_bottom()

    def create_labels(self):

        self.title_font = ctk.CTkFont(
            family="Arial",
            size=20,
            weight="bold"
        )

        self.title_label = ctk.CTkLabel(
            master=self.header_frame,
            text="MANAGE USERS",
            font=self.title_font
        )

        self.title_label.pack(pady=15)

    def create_search(self):

        self.search_entry = ctk.CTkEntry(
            master=self.search_frame,
            width=300,
            placeholder_text="Search username..."
        )
        self.search_entry.pack(
            side="left",
            padx=(0, 10)
        )

        self.search_button = ctk.CTkButton(
            master=self.search_frame,
            text="Search"
        )
        self.search_button.pack(side="left")

    def create_users_area(self):

        self.id_header = ctk.CTkLabel(
            master=self.users_frame,
            text="ID"
        )
        self.id_header.grid(
            row=0,
            column=0,
            padx=20,
            pady=10
        )

        self.username_header = ctk.CTkLabel(
            master=self.users_frame,
            text="USERNAME"
        )
        self.username_header.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )

        self.email_header = ctk.CTkLabel(
            master=self.users_frame,
            text="EMAIL"
        )
        self.email_header.grid(
            row=0,
            column=2,
            padx=20,
            pady=10
        )

        self.role_header = ctk.CTkLabel(
            master=self.users_frame,
            text="ROLE"
        )
        self.role_header.grid(
            row=0,
            column=3,
            padx=20,
            pady=10
        )

    def create_actions(self):

        self.selected_user_label = ctk.CTkLabel(
            master=self.actions_frame,
            text="No user selected"
        )
        self.selected_user_label.pack(
            side="left",
            padx=10
        )

        self.change_role_button = ctk.CTkButton(
            master=self.actions_frame,
            text="Change Role"
        )
        self.change_role_button.pack(
            side="right",
            padx=5
        )

        self.delete_user_button = ctk.CTkButton(
            master=self.actions_frame,
            text="Delete User"
        )
        self.delete_user_button.pack(
            side="right",
            padx=5
        )

    def create_bottom(self):

        self.back_button = ctk.CTkButton(
            master=self.bottom_frame,
            text="Back",
            command=self.close_dashboard
        )

        self.back_button.pack(pady=10)

    def display_users(self):

        pass

    def close_dashboard(self):
        self.manage_window.destroy()
        self.parent.dashboard.deiconify()
    
    def caution(self):
        self.manage_window.protocol("WM_DELETE_WINDOW", self.close_dashboard)