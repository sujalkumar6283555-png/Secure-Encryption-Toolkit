import customtkinter as ctk


class Header(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            height=70,
            corner_radius=0,
            fg_color="#161616"
        )

        self.pack(fill="x")

        title = ctk.CTkLabel(
            self,
            text="🛡 Secure Encryption Toolkit",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        )

        title.pack(padx=25, pady=18, anchor="w")