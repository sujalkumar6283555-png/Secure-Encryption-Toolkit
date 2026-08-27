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
    # XOR FILE PROCESSING
    # ========================================

    def xor_process_file(self, input_file, output_file, key):

        with open(input_file, "rb") as source:

            data = source.read()

        encrypted_data = bytes(
            byte ^ key
            for byte in data
        )

        with open(output_file, "wb") as destination:

            destination.write(encrypted_data)

    # ========================================
    # ENCRYPT FILE
    # ========================================

    def encrypt_file(self):

        if not self.selected_file:

            self.status_label.configure(
                text="●  Error",
                text_color="#FF5555"
            )

            self.status_description.configure(
                text="Please select a file first."
            )

            return

        algorithm = self.algorithm_menu.get()
        key = self.key_entry.get().strip()

        # --------------------------------
        # Check Algorithm
        # --------------------------------

        if algorithm != "XOR Cipher":

            self.status_label.configure(
                text="●  Coming Soon",
                text_color="#FFB000"
            )

            self.status_description.configure(
                text=f"{algorithm} file encryption is coming soon."
            )

            return

        # --------------------------------
        # Validate Key
        # --------------------------------

        if not key:

            self.status_label.configure(
                text="●  Error",
                text_color="#FF5555"
            )

            self.status_description.configure(
                text="Please enter an encryption key."
            )

            return

        try:

            key = int(key)

            if key < 0 or key > 255:

                raise ValueError

        except ValueError:

            self.status_label.configure(
                text="●  Error",
                text_color="#FF5555"
            )

            self.status_description.configure(
                text="XOR key must be a number between 0 and 255."
            )

            return

        # --------------------------------
        # Create Output File
        # --------------------------------

        directory = os.path.dirname(self.selected_file)
        filename = os.path.basename(self.selected_file)

        output_file = os.path.join(
            directory,
            filename + ".encrypted"
        )

        try:

            self.xor_process_file(
                self.selected_file,
                output_file,
                key
            )

            self.status_label.configure(
                text="●  Success",
                text_color="#4CAF50"
            )

            self.status_description.configure(
                text=f"Encrypted file created: {os.path.basename(output_file)}"
            )
            self.winfo_toplevel().history.add_history(
                algorithm,
                "Encrypt File",
                key,
                os.path.basename(self.selected_file),
                os.path.basename(output_file)
)

        except Exception as error:

            self.status_label.configure(
                text="●  Error",
                text_color="#FF5555"
            )

            self.status_description.configure(
                text=f"Encryption failed: {error}"
            )

    # ========================================
    # DECRYPT FILE
    # ========================================

    def decrypt_file(self):

        if not self.selected_file:

            self.status_label.configure(
                text="●  Error",
                text_color="#FF5555"
            )

            self.status_description.configure(
                text="Please select an encrypted file first."
            )

            return

        algorithm = self.algorithm_menu.get()
        key = self.key_entry.get().strip()

        # --------------------------------
        # Check Algorithm
        # --------------------------------

        if algorithm != "XOR Cipher":

            self.status_label.configure(
                text="●  Coming Soon",
                text_color="#FFB000"
            )

            self.status_description.configure(
                text=f"{algorithm} file decryption is coming soon."
            )

            return

        # --------------------------------
        # Validate Key
        # --------------------------------

        if not key:

            self.status_label.configure(
                text="●  Error",
                text_color="#FF5555"
            )

            self.status_description.configure(
                text="Please enter the encryption key."
            )

            return

        try:

            key = int(key)

            if key < 0 or key > 255:

                raise ValueError

        except ValueError:

            self.status_label.configure(
                text="●  Error",
                text_color="#FF5555"
            )

            self.status_description.configure(
                text="XOR key must be a number between 0 and 255."
            )

            return

        # --------------------------------
        # Create Decrypted File
        # --------------------------------

        directory = os.path.dirname(self.selected_file)
        filename = os.path.basename(self.selected_file)

        if filename.endswith(".encrypted"):

            original_filename = filename[:-10]

        else:

            original_filename = filename + ".decrypted"

        output_file = os.path.join(
            directory,
            "decrypted_" + original_filename
        )

        try:

            self.xor_process_file(
                self.selected_file,
                output_file,
                key
            )

            self.status_label.configure(
                text="●  Success",
                text_color="#4CAF50"
            )

            self.status_description.configure(
                text=f"Decrypted file created: {os.path.basename(output_file)}"
            )
            self.winfo_toplevel().history.add_history(
                algorithm,
                "Decrypt File",
                key,
                os.path.basename(self.selected_file),
                os.path.basename(output_file)
)

        except Exception as error:

            self.status_label.configure(
                text="●  Error",
                text_color="#FF5555"
            )

            self.status_description.configure(
                text=f"Decryption failed: {error}"
            )