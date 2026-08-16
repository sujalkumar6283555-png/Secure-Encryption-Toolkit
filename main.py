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
        self.grid_rowconfigure(0, weight=0)   # Header
        self.grid_rowconfigure(1, weight=1)   # Content

        self.grid_columnconfigure(0, weight=1)

        # ----------------------------
        # Header
        # ----------------------------
        self.header = Header(self)
        self.header.grid(row=0, column=0, sticky="ew")

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

        # Content Grid
        self.content_frame.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.content_frame.grid_columnconfigure(0, weight=0)

        # Workspace
        self.content_frame.grid_columnconfigure(1, weight=1)

        # History Panel (Coming Soon)
        self.content_frame.grid_columnconfigure(2, weight=0)

        # ----------------------------
        # UI Components
        # ----------------------------
        self.sidebar = Sidebar(self.content_frame)
        self.workspace = Workspace(self.content_frame)
        self.history = HistoryPanel(self.content_frame)
        


# ----------------------------
# Start Application
# ----------------------------
if __name__ == "__main__":
    app = SecureEncryptionToolkit()
    app.mainloop()          