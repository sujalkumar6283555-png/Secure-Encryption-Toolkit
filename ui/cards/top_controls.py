import customtkinter as ctk


class TopControls(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="transparent"
        )

        

        # -------------------------
        # Grid Configuration
        # -------------------------
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # -------------------------
        # Algorithm
        # -------------------------
        algorithm_label = ctk.CTkLabel(
            self,
            text="Algorithm",
            font=("Segoe UI", 14, "bold")
        )

        algorithm_label.grid(row=0, column=0, sticky="w", padx=(0, 15))

        self.algorithm_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "Caesar Cipher",
                "Vigenère Cipher",
                "XOR Cipher"
            ],
            height=38,
            fg_color="#B71C1C",
            button_color="#8B0000",
            button_hover_color="#6A0000"
        )

        self.algorithm_menu.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=(0, 15)
        )

        # -------------------------
        # Mode
        # -------------------------
        mode_label = ctk.CTkLabel(
            self,
            text="Mode",
            font=("Segoe UI", 14, "bold")
        )

        mode_label.grid(row=0, column=1, sticky="w")

        self.mode_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "Encrypt",
                "Decrypt"
            ],
            height=38,
            fg_color="#B71C1C",
            button_color="#8B0000",
            button_hover_color="#6A0000"
        )

        self.mode_menu.grid(
            row=1,
            column=1,
            sticky="ew"
        )

        # -------------------------
        # Key
        # -------------------------
        key_label = ctk.CTkLabel(
            self,
            text="Encryption Key",
            font=("Segoe UI", 14, "bold")
        )

        key_label.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(20, 5)
        )

        self.key_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter encryption key...",
            height=40
        )

        self.key_entry.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew"
        )