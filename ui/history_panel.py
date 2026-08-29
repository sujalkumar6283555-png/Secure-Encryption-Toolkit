import customtkinter as ctk
import json
import os


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

        # ========================================
        # DATA
        # ========================================

        self.history_data = []
        self.favorites_data = []

        # File used to save favorites
        self.favorites_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "favorites.json"
        )

        self.load_favorites()

        # Current panel mode
        self.show_favorites = False

        # ========================================
        # TITLE
        # ========================================

        self.title = ctk.CTkLabel(
            self,
            text="History",
            font=("Segoe UI", 26, "bold")
        )

        self.title.pack(
            anchor="nw",
            padx=20,
            pady=(20, 15)
        )

        # ========================================
        # SEARCH
        # ========================================

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

        # ========================================
        # SCROLL AREA
        # ========================================

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

        # ========================================
        # CLEAR HISTORY
        # ========================================

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

        # Newest operation first
        self.history_data.insert(0, item)

        self.refresh_history()

    # ========================================
    # ADD TO FAVORITES
    # ========================================

    def add_to_favorites(self, item):

        if item not in self.favorites_data:

            self.favorites_data.append(item)

            self.save_favorites()

            self.refresh_history()

    # ========================================
    # REMOVE FROM FAVORITES
    # ========================================

    def remove_from_favorites(self, item):

        if item in self.favorites_data:

            self.favorites_data.remove(item)

            self.save_favorites()

            self.refresh_history()

    # ========================================
    # CHECK FAVORITE
    # ========================================

    def is_favorite(self, item):

        return item in self.favorites_data

    # ========================================
    # SAVE FAVORITES
    # ========================================

    def save_favorites(self):

        try:

            with open(
                self.favorites_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.favorites_data,
                    file,
                    indent=4
                )

        except Exception as error:

            print(
                f"Could not save favorites: {error}"
            )

    # ========================================
    # LOAD FAVORITES
    # ========================================

    def load_favorites(self):

        if not os.path.exists(self.favorites_file):

            return

        try:

            with open(
                self.favorites_file,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                if isinstance(data, list):

                    self.favorites_data = data

        except Exception as error:

            print(
                f"Could not load favorites: {error}"
            )

            self.favorites_data = []

    # ========================================
    # REFRESH HISTORY
    # ========================================

    def refresh_history(self, data=None):

        # Remove existing cards
        for widget in self.history_frame.winfo_children():

            widget.destroy()

        # Determine what to display
        if data is None:

            if self.show_favorites:

                data = self.favorites_data

            else:

                data = self.history_data

        # ========================================
        # EMPTY STATE
        # ========================================

        if not data:

            empty_label = ctk.CTkLabel(
                self.history_frame,
                text=(
                    "No favorites yet."
                    if self.show_favorites
                    else "No history yet."
                ),
                text_color="#666666",
                font=("Segoe UI", 13)
            )

            empty_label.pack(
                pady=30
            )

            return

        # ========================================
        # CREATE CARDS
        # ========================================

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

            # --------------------------------
            # TOP ROW
            # --------------------------------

            top_frame = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            top_frame.pack(
                fill="x",
                padx=10,
                pady=(8, 0)
            )

            # Algorithm
            algorithm_label = ctk.CTkLabel(
                top_frame,
                text=item["algorithm"],
                font=("Segoe UI", 15, "bold")
            )

            algorithm_label.pack(
                side="left",
                padx=5
            )

            # Favorite button
            if self.is_favorite(item):

                favorite_text = "★"

            else:

                favorite_text = "☆"

            favorite_button = ctk.CTkButton(
                top_frame,
                text=favorite_text,
                width=35,
                height=30,
                corner_radius=7,
                fg_color="transparent",
                hover_color="#333333",
                text_color="#FFD700",
                font=("Segoe UI", 20, "bold"),
                command=lambda current_item=item:
                    self.toggle_favorite(current_item)
            )

            favorite_button.pack(
                side="right"
            )

            # --------------------------------
            # ACTION
            # --------------------------------

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

            # --------------------------------
            # KEY
            # --------------------------------

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

            # --------------------------------
            # INPUT
            # --------------------------------

            input_preview = str(
                item["input"]
            )

            if len(input_preview) > 25:

                input_preview = (
                    input_preview[:25] + "..."
                )

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

            # --------------------------------
            # OUTPUT
            # --------------------------------

            output_preview = str(
                item["output"]
            )

            if len(output_preview) > 25:

                output_preview = (
                    output_preview[:25] + "..."
                )

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
    # TOGGLE FAVORITE
    # ========================================

    def toggle_favorite(self, item):

        if self.is_favorite(item):

            self.remove_from_favorites(item)

        else:

            self.add_to_favorites(item)

    # ========================================
    # SEARCH
    # ========================================

    def search_history(self, event=None):

        query = self.search.get().strip().lower()

        # Get current data source
        if self.show_favorites:

            source_data = self.favorites_data

        else:

            source_data = self.history_data

        if not query:

            self.refresh_history(
                source_data
            )

            return

        filtered_data = []

        for item in source_data:

            searchable_text = (
                str(item["algorithm"]) + " " +
                str(item["action"]) + " " +
                str(item["key"]) + " " +
                str(item["input"]) + " " +
                str(item["output"])
            ).lower()

            if query in searchable_text:

                filtered_data.append(item)

        self.refresh_history(
            filtered_data
        )

    # ========================================
    # SHOW HISTORY
    # ========================================

    def show_history(self):

        self.show_favorites = False

        self.title.configure(
            text="History"
        )

        self.search.configure(
            placeholder_text="Search history..."
        )

        self.clear_btn.configure(
            text="Clear History",
            command=self.clear_history
        )

        self.search.delete(
            0,
            "end"
        )

        self.refresh_history()

    # ========================================
    # SHOW FAVORITES
    # ========================================

    def show_favorites_panel(self):

        self.show_favorites = True

        self.title.configure(
            text="Favorites"
        )

        self.search.configure(
            placeholder_text="Search favorites..."
        )

        self.clear_btn.configure(
            text="Clear Favorites",
            command=self.clear_favorites
        )

        self.search.delete(
            0,
            "end"
        )

        self.refresh_history()

    # ========================================
    # CLEAR HISTORY
    # ========================================

    def clear_history(self):

        self.history_data.clear()

        self.refresh_history()

    # ========================================
    # CLEAR FAVORITES
    # ========================================

    def clear_favorites(self):

        self.favorites_data.clear()

        self.save_favorites()

        self.refresh_history()