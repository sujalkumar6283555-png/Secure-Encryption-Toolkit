import customtkinter as ctk
from tkinter import filedialog

from core.caesar import encrypt, decrypt
from core.vigenere import encrypt as vigenere_encrypt
from core.vigenere import decrypt as vigenere_decrypt
from core.xor import encrypt as xor_encrypt
from core.xor import decrypt as xor_decrypt


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

        # --------------------------------
        # BUTTON AREA
        # --------------------------------

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(12, 8)
        )

        button_frame.grid_columnconfigure(0, weight=0)
        button_frame.grid_columnconfigure(1, weight=0)
        button_frame.grid_columnconfigure(2, weight=1)
        button_frame.grid_columnconfigure(3, weight=0)

        # --------------------------------
        # ENCRYPT BUTTON
        # --------------------------------

        self.encrypt_button = ctk.CTkButton(
            button_frame,
            text="🔒  Encrypt",
            height=40,
            width=140,
            fg_color="#B71C1C",
            hover_color="#8B0000",
            font=("Segoe UI", 14, "bold"),
            command=self.encrypt_text
        )

        self.encrypt_button.grid(
            row=0,
            column=0,
            padx=(0, 10)
        )

        # --------------------------------
        # DECRYPT BUTTON
        # --------------------------------

        self.decrypt_button = ctk.CTkButton(
            button_frame,
            text="🔓  Decrypt",
            height=40,
            width=140,
            fg_color="#333333",
            hover_color="#444444",
            font=("Segoe UI", 14, "bold"),
            command=self.decrypt_text
        )

        self.decrypt_button.grid(
            row=0,
            column=1,
            padx=(0, 10)
        )

        # --------------------------------
        # COPY OUTPUT BUTTON
        # --------------------------------

        self.copy_button = ctk.CTkButton(
            button_frame,
            text="📋  Copy Output",
            height=40,
            width=140,
            fg_color="#333333",
            hover_color="#444444",
            font=("Segoe UI", 14),
            command=self.copy_output
        )

        self.copy_button.grid(
            row=0,
            column=3,
            padx=(0, 10)
        )

        # --------------------------------
        # EXPORT BUTTON
        # --------------------------------

        self.export_button = ctk.CTkButton(
            button_frame,
            text="⬇  Export",
            height=40,
            width=110,
            fg_color="#333333",
            hover_color="#444444",
            font=("Segoe UI", 14),
            command=self.export_output
        )

        self.export_button.grid(
            row=0,
            column=4
        )

        # --------------------------------
        # STATUS BAR
        # --------------------------------

        self.status_frame = ctk.CTkFrame(
            self,
            fg_color="#191919",
            corner_radius=10,
            border_width=1,
            border_color="#2A2A2A"
        )

        self.status_frame.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 5)
        )

        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="●  Ready     Enter your text and select an algorithm to begin.",
            text_color="#BBBBBB",
            font=("Segoe UI", 12)
        )

        self.status_label.pack(
            anchor="w",
            padx=15,
            pady=9
        )

    # ========================================
    # ENCRYPT
    # ========================================

    def encrypt_text(self):

        algorithm = self.master.controls.algorithm_menu.get()
        
        key = self.master.controls.key_entry.get()
        text = self.input_text.get("1.0", "end-1c")

        if not text:
            self.set_status(
            "●  Error     Please enter some text.",
            "#FF5555"
        )
            return

        if not key:
            self.set_status(
            "●  Error     Please enter an encryption key.",
            "#FF5555"
        )
            return

    # --------------------------------
    # Caesar Cipher
    # --------------------------------

        if algorithm == "Caesar Cipher":

            try:
                key = int(key)
            except ValueError:
                self.set_status(
                "●  Error     Caesar Cipher key must be a number.",
                "#FF5555"
            )
                return

            result = encrypt(text, key)

            success_message = (
            "●  Success     Text encrypted successfully using Caesar Cipher."
        )

    # --------------------------------
    # Vigenère Cipher
    # --------------------------------

        elif algorithm == "Vigenère Cipher":

            if not key.isalpha():
                self.set_status(
                "●  Error     Vigenère key must contain letters only.",
                "#FF5555"
            )
                return

            result = vigenere_encrypt(text, key)

            success_message = (
            "●  Success     Text encrypted successfully using Vigenère Cipher."
        )
        elif algorithm == "XOR Cipher":

            try:
                key = int(key)
            except ValueError:
                self.set_status(
            "●  Error     XOR Cipher key must be a number.",
            "#FF5555"
        )
                return

            result = xor_encrypt(text, key)

            

            success_message = (
        "●  Success     Text encrypted successfully using XOR Cipher."
    )
    # --------------------------------
    # Other algorithms
    # --------------------------------

        else:

            self.set_status(
            f"●  {algorithm} is coming soon.",
            "#FFB000"
        )
            return

    # --------------------------------
    # Show Output
    # --------------------------------

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)

        self.set_status(
        success_message,
        "#4CAF50"
    )
        self.winfo_toplevel().history.add_history(
    algorithm,
    "Encrypt",
    key,
    text,
    result
)
        

        
       
    # ========================================
    # DECRYPT
    # ========================================

    def decrypt_text(self):

        algorithm = self.master.controls.algorithm_menu.get()
        key = self.master.controls.key_entry.get()
        text = self.output_text.get("1.0", "end-1c")

        if not text:
            self.set_status(
            "●  Error     Please enter encrypted text.",
            "#FF5555"
        )
            return

        if not key:
            self.set_status(
            "●  Error     Please enter an encryption key.",
            "#FF5555"
        )
            return

    # --------------------------------
    # Caesar Cipher
    # --------------------------------

        if algorithm == "Caesar Cipher":

            try:
                key = int(key)
            except ValueError:
                self.set_status(
                "●  Error     Caesar Cipher key must be a number.",
                "#FF5555"
            )
                return

            result = decrypt(text, key)

            success_message = (
            "●  Success     Text decrypted successfully using Caesar Cipher."
        )

    # --------------------------------
    # Vigenère Cipher
    # --------------------------------

        elif algorithm == "Vigenère Cipher":

            if not key.isalpha():
                self.set_status(
                "●  Error     Vigenère key must contain letters only.",
                "#FF5555"
            )
                return

            result = vigenere_decrypt(text, key)

            success_message = (
            "●  Success     Text decrypted successfully using Vigenère Cipher."
        )

        elif algorithm == "XOR Cipher":

            try:
                key = int(key)
            except ValueError:
                self.set_status(
            "●  Error     XOR Cipher key must be a number.",
            "#FF5555"
        )
                return

            result = xor_decrypt(text, key)

            success_message = (
        "●  Success     Text decrypted successfully using XOR Cipher."
    )    

    # --------------------------------
    # Other Algorithms
    # --------------------------------

        else:

            self.set_status(
            f"●  {algorithm} is coming soon.",
            "#FFB000"
        )
            return

    # --------------------------------
    # Show Output
    # --------------------------------

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)

        self.set_status(
        success_message,
        "#4CAF50"
    )
        self.winfo_toplevel().history.add_history(
    algorithm,
    "Decrypt",
    key,
    text,
    result
)

    # ========================================
    # COPY OUTPUT
    # ========================================

    def copy_output(self):

        output = self.output_text.get("1.0", "end-1c")

        if not output.strip():
            self.set_status(
                "●  Error     Output box is empty.",
                "#FF5555"
            )
            return

        self.clipboard_clear()
        self.clipboard_append(output)

        self.set_status(
            "●  Success     Output copied to clipboard.",
            "#4CAF50"
        )

    # ========================================
    # EXPORT OUTPUT
    # ========================================

    def export_output(self):

        output = self.output_text.get("1.0", "end-1c")

        if not output.strip():
            self.set_status(
                "●  Error     Nothing to export.",
                "#FF5555"
            )
            return

        file_path = filedialog.asksaveasfilename(
            title="Export Encryption Result",
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(output)

            self.set_status(
                "●  Success     Output exported successfully.",
                "#4CAF50"
            )

        except Exception as error:
            self.set_status(
                f"●  Error     {error}",
                "#FF5555"
            )

    # ========================================
    # STATUS
    # ========================================

    def set_status(self, message, color="#BBBBBB"):

        self.status_label.configure(
            text=message,
            text_color=color
        )