import customtkinter as ctk
from ui.cards.encryption_card import EncryptionCard



class Workspace(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#151515",
            corner_radius=0
        )

        self.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=10,
    pady=10
)

       
        self.card = EncryptionCard(self)