import customtkinter as ctk
from tkinter import filedialog
import os


class FileEncryptionCard(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#1A1A1A",
            corner_radius=18,
            border_width=1,
            border_color="#2A2A2A"
        )

        self.selected_file = None

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

        self.grid_columnconfigure(
            0,
            weight=1
        )

        # --------------------------------
        # TITLE
        # --------------------------------

        title = ctk.CTkLabel(
            self,
            text="File Encryption",
            font=("Segoe UI", 28, "bold"),
            text_color="#FFFFFF"
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=25,
            pady=(25, 5)
        )

        # --------------------------------
        # SUBTITLE
        # --------------------------------

        subtitle = ctk.CTkLabel(
            self,
            text="Encrypt or decrypt files using a selected algorithm.",
            text_color="#AAAAAA",
            font=("Segoe UI", 14)
        )

        subtitle.grid(
            row=1,
            column=0,
            sticky="w",
            padx=25,
            pady=(0, 25)
        )

        # --------------------------------
        # SELECT FILE LABEL
        # --------------------------------

        file_label = ctk.CTkLabel(
            self,
            text="Select File",
            font=("Segoe UI", 14, "bold")
        )

        file_label.grid(
            row=2,
            column=0,
            sticky="w",
            padx=25,
            pady=(5, 8)
        )

        # --------------------------------
        # FILE SELECTION FRAME
        # --------------------------------

        file_frame = ctk.CTkFrame(
            self,
            fg_color="#111111",
            corner_radius=10,
            border_width=1,
            border_color="#333333"
        )

        file_frame.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 25)
        )

        file_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # Selected file label

        self.file_label = ctk.CTkLabel(
            file_frame,
            text="No file selected",
            text_color="#777777",
            font=("Segoe UI", 13),
            anchor="w"
        )

        self.file_label.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=15,
            pady=12
        )

        # Choose file button

        self.choose_button = ctk.CTkButton(
            file_frame,
            text="📁  Choose File",
            height=38,
            width=140,
            corner_radius=8,
            fg_color="#B71C1C",
            hover_color="#8B0000",
            font=("Segoe UI", 13, "bold"),
            command=self.choose_file
        )

        self.choose_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        # --------------------------------
        # ALGORITHM
        # --------------------------------

        algorithm_label = ctk.CTkLabel(
            self,
            text="Algorithm",
            font=("Segoe UI", 14, "bold")
        )

        algorithm_label.grid(
            row=4,
            column=0,
            sticky="w",
            padx=25,
            pady=(0, 8)
        )

        self.algorithm_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "Caesar Cipher",
                "Vigenère Cipher",
                "XOR Cipher"
            ],
            height=40,
            fg_color="#B71C1C",
            button_color="#8B0000",
            button_hover_color="#6A0000"
        )

        self.algorithm_menu.set("XOR Cipher")

        self.algorithm_menu.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 25)
        )

        # --------------------------------
        # ENCRYPTION KEY
        # --------------------------------

        key_label = ctk.CTkLabel(
            self,
            text="Encryption Key",
            font=("Segoe UI", 14, "bold")
        )

        key_label.grid(
            row=6,
            column=0,
            sticky="w",
            padx=25,
            pady=(0, 8)
        )

        self.key_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter encryption key...",
            height=40
        )

        self.key_entry.grid(
            row=7,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 30)
        )

        # --------------------------------
        # ACTION BUTTONS
        # --------------------------------

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.grid(
            row=8,
            column=0,
            sticky="w",
            padx=25,
            pady=(0, 25)
        )

        # Encrypt

        self.encrypt_button = ctk.CTkButton(
            button_frame,
            text="🔒  Encrypt File",
            height=42,
            width=160,
            corner_radius=8,
            fg_color="#E3262E",
            hover_color="#B91C24",
            font=("Segoe UI", 14, "bold"),
            command=self.encrypt_file
        )

        self.encrypt_button.grid(
            row=0,
            column=0,
            padx=(0, 10)
        )

        # Decrypt

        self.decrypt_button = ctk.CTkButton(
            button_frame,
            text="🔓  Decrypt File",
            height=42,
            width=160,
            corner_radius=8,
            fg_color="#252525",
            hover_color="#333333",
            border_width=1,
            border_color="#555555",
            font=("Segoe UI", 14, "bold"),
            command=self.decrypt_file
        )

        self.decrypt_button.grid(
            row=0,
            column=1
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
            row=9,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 25)
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
            text="Select a file to begin.",
            text_color="#777777",
            font=("Segoe UI", 13)
        )

        self.status_description.pack(
            side="left",
            padx=5,
            pady=12
        )

    # ========================================
    # CHOOSE FILE
    # ========================================

    def choose_file(self):

        file_path = filedialog.askopenfilename(
            title="Select a file"
        )

        if not file_path:
            return

        self.selected_file = file_path

        file_name = os.path.basename(file_path)

        self.file_label.configure(
            text=file_name,
            text_color="#FFFFFF"
        )

        self.status_label.configure(
            text="●  File Selected",
            text_color="#4CAF50"
        )

        self.status_description.configure(
            text=f"Ready to encrypt: {file_name}"
        )

    # ========================================
    # STATUS HELPER
    # ========================================

    def set_status(self, title, description, color):

        self.status_label.configure(
            text=title,
            text_color=color
        )

        self.status_description.configure(
            text=description
        )

    # ========================================
    # XOR FILE PROCESSING
    # ========================================

    def xor_process_file(self, input_file, output_file, key):

        with open(input_file, "rb") as source:

            data = source.read()

        processed_data = bytes(
            byte ^ key
            for byte in data
        )

        with open(output_file, "wb") as destination:

            destination.write(processed_data)

    # ========================================
    # CAESAR FILE PROCESSING
    # ========================================

    def caesar_process_file(
        self,
        input_file,
        output_file,
        key,
        decrypt_mode=False
    ):

        with open(input_file, "rb") as source:

            data = source.read()

        if decrypt_mode:

            processed_data = bytes(
                (byte - key) % 256
                for byte in data
            )

        else:

            processed_data = bytes(
                (byte + key) % 256
                for byte in data
            )

        with open(output_file, "wb") as destination:

            destination.write(processed_data)

    # ========================================
    # VIGENERE FILE PROCESSING
    # ========================================

    def vigenere_process_file(
        self,
        input_file,
        output_file,
        key,
        decrypt_mode=False
    ):

        key_bytes = key.encode("utf-8")

        if not key_bytes:
            raise ValueError("Vigenère key cannot be empty.")

        with open(input_file, "rb") as source:

            data = source.read()

        processed = bytearray()

        for index, byte in enumerate(data):

            key_byte = key_bytes[index % len(key_bytes)]

            if decrypt_mode:

                new_byte = (byte - key_byte) % 256

            else:

                new_byte = (byte + key_byte) % 256

            processed.append(new_byte)

        with open(output_file, "wb") as destination:

            destination.write(processed)

    # ========================================
    # VALIDATE KEY
    # ========================================

    def validate_key(self, algorithm, key):

        if not key:

            self.set_status(
                "●  Error",
                "Please enter an encryption key.",
                "#FF5555"
            )

            return None

        # --------------------------------
        # Caesar
        # --------------------------------

        if algorithm == "Caesar Cipher":

            try:

                numeric_key = int(key)

                if numeric_key < 0 or numeric_key > 255:

                    raise ValueError

                return numeric_key

            except ValueError:

                self.set_status(
                    "●  Error",
                    "Caesar key must be a number between 0 and 255.",
                    "#FF5555"
                )

                return None

        # --------------------------------
        # XOR
        # --------------------------------

        if algorithm == "XOR Cipher":

            try:

                numeric_key = int(key)

                if numeric_key < 0 or numeric_key > 255:

                    raise ValueError

                return numeric_key

            except ValueError:

                self.set_status(
                    "●  Error",
                    "XOR key must be a number between 0 and 255.",
                    "#FF5555"
                )

                return None

        # --------------------------------
        # Vigenère
        # --------------------------------

        if algorithm == "Vigenère Cipher":

            if not key.isascii() or not key.isalpha():

                self.set_status(
                    "●  Error",
                    "Vigenère key must contain letters only.",
                    "#FF5555"
                )

                return None

            return key

        return None

    # ========================================
    # CREATE ENCRYPTED OUTPUT FILE
    # ========================================

    def get_encrypted_output_path(self):

        directory = os.path.dirname(
            self.selected_file
        )

        filename = os.path.basename(
            self.selected_file
        )

        output_file = os.path.join(
            directory,
            filename + ".encrypted"
        )

        return output_file

    # ========================================
    # CREATE DECRYPTED OUTPUT FILE
    # ========================================

    def get_decrypted_output_path(self):

        directory = os.path.dirname(
            self.selected_file
        )

        filename = os.path.basename(
            self.selected_file
        )

        if filename.endswith(".encrypted"):

            original_filename = filename[:-10]

        else:

            original_filename = filename

        output_file = os.path.join(
            directory,
            "decrypted_" + original_filename
        )

        return output_file

    # ========================================
    # ENCRYPT FILE
    # ========================================

    def encrypt_file(self):

        # --------------------------------
        # Check File
        # --------------------------------

        if not self.selected_file:

            self.set_status(
                "●  Error",
                "Please select a file first.",
                "#FF5555"
            )

            return

        # --------------------------------
        # Get Algorithm
        # --------------------------------

        algorithm = self.algorithm_menu.get()

        # --------------------------------
        # Get Key
        # --------------------------------

        key = self.key_entry.get().strip()

        validated_key = self.validate_key(
            algorithm,
            key
        )

        if validated_key is None:

            return

        key = validated_key

        # --------------------------------
        # Create Output
        # --------------------------------

        output_file = self.get_encrypted_output_path()

        try:

            # --------------------------------
            # Caesar Cipher
            # --------------------------------

            if algorithm == "Caesar Cipher":

                self.caesar_process_file(
                    self.selected_file,
                    output_file,
                    key,
                    decrypt_mode=False
                )

            # --------------------------------
            # Vigenère Cipher
            # --------------------------------

            elif algorithm == "Vigenère Cipher":

                self.vigenere_process_file(
                    self.selected_file,
                    output_file,
                    key,
                    decrypt_mode=False
                )

            # --------------------------------
            # XOR Cipher
            # --------------------------------

            elif algorithm == "XOR Cipher":

                self.xor_process_file(
                    self.selected_file,
                    output_file,
                    key
                )

            else:

                self.set_status(
                    "●  Error",
                    "Unsupported encryption algorithm.",
                    "#FF5555"
                )

                return

            # --------------------------------
            # Success
            # --------------------------------

            output_name = os.path.basename(
                output_file
            )

            input_name = os.path.basename(
                self.selected_file
            )

            self.set_status(
                "●  Success",
                f"Encrypted file created: {output_name}",
                "#4CAF50"
            )

            # --------------------------------
            # Add History
            # --------------------------------

            self.winfo_toplevel().history.add_history(
                algorithm,
                "Encrypt File",
                key,
                input_name,
                output_name
            )

        except Exception as error:

            self.set_status(
                "●  Error",
                f"Encryption failed: {error}",
                "#FF5555"
            )

    # ========================================
    # DECRYPT FILE
    # ========================================

    def decrypt_file(self):

        # --------------------------------
        # Check File
        # --------------------------------

        if not self.selected_file:

            self.set_status(
                "●  Error",
                "Please select an encrypted file first.",
                "#FF5555"
            )

            return

        # --------------------------------
        # Get Algorithm
        # --------------------------------

        algorithm = self.algorithm_menu.get()

        # --------------------------------
        # Get Key
        # --------------------------------

        key = self.key_entry.get().strip()

        validated_key = self.validate_key(
            algorithm,
            key
        )

        if validated_key is None:

            return

        key = validated_key

        # --------------------------------
        # Create Output
        # --------------------------------

        output_file = self.get_decrypted_output_path()

        try:

            # --------------------------------
            # Caesar Cipher
            # --------------------------------

            if algorithm == "Caesar Cipher":

                self.caesar_process_file(
                    self.selected_file,
                    output_file,
                    key,
                    decrypt_mode=True
                )

            # --------------------------------
            # Vigenère Cipher
            # --------------------------------

            elif algorithm == "Vigenère Cipher":

                self.vigenere_process_file(
                    self.selected_file,
                    output_file,
                    key,
                    decrypt_mode=True
                )

            # --------------------------------
            # XOR Cipher
            # --------------------------------

            elif algorithm == "XOR Cipher":

                self.xor_process_file(
                    self.selected_file,
                    output_file,
                    key
                )

            else:

                self.set_status(
                    "●  Error",
                    "Unsupported decryption algorithm.",
                    "#FF5555"
                )

                return

            # --------------------------------
            # Success
            # --------------------------------

            output_name = os.path.basename(
                output_file
            )

            input_name = os.path.basename(
                self.selected_file
            )

            self.set_status(
                "●  Success",
                f"Decrypted file created: {output_name}",
                "#4CAF50"
            )

            # --------------------------------
            # Add History
            # --------------------------------

            self.winfo_toplevel().history.add_history(
                algorithm,
                "Decrypt File",
                key,
                input_name,
                output_name
            )

        except Exception as error:

            self.set_status(
                "●  Error",
                f"Decryption failed: {error}",
                "#FF5555"
            )