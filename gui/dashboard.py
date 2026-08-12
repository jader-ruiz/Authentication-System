import customtkinter as ctk

class Dashboard:

    def __init__(self,login,user):
        self.login = login
        self.dashboard = ctk.CTkToplevel(login.root)
        self.user = user
        self.interface()
        self.frames()
        self.widgets()
        self.caution()
        

    def interface(self):
        self.dashboard.geometry("750x600")
        self.dashboard.title("Dashboard")
        self.dashboard.resizable(False, False)

    def frames(self):
        self.header_frame = ctk.CTkFrame(master=self.dashboard)
        self.header_frame.pack(fill="x")
        
        self.main_frame = ctk.CTkFrame(master=self.dashboard)
        self.main_frame.pack(fill="both",expand=True)
        
        self.dashboard_frame = ctk.CTkFrame(master=self.main_frame,fg_color="transparent")
        self.dashboard_frame.pack(pady=(20,0))
        
        self.bottom_frame = ctk.CTkFrame(master=self.dashboard)
        self.bottom_frame.pack(fill="x")

    def widgets(self):
        self.c_labels()
        self.c_button()

    def c_labels(self):
        self.font_main_title = ctk.CTkFont(family='Arial',size=20,weight="bold")
        self.main_title = ctk.CTkLabel(master=self.header_frame,text="DASHBOARD",font=self.font_main_title)
        self.main_title.pack(pady=10)

        self.font_label = ctk.CTkFont(family='Arial',size=12,weight="bold")

        self.s_title = ctk.CTkLabel(master=self.dashboard_frame,text="Welcome!",font=self.font_label)
        self.s_title.grid(column=0,row=0,pady=(5,10))

        self.username_label = ctk.CTkLabel(master=self.dashboard_frame,text=f"Username: {self.user['username']}",font=self.font_label)
        self.username_label.grid(row=1,column=0,pady=(0,5))
        
        self.email_label = ctk.CTkLabel(master=self.dashboard_frame,text=f"Email: {self.user['email']}",font=self.font_label)
        self.email_label.grid(row=2,column=0,pady=(0,5))

        self.r_label = ctk.CTkLabel(master=self.dashboard_frame,text=f"Role: {'role'}",font=self.font_label)
        self.r_label.grid(row=3,column=0,pady=(0,25))

    def c_button(self):
        self.edit_profile = ctk.CTkButton(
            master=self.dashboard_frame,
            text="Edit Profile",
            command=self.open_edit_profile
        )
        self.edit_profile.grid(column=0,row=4,pady=(0,10))

        self.change_password = ctk.CTkButton(
            master=self.dashboard_frame,
            text="Change Password",
            command=self.open_change_password
        )
        self.change_password.grid(column=0,row=5,pady=(0,10))

        self.delete_account = ctk.CTkButton(
            master=self.dashboard_frame,
            text="Delete Account"
        )
        self.delete_account.grid(column=0,row=6)

        self.logout = ctk.CTkButton(
            master=self.bottom_frame,
            text="Logout",
            command=self.close_dashboard
        )
        self.logout.pack(pady=20)

    def close_dashboard(self):
        self.dashboard.destroy()
        self.login.root.deiconify()

    def caution(self):
        self.dashboard.protocol("WM_DELETE_WINDOW", self.close_dashboard)

    def open_edit_profile(self):
        self.dashboard.withdraw()
        from .edit_profile import EditProfile
        EditProfile(self,self.user)

    def update_user_info(self):
        self.username_label.configure(
            text=f"Username: {self.user['username']}"
        )

        self.email_label.configure(
            text=f"Email: {self.user['email']}"
        )

    def open_change_password(self):
        self.dashboard.withdraw()
        from .changepass import ChangePassword
        ChangePassword(self,self.user)