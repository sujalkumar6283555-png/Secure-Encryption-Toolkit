import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, command=None):

        super().__init__(
            parent,
            width=250,
            corner_radius=0,
            fg_color="#0F0F0F"
        )

        self.command = command

        # Prevent sidebar from changing width
        self.grid_propagate(False)

        self.grid(
            row=0,
            column=0,
            sticky="ns"
        )

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

        self.buttons = {}

        # --------------------------------
        # Encrypt / Decrypt
        # --------------------------------

        self.workspace_button = ctk.CTkButton(
            self,
            text="🏠   Encrypt / Decrypt",
            height=44,
            corner_radius=8,
            fg_color="#B71C1C",
            hover_color="#8B0000",
            text_color="#FFFFFF",
            anchor="w",
            font=("Segoe UI", 14, "bold"),
            command=lambda: self.menu_clicked("encrypt")
        )

        self.workspace_button.pack(
            fill="x",
            padx=15,
            pady=4
        )

        self.buttons["encrypt"] = self.workspace_button

        # --------------------------------
        # History
        # --------------------------------

        self.history_button = ctk.CTkButton(
            self,
            text="📜   History",
            height=44,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 14),
            command=lambda: self.menu_clicked("history")
        )

        self.history_button.pack(
            fill="x",
            padx=15,
            pady=4
        )

        self.buttons["history"] = self.history_button

        # --------------------------------
        # Favorites
        # --------------------------------

        self.favorites_button = ctk.CTkButton(
            self,
            text="⭐   Favorites",
            height=44,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 14),
            command=lambda: self.menu_clicked("favorites")
        )

        self.favorites_button.pack(
            fill="x",
            padx=15,
            pady=4
        )

        self.buttons["favorites"] = self.favorites_button

        # --------------------------------
        # File Encryption
        # --------------------------------

        self.file_button = ctk.CTkButton(
            self,
            text="📁   File Encryption",
            height=44,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 14),
            command=lambda: self.menu_clicked("file")
        )

        self.file_button.pack(
            fill="x",
            padx=15,
            pady=4
        )

        self.buttons["file"] = self.file_button

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
            pady=(25, 8),
            anchor="w"
        )

        # --------------------------------
        # Caesar Cipher
        # --------------------------------

        self.caesar_button = ctk.CTkButton(
            self,
            text="   Caesar Cipher",
            height=34,
            corner_radius=7,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#999999",
            anchor="w",
            font=("Segoe UI", 13),
            command=lambda: self.menu_clicked("caesar")
        )

        self.caesar_button.pack(
            fill="x",
            padx=15,
            pady=2
        )

        # --------------------------------
        # Vigenère Cipher
        # --------------------------------

        self.vigenere_button = ctk.CTkButton(
            self,
            text="   Vigenère Cipher",
            height=34,
            corner_radius=7,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#999999",
            anchor="w",
            font=("Segoe UI", 13),
            command=lambda: self.menu_clicked("vigenere")
        )

        self.vigenere_button.pack(
            fill="x",
            padx=15,
            pady=2
        )

        # --------------------------------
        # XOR Cipher
        # --------------------------------

        self.xor_button = ctk.CTkButton(
            self,
            text="   XOR Cipher",
            height=34,
            corner_radius=7,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#999999",
            anchor="w",
            font=("Segoe UI", 13),
            command=lambda: self.menu_clicked("xor")
        )

        self.xor_button.pack(
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

        # --------------------------------
        # Settings
        # --------------------------------

        self.settings_button = ctk.CTkButton(
            bottom_frame,
            text="⚙   Settings",
            height=42,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 13),
            command=lambda: self.menu_clicked("settings")
        )

        self.settings_button.pack(
            fill="x",
            pady=3
        )

        self.buttons["settings"] = self.settings_button

        # --------------------------------
        # About
        # --------------------------------

        self.about_button = ctk.CTkButton(
            bottom_frame,
            text="ℹ   About",
            height=42,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#252525",
            text_color="#CCCCCC",
            anchor="w",
            font=("Segoe UI", 13),
            command=lambda: self.menu_clicked("about")
        )

        self.about_button.pack(
            fill="x",
            pady=3
        )

        self.buttons["about"] = self.about_button

    # ========================================
    # MENU CLICK
    # ========================================

    def menu_clicked(self, key):

        # --------------------------------
        # Reset normal menu buttons
        # --------------------------------

        for button in self.buttons.values():

            button.configure(
                fg_color="transparent",
                text_color="#CCCCCC"
            )

        # --------------------------------
        # Reset algorithm buttons
        # --------------------------------

        self.caesar_button.configure(
            fg_color="transparent",
            text_color="#999999"
        )

        self.vigenere_button.configure(
            fg_color="transparent",
            text_color="#999999"
        )

        self.xor_button.configure(
            fg_color="transparent",
            text_color="#999999"
        )

        # --------------------------------
        # Highlight selected button
        # --------------------------------

        if key in self.buttons:

            self.buttons[key].configure(
                fg_color="#B71C1C",
                text_color="#FFFFFF"
            )

        elif key == "caesar":

            self.caesar_button.configure(
                fg_color="#B71C1C",
                text_color="#FFFFFF"
            )

        elif key == "vigenere":

            self.vigenere_button.configure(
                fg_color="#B71C1C",
                text_color="#FFFFFF"
            )

        elif key == "xor":

            self.xor_button.configure(
                fg_color="#B71C1C",
                text_color="#FFFFFF"
            )

        # --------------------------------
        # Notify main application
        # --------------------------------

        if self.command:
            self.command(key)