import customtkinter as ctk

# ----------------------------
# App Configuration
# ----------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")   # We'll customize colors ourselves later


class SecureEncryptionToolkit(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window title
        self.title("Secure Encryption Toolkit")

        # Window size
        self.geometry("1400x850")

        # Minimum size
        self.minsize(1200, 700)

        # Background color
        self.configure(fg_color="#111111")


# ----------------------------
# Start Application
# ----------------------------
if __name__ == "__main__":
    app = SecureEncryptionToolkit()
    app.mainloop()