import customtkinter as ctk


class EncryptionCard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#1A1A1A",
            corner_radius=18,
            border_width=1,
            border_color="#2A2A2A"
        )

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        title = ctk.CTkLabel(
            self,
            text="Encrypt / Decrypt",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(anchor="nw", padx=25, pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Choose an algorithm, enter your text and key.",
            text_color="#AAAAAA",
            font=("Segoe UI", 14)
        )

        subtitle.pack(anchor="nw", padx=25)
        