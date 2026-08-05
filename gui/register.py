import customtkinter as ctk

class Register:

    def __init__(self,login):

        self.login = login
        self.register = ctk.CTkToplevel(login.root)
        self.interface()
        self.button_create()
        self.caution()

    def interface(self):
        self.register.geometry("600x400")
        self.register.title("Register User")
        self.register.resizable(False, False)

    def button_create(self):
        button = ctk.CTkButton(master=self.register,text="Close",command=self.close_register)
        button.pack(pady=20)

    def close_register(self):
        self.register.destroy()
        self.login.root.deiconify()

    def caution(self):
        self.register.protocol("WM_DELETE_WINDOW", self.close_register)
        
    