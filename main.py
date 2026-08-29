import customtkinter as ctk

from ui.header import Header
from ui.sidebar import Sidebar
from ui.workspace import Workspace
from ui.history_panel import HistoryPanel


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

        # Sidebar
        self.content_frame.grid_columnconfigure(
            0,
            weight=0
        )

        # Workspace
        self.content_frame.grid_columnconfigure(
            1,
            weight=1
        )

        # History
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
    # Sidebar Navigation
    # ==================================================

    def handle_menu_click(self, key):

        # --------------------------------
        # Encrypt / Decrypt
        # --------------------------------

        if key == "encrypt":

            # Show normal encryption card
            self.workspace.show_encryption()

            # Show normal history
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

            # Show normal encryption workspace
            self.workspace.show_encryption()

            # Show history panel
            self.history.show_history()
            self.history.grid()

            self.history.search.focus_set()

        # --------------------------------
        # Favorites
        # --------------------------------

        elif key == "favorites":

            # Keep normal encryption workspace visible
            self.workspace.show_encryption()

            # Show favorites in right panel
            self.history.show_favorites_panel()
            self.history.grid()

        # --------------------------------
        # File Encryption
        # --------------------------------

        elif key == "file":

            # Show File Encryption card
            self.workspace.show_file_encryption()

            # Keep history visible
            self.history.show_history()
            self.history.grid()

        # --------------------------------
        # Caesar Cipher
        # --------------------------------

        elif key == "caesar":

            # Make sure normal encryption card is visible
            self.workspace.show_encryption()

            # Return history panel to normal history
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

            # Make sure normal encryption card is visible
            self.workspace.show_encryption()

            # Return history panel to normal history
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

            # Make sure normal encryption card is visible
            self.workspace.show_encryption()

            # Return history panel to normal history
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
        # Other Sections
        # --------------------------------

        else:

            # Return to normal encryption card
            self.workspace.show_encryption()

            # Return history to normal mode
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