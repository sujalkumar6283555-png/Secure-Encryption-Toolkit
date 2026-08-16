import customtkinter as ctk

from ui.cards.top_controls import TopControls
from ui.cards.text_area_section import TextAreaSection

from core import caesar
from core import vigenere


class EncryptionCard(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#1A1A1A",
            corner_radius=18,
            border_width=1,
            border_color="#2A2A2A"
        )

        # --------------------------------
        # CARD POSITION
        # --------------------------------

        self.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=20,
            pady=20
        )

        # --------------------------------
        # GRID CONFIGURATION
        # --------------------------------

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)   # Title
        self.grid_rowconfigure(1, weight=0)   # Subtitle
        self.grid_rowconfigure(2, weight=0)   # Controls
        self.grid_rowconfigure(3, weight=1)   # Text area + buttons

        # --------------------------------
        # TITLE
        # --------------------------------

        title = ctk.CTkLabel(
            self,
            text="Encrypt / Decrypt",
            font=("Segoe UI", 28, "bold"),
            text_color="#FFFFFF"
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=25,
            pady=(20, 5)
        )

        # --------------------------------
        # SUBTITLE
        # --------------------------------

        subtitle = ctk.CTkLabel(
            self,
            text="Choose an algorithm, enter your text and key.",
            text_color="#AAAAAA",
            font=("Segoe UI", 14)
        )

        subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            padx=25,
            pady=(0, 5)
        )

        # --------------------------------
        # TOP CONTROLS
        # --------------------------------

        self.controls = TopControls(self)

        self.controls.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=0,
            pady=10
        )

        # --------------------------------
        # TEXT AREA SECTION
        # --------------------------------

        self.text_area = TextAreaSection(self)

        self.text_area.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=25,
            pady=15
        )