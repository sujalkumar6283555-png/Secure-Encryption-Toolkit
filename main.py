import customtkinter as ctk

from ui.header import Header
from ui.sidebar import Sidebar
from ui.workspace import Workspace
from ui.history_panel import HistoryPanel
from ui.settings_panel import SettingsPanel
from ui.about_panel import AboutPanel


# ----------------------------
# App Configuration
# ----------------------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class SecureEncryptionToolkit(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ----------------------------
        # Window Configuration
        # ----------------------------

        self.title("Secure Encryption Toolkit")
        self.geometry("1400x850")
        self.minsize(1200, 700)
        self.configure(fg_color="#111111")

        # ----------------------------
        # Main Window Grid
        # ----------------------------

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)

        # ----------------------------
        # Header
        # ----------------------------

        self.header = Header(self)

        self.header.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        # ----------------------------
        # Content Frame
        # ----------------------------

        self.content_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content_frame.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        # ----------------------------
        # Content Grid
        # ----------------------------

        self.content_frame.grid_rowconfigure(
            0,
            weight=1
        )

        self.content_frame.grid_columnconfigure(
            0,
            weight=0
        )

        self.content_frame.grid_columnconfigure(
            1,
            weight=1
        )

        self.content_frame.grid_columnconfigure(
            2,
            weight=0
        )

        # ----------------------------
        # UI Components
        # ----------------------------

        self.sidebar = Sidebar(
            self.content_frame,
            self.handle_menu_click
        )

        self.workspace = Workspace(
            self.content_frame
        )

        self.history = HistoryPanel(
            self.content_frame
        )

    # ==================================================
    # SIDEBAR NAVIGATION
    # ==================================================

    def handle_menu_click(self, key):

        # --------------------------------
        # Encrypt / Decrypt
        # --------------------------------

        if key == "encrypt":

            self.workspace.show_encryption()

            self.history.show_history()
            self.history.grid()

            self.workspace.card.text_area.set_status(
                "●  Ready     Enter your text and select an algorithm to begin.",
                "#AAAAAA"
            )

        # --------------------------------
        # History
        # --------------------------------

        elif key == "history":

            self.workspace.show_encryption()

            self.history.show_history()
            self.history.grid()

            self.history.search.focus_set()

        # --------------------------------
        # Favorites
        # --------------------------------

        elif key == "favorites":

            self.workspace.show_encryption()

            self.history.show_favorites_panel()
            self.history.grid()

        # --------------------------------
        # File Encryption
        # --------------------------------

        elif key == "file":

            self.workspace.show_file_encryption()

            self.history.show_history()
            self.history.grid()

        # --------------------------------
        # Caesar Cipher
        # --------------------------------

        elif key == "caesar":

            self.workspace.show_encryption()

            self.history.show_history()
            self.history.grid()

            self.workspace.card.controls.algorithm_menu.set(
                "Caesar Cipher"
            )

            self.workspace.card.text_area.set_status(
                "●  Selected     Caesar Cipher",
                "#4CAF50"
            )

        # --------------------------------
        # Vigenère Cipher
        # --------------------------------

        elif key == "vigenere":

            self.workspace.show_encryption()

            self.history.show_history()
            self.history.grid()

            self.workspace.card.controls.algorithm_menu.set(
                "Vigenère Cipher"
            )

            self.workspace.card.text_area.set_status(
                "●  Selected     Vigenère Cipher",
                "#4CAF50"
            )

        # --------------------------------
        # XOR Cipher
        # --------------------------------

        elif key == "xor":

            self.workspace.show_encryption()

            self.history.show_history()
            self.history.grid()

            self.workspace.card.controls.algorithm_menu.set(
                "XOR Cipher"
            )

            self.workspace.card.text_area.set_status(
                "●  Selected     XOR Cipher",
                "#4CAF50"
            )

        # --------------------------------
        # Settings
        # --------------------------------

        elif key == "settings":

            SettingsPanel(self)

        # --------------------------------
        # About
        # --------------------------------

        elif key == "about":

            AboutPanel(self)

        # --------------------------------
        # Other Sections
        # --------------------------------

        else:

            self.workspace.show_encryption()

            self.history.show_history()
            self.history.grid()

            self.workspace.card.text_area.set_status(
                f"●  {key.title()} section is coming soon.",
                "#FFB000"
            )


# ----------------------------
# Start Application
# ----------------------------

if __name__ == "__main__":

    app = SecureEncryptionToolkit()

    app.mainloop()