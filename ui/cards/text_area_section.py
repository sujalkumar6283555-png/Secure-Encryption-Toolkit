import customtkinter as ctk


class TextAreaSection(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.pack(fill="both", expand=True, padx=25, pady=20)

        # ----------------------------
        # Input
        # ----------------------------
        input_label = ctk.CTkLabel(
            self,
            text="Input Text",
            font=("Segoe UI", 16, "bold")
        )
        input_label.pack(anchor="w", pady=(0, 8))

        self.input_text = ctk.CTkTextbox(
            self,
            height=170,
            corner_radius=12,
            border_width=1,
            border_color="#2A2A2A"
        )

        self.input_text.pack(fill="x")

        # ----------------------------
        # Output
        # ----------------------------
        output_label = ctk.CTkLabel(
            self,
            text="Output Text",
            font=("Segoe UI", 16, "bold")
        )
        output_label.pack(anchor="w", pady=(25, 8))

        self.output_text = ctk.CTkTextbox(
            self,
            height=170,
            corner_radius=12,
            border_width=1,
            border_color="#2A2A2A"
        )

        self.output_text.pack(fill="x")