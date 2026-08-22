import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            width=250,
            corner_radius=0,
            fg_color="#0F0F0F"
        )

        self.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # Prevent sidebar from shrinking
        self.grid_propagate(False)

        # ========================================
        # LOGO / TITLE
        # ========================================

        title = ctk.CTkLabel(
            self,
            text="🔒 Secure\nEncryption",
            font=("Segoe UI", 24, "bold"),
            justify="left",
            text_color="#FFFFFF"
        )

        title.pack(
            pady=(30, 35),
            padx=20,
            anchor="w"
        )

        # ========================================
        # MAIN MENU LABEL
        # ========================================

        menu_label = ctk.CTkLabel(
            self,
            text="MAIN MENU",
            font=("Segoe UI", 11, "bold"),
            text_color="#666666"
        )

        menu_label.pack(
            padx=20,
            pady=(0, 10),
            anchor="w"
        )

        # ========================================
        # MAIN MENU BUTTONS
        # ========================================

        self.workspace_button = ctk.CTkButton(
            self,
            text="🏠   Encrypt / Decrypt",
            height=44,
            corner_radius=8,
            fg_color="#B71C1C",
            hover_color="#8B0000",
            text_color="#FFFFFF",
            anchor="w",
            font=("Segoe UI", 14, "bold")
        )

        self.workspace_button.pack(
            fill="x",
            padx=15,
            pady=4
        )

        self.history_button = ctk.CTkButton(
            self,
            text="📜   History",
            height=44,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 14)
        )

        self.history_button.pack(
            fill="x",
            padx=15,
            pady=4
        )

        self.favorites_button = ctk.CTkButton(
            self,
            text="⭐   Favorites",
            height=44,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 14)
        )

        self.favorites_button.pack(
            fill="x",
            padx=15,
            pady=4
        )

        self.file_button = ctk.CTkButton(
            self,
            text="📁   File Encryption",
            height=44,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 14)
        )

        self.file_button.pack(
            fill="x",
            padx=15,
            pady=4
        )

        # ========================================
        # ALGORITHMS SECTION
        # ========================================

        algorithm_label = ctk.CTkLabel(
            self,
            text="ALGORITHMS",
            font=("Segoe UI", 11, "bold"),
            text_color="#666666"
        )

        algorithm_label.pack(
            padx=20,
            pady=(25, 10),
            anchor="w"
        )

        algorithms = [
            "Caesar Cipher",
            "Vigenère Cipher",
            "XOR Cipher"
        ]

        for algorithm in algorithms:

            button = ctk.CTkButton(
                self,
                text=f"   {algorithm}",
                height=36,
                corner_radius=7,
                fg_color="transparent",
                hover_color="#252525",
                text_color="#999999",
                anchor="w",
                font=("Segoe UI", 13)
            )

            button.pack(
                fill="x",
                padx=15,
                pady=2
            )

        # ========================================
        # BOTTOM SECTION
        # ========================================

        bottom_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom_frame.pack(
            side="bottom",
            fill="x",
            padx=15,
            pady=15
        )

        self.settings_button = ctk.CTkButton(
            bottom_frame,
            text="⚙   Settings",
            height=42,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 13)
        )

        self.settings_button.pack(
            fill="x",
            pady=3
        )

        self.about_button = ctk.CTkButton(
            bottom_frame,
            text="ℹ   About",
            height=42,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 13)
        )

        self.about_button.pack(
            fill="x",
            pady=3
        )