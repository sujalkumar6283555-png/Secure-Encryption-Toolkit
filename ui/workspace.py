import customtkinter as ctk
from ui.cards.encryption_card import EncryptionCard


class Workspace(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="transparent"
        )

        # Put workspace inside main window
        self.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        # Allow the encryption card to expand
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Encryption Card
        self.card = EncryptionCard(self)