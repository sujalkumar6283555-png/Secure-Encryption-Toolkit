import customtkinter as ctk


class SettingsPanel(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        # --------------------------------
        # WINDOW
        # --------------------------------

        self.title("Settings")
        self.geometry("500x500")
        self.resizable(False, False)

        self.configure(
            fg_color="#111111"
        )

        # Keep window above main application
        self.transient(parent)
        self.grab_set()

        # --------------------------------
        # TITLE
        # --------------------------------

        title = ctk.CTkLabel(
            self,
            text="⚙ Settings",
            font=("Segoe UI", 28, "bold"),
            text_color="#FFFFFF"
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(30, 5)
        )

        # --------------------------------
        # SUBTITLE
        # --------------------------------

        subtitle = ctk.CTkLabel(
            self,
            text="Customize your Secure Encryption Toolkit.",
            font=("Segoe UI", 13),
            text_color="#888888"
        )

        subtitle.pack(
            anchor="w",
            padx=30,
            pady=(0, 30)
        )

        # ========================================
        # APPEARANCE SECTION
        # ========================================

        appearance_label = ctk.CTkLabel(
            self,
            text="Appearance",
            font=("Segoe UI", 16, "bold"),
            text_color="#FFFFFF"
        )

        appearance_label.pack(
            anchor="w",
            padx=30,
            pady=(0, 10)
        )

        # --------------------------------
        # THEME
        # --------------------------------

        theme_frame = ctk.CTkFrame(
            self,
            fg_color="#1A1A1A",
            corner_radius=10
        )

        theme_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 25)
        )

        theme_title = ctk.CTkLabel(
            theme_frame,
            text="Theme",
            font=("Segoe UI", 14, "bold")
        )

        theme_title.pack(
            side="left",
            padx=15,
            pady=15
        )

        self.theme_menu = ctk.CTkOptionMenu(
            theme_frame,
            values=[
                "Dark",
                "Light",
                "System"
            ],
            width=130,
            height=36,
            fg_color="#B71C1C",
            button_color="#8B0000",
            button_hover_color="#6A0000",
            command=self.change_theme
        )

        self.theme_menu.set("Dark")

        self.theme_menu.pack(
            side="right",
            padx=15,
            pady=10
        )

        # ========================================
        # INFORMATION
        # ========================================

        info_label = ctk.CTkLabel(
            self,
            text="More settings will be added soon.",
            font=("Segoe UI", 13),
            text_color="#666666"
        )

        info_label.pack(
            pady=20
        )

        # ========================================
        # CLOSE BUTTON
        # ========================================

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
            pady=20
        )

    # ========================================
    # CHANGE THEME
    # ========================================

    def change_theme(self, selected_theme):

        if selected_theme == "Dark":

            ctk.set_appearance_mode("Dark")

        elif selected_theme == "Light":

            ctk.set_appearance_mode("Light")

        elif selected_theme == "System":

            ctk.set_appearance_mode("System")