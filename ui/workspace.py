import customtkinter as ctk


class Workspace(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#151515",
            corner_radius=0
        )

        self.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        title = ctk.CTkLabel(
            self,
            text="Encryption Workspace",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(anchor="nw", padx=25, pady=(20, 10))