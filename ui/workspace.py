import customtkinter as ctk

from ui.cards.encryption_card import EncryptionCard
from ui.cards.file_encryption_card import FileEncryptionCard


class Workspace(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        # --------------------------------
        # Put workspace inside main window
        # --------------------------------

        self.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        # --------------------------------
        # Workspace Grid Configuration
        # --------------------------------

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        # --------------------------------
        # Encryption Card
        # --------------------------------

        self.card = EncryptionCard(self)

        # --------------------------------
        # File Encryption Card
        # --------------------------------

        self.file_card = FileEncryptionCard(self)

        # Hide File Encryption initially
        self.file_card.grid_remove()

    # ========================================
    # SHOW TEXT ENCRYPTION
    # ========================================

    def show_encryption(self):

        self.file_card.grid_remove()

        self.card.grid()

    # ========================================
    # SHOW FILE ENCRYPTION
    # ========================================

    def show_file_encryption(self):

        self.card.grid_remove()

        self.file_card.grid()