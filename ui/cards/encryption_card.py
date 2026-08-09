import customtkinter as ctk
from ui.cards.top_controls import TopControls
from ui.cards.text_area_section import TextAreaSection


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
        self.grid_rowconfigure(3, weight=1)   # Text areas
        self.grid_rowconfigure(4, weight=0)   # Buttons
        self.grid_rowconfigure(5, weight=0)   # Status

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

        # --------------------------------
        # ACTION BUTTONS
        # --------------------------------

        self.button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.button_frame.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=25,
            pady=(5, 10)
        )

        self.button_frame.grid_columnconfigure(0, weight=0)
        self.button_frame.grid_columnconfigure(1, weight=0)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=0)

        # Encrypt Button

        self.encrypt_button = ctk.CTkButton(
            self.button_frame,
            text="🔒  Encrypt",
            height=42,
            width=140,
            corner_radius=8,
            fg_color="#E3262E",
            hover_color="#B91C24",
            font=("Segoe UI", 14, "bold")
        )

        self.encrypt_button.grid(
            row=0,
            column=0,
            padx=(0, 10)
        )

        # Decrypt Button

        self.decrypt_button = ctk.CTkButton(
            self.button_frame,
            text="🔓  Decrypt",
            height=42,
            width=140,
            corner_radius=8,
            fg_color="#252525",
            hover_color="#333333",
            border_width=1,
            border_color="#555555",
            font=("Segoe UI", 14, "bold")
        )

        self.decrypt_button.grid(
            row=0,
            column=1,
            padx=(0, 10)
        )

        # Copy Output Button

        self.copy_button = ctk.CTkButton(
            self.button_frame,
            text="📋  Copy Output",
            height=42,
            width=150,
            corner_radius=8,
            fg_color="#252525",
            hover_color="#333333",
            border_width=1,
            border_color="#555555",
            font=("Segoe UI", 14)
        )

        self.copy_button.grid(
            row=0,
            column=2,
            sticky="e",
            padx=(0, 10)
        )

        # Export Button

        self.export_button = ctk.CTkButton(
            self.button_frame,
            text="↓  Export",
            height=42,
            width=120,
            corner_radius=8,
            fg_color="#252525",
            hover_color="#333333",
            border_width=1,
            border_color="#555555",
            font=("Segoe UI", 14)
        )

        self.export_button.grid(
            row=0,
            column=3
        )

        # --------------------------------
        # STATUS BAR
        # --------------------------------

        self.status_frame = ctk.CTkFrame(
            self,
            fg_color="#151515",
            corner_radius=10,
            border_width=1,
            border_color="#2A2A2A"
        )

        self.status_frame.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 20)
        )

        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="●  Ready",
            text_color="#AAAAAA",
            font=("Segoe UI", 14, "bold")
        )

        self.status_label.pack(
            side="left",
            padx=15,
            pady=12
        )

        self.status_description = ctk.CTkLabel(
            self.status_frame,
            text="Enter your text and select an algorithm to begin.",
            text_color="#777777",
            font=("Segoe UI", 13)
        )

        self.status_description.pack(
            side="left",
            padx=5,
            pady=12
        )