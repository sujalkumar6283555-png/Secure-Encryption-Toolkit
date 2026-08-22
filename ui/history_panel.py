import customtkinter as ctk


class HistoryPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            width=320,
            corner_radius=15,
            fg_color="#151515",
            border_width=1,
            border_color="#2A2A2A"
        )

        self.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(0, 10),
            pady=10
        )

        self.grid_propagate(False)

        # Store all operations
        self.history_data = []

        # ----------------------------
        # TITLE
        # ----------------------------

        title = ctk.CTkLabel(
            self,
            text="History",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(
            anchor="nw",
            padx=20,
            pady=(20, 15)
        )

        # ----------------------------
        # SEARCH
        # ----------------------------

        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search history...",
            height=38,
            corner_radius=10
        )

        self.search.pack(
            fill="x",
            padx=20
        )

        self.search.bind(
            "<KeyRelease>",
            self.search_history
        )

        # ----------------------------
        # SCROLL AREA
        # ----------------------------

        self.history_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.history_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=20
        )

        # ----------------------------
        # CLEAR BUTTON
        # ----------------------------

        self.clear_btn = ctk.CTkButton(
            self,
            text="Clear History",
            height=42,
            fg_color="#B71C1C",
            hover_color="#8B0000",
            command=self.clear_history
        )

        self.clear_btn.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

    # ========================================
    # ADD HISTORY
    # ========================================

    def add_history(
        self,
        algorithm,
        action,
        key="",
        input_text="",
        output_text=""
    ):

        item = {
            "algorithm": algorithm,
            "action": action,
            "key": str(key),
            "input": input_text,
            "output": output_text
        }

        # Newest operation goes to the beginning
        self.history_data.insert(0, item)

        self.refresh_history()

    # ========================================
    # REFRESH HISTORY
    # ========================================

    def refresh_history(self, data=None):

        # Remove existing cards
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        if data is None:
            data = self.history_data

        # ----------------------------
        # Create cards
        # ----------------------------

        for item in data:

            card = ctk.CTkFrame(
                self.history_frame,
                corner_radius=12,
                fg_color="#1D1D1D"
            )

            card.pack(
                fill="x",
                pady=6
            )

            # Algorithm
            algorithm_label = ctk.CTkLabel(
                card,
                text=item["algorithm"],
                font=("Segoe UI", 15, "bold")
            )

            algorithm_label.pack(
                anchor="w",
                padx=15,
                pady=(10, 2)
            )

            # Action
            action_label = ctk.CTkLabel(
                card,
                text=item["action"],
                text_color="#FF4040",
                font=("Segoe UI", 13, "bold")
            )

            action_label.pack(
                anchor="w",
                padx=15,
                pady=(0, 5)
            )

            # Key
            if item["key"]:

                key_label = ctk.CTkLabel(
                    card,
                    text=f"Key: {item['key']}",
                    text_color="#AAAAAA",
                    font=("Segoe UI", 12)
                )

                key_label.pack(
                    anchor="w",
                    padx=15,
                    pady=(0, 3)
                )

            # Input
            input_preview = str(item["input"])

            if len(input_preview) > 25:
                input_preview = input_preview[:25] + "..."

            input_label = ctk.CTkLabel(
                card,
                text=f"Input: {input_preview}",
                text_color="#888888",
                font=("Segoe UI", 11),
                wraplength=260
            )

            input_label.pack(
                anchor="w",
                padx=15,
                pady=(0, 3)
            )

            # Output
            output_preview = str(item["output"])

            if len(output_preview) > 25:
                output_preview = output_preview[:25] + "..."

            output_label = ctk.CTkLabel(
                card,
                text=f"Output: {output_preview}",
                text_color="#888888",
                font=("Segoe UI", 11),
                wraplength=260
            )

            output_label.pack(
                anchor="w",
                padx=15,
                pady=(0, 10)
            )

    # ========================================
    # SEARCH
    # ========================================

    def search_history(self, event=None):

        query = self.search.get().strip().lower()

        if not query:
            self.refresh_history()
            return

        filtered_data = []

        for item in self.history_data:

            searchable_text = (
                str(item["algorithm"]) + " " +
                str(item["action"]) + " " +
                str(item["key"]) + " " +
                str(item["input"]) + " " +
                str(item["output"])
            ).lower()

            if query in searchable_text:
                filtered_data.append(item)

        self.refresh_history(filtered_data)

    # ========================================
    # CLEAR HISTORY
    # ========================================

    def clear_history(self):

        self.history_data.clear()

        self.refresh_history()