import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=250,
            corner_radius=0,
            fg_color="#0F0F0F"
        )

        self.pack(side="left", fill="y")

        title = ctk.CTkLabel(
            self,
            text="🔒 Secure\nEncryption",
            font=("Segoe UI", 24, "bold"),
            justify="left"
        )

        title.pack(pady=(30, 40), padx=20, anchor="w")

        menu_items = [
            "🏠 Encrypt / Decrypt",
            "📜 History",
            "⭐ Favorites",
            "📁 File Encryption",
            "⚙ Settings",
            "ℹ About"
        ]

        for item in menu_items:
            button = ctk.CTkButton(
                self,
                text=item,
                width=200,
                height=45,
                fg_color="transparent",
                hover_color="#B71C1C",
                anchor="w"
            )

            button.pack(pady=6, padx=20)