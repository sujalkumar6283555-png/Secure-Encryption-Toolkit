import customtkinter as ctk


class HistoryPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            width=320,
            corner_radius=15,
            fg_color="#151515",
            border_width=1,
            border_color="#2A2A2A"
        )

        self.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(0, 10),
            pady=10
        )

        # Keep fixed width
        self.grid_propagate(False)

        # ----------------------------
        # Title
        # ----------------------------
        title = ctk.CTkLabel(
            self,
            text="History",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(anchor="nw", padx=20, pady=(20, 15))

        # ----------------------------
        # Search Box
        # ----------------------------
        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search history...",
            height=38,
            corner_radius=10
        )

        self.search.pack(fill="x", padx=20)

        # ----------------------------
        # Scroll Area
        # ----------------------------
        self.history_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.history_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=20
        )

        # ----------------------------
        # Temporary Sample Cards
        # ----------------------------
        sample_data = [
            ("Caesar Cipher", "Encrypt"),
            ("Vigenère Cipher", "Decrypt"),
            ("XOR Cipher", "Encrypt"),
        ]

        for algorithm, action in sample_data:

            card = ctk.CTkFrame(
                self.history_frame,
                corner_radius=12,
                fg_color="#1D1D1D"
            )

            card.pack(fill="x", pady=8)

            title = ctk.CTkLabel(
                card,
                text=algorithm,
                font=("Segoe UI", 15, "bold")
            )

            title.pack(anchor="w", padx=15, pady=(10, 2))

            mode = ctk.CTkLabel(
                card,
                text=action,
                text_color="#FF4040"
            )

            mode.pack(anchor="w", padx=15, pady=(0, 10))

        # ----------------------------
        # Clear Button
        # ----------------------------
        clear_btn = ctk.CTkButton(
            self,
            text="Clear History",
            height=42,
            fg_color="#B71C1C",
            hover_color="#8B0000"
        )

        clear_btn.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )