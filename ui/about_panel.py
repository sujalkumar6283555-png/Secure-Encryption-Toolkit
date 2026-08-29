import customtkinter as ctk


class AboutPanel(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        # --------------------------------
        # WINDOW
        # --------------------------------

        self.title("About")
        self.geometry("520x600")
        self.resizable(False, False)

        self.configure(
            fg_color="#111111"
        )

        # Keep window above main application
        self.transient(parent)
        self.grab_set()

        # --------------------------------
        # ICON
        # --------------------------------

        icon = ctk.CTkLabel(
            self,
            text="🛡",
            font=("Segoe UI", 50)
        )

        icon.pack(
            pady=(30, 5)
        )

        # --------------------------------
        # TITLE
        # --------------------------------

        title = ctk.CTkLabel(
            self,
            text="Secure Encryption Toolkit",
            font=("Segoe UI", 26, "bold"),
            text_color="#FFFFFF"
        )

        title.pack(
            pady=(0, 5)
        )

        # --------------------------------
        # VERSION
        # --------------------------------

        version = ctk.CTkLabel(
            self,
            text="Version 1.0",
            font=("Segoe UI", 12),
            text_color="#888888"
        )

        version.pack(
            pady=(0, 25)
        )

        # --------------------------------
        # DESCRIPTION
        # --------------------------------

        description = ctk.CTkLabel(
            self,
            text=(
                "A desktop encryption toolkit designed to "
                "encrypt and decrypt text and files using "
                "multiple classical encryption algorithms."
            ),
            font=("Segoe UI", 13),
            text_color="#AAAAAA",
            wraplength=430,
            justify="center"
        )

        description.pack(
            padx=30,
            pady=(0, 25)
        )

        # --------------------------------
        # FEATURES
        # --------------------------------

        features_title = ctk.CTkLabel(
            self,
            text="Supported Features",
            font=("Segoe UI", 17, "bold"),
            text_color="#FFFFFF"
        )

        features_title.pack(
            anchor="w",
            padx=40,
            pady=(0, 10)
        )

        features = ctk.CTkLabel(
            self,
            text=(
                "🔐  Caesar Cipher\n"
                "🔑  Vigenère Cipher\n"
                "⚡  XOR Cipher\n"
                "📁  File Encryption & Decryption\n"
                "📜  Operation History\n"
                "⭐  Favorites\n"
                "⚙  Custom Settings"
            ),
            font=("Segoe UI", 13),
            text_color="#CCCCCC",
            justify="left"
        )

        features.pack(
            anchor="w",
            padx=55,
            pady=(0, 20)
        )

        # --------------------------------
        # TECHNOLOGY
        # --------------------------------

        technology = ctk.CTkLabel(
            self,
            text="Built with Python + CustomTkinter",
            font=("Segoe UI", 12),
            text_color="#777777"
        )

        technology.pack(
            pady=10
        )

        # --------------------------------
        # CLOSE BUTTON
        # --------------------------------

        close_button = ctk.CTkButton(
            self,
            text="Close",
            height=42,
            width=150,
            corner_radius=8,
            fg_color="#B71C1C",
            hover_color="#8B0000",
            font=("Segoe UI", 14, "bold"),
            command=self.destroy
        )

        close_button.pack(
            pady=15
        )