import customtkinter as ctk


class TextAreaSection(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="transparent"
        )

        # --------------------------------
        # GRID CONFIGURATION
        # --------------------------------

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --------------------------------
        # INPUT LABEL
        # --------------------------------

        input_label = ctk.CTkLabel(
            self,
            text="Input Text",
            font=("Segoe UI", 15, "bold")
        )

        input_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=(0, 8)
        )

        # --------------------------------
        # OUTPUT LABEL
        # --------------------------------

        output_label = ctk.CTkLabel(
            self,
            text="Output Text",
            font=("Segoe UI", 15, "bold")
        )

        output_label.grid(
            row=0,
            column=1,
            sticky="w",
            padx=(10, 0),
            pady=(0, 8)
        )

        # --------------------------------
        # INPUT TEXTBOX
        # --------------------------------

        self.input_text = ctk.CTkTextbox(
            self,
            corner_radius=12,
            border_width=1,
            border_color="#333333",
            fg_color="#111111",
            font=("Segoe UI", 14)
        )

        self.input_text.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        # --------------------------------
        # OUTPUT TEXTBOX
        # --------------------------------

        self.output_text = ctk.CTkTextbox(
            self,
            corner_radius=12,
            border_width=1,
            border_color="#333333",
            fg_color="#111111",
            font=("Segoe UI", 14)
        )

        self.output_text.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )