import customtkinter as ctk

class Login:

    def __init__(self):
        self.root = ctk.CTk()
        self.interface()
        self.button_create()

    def interface(self):
        self.root.geometry("600x400")

    def button_create(self):
        button = ctk.CTkButton(
            master=self.root,
            text="Login",
            command=self.open_register
        )
        button.pack(pady=20)

    def open_register(self):
        self.root.withdraw()
        from .register import Register
        Register(self)

    def run(self):
        self.root.mainloop()