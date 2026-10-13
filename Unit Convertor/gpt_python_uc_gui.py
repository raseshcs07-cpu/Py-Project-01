
import customtkinter as ctk
from datetime import datetime

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ModernDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NEXUS | Dashboard")
        self.geometry("1100x700")
        self.minsize(850, 600)
        self.configure(fg_color="#0B1020")

        self.tasks = []

        # Main layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()
        self.show_page("Dashboard")

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
            fg_color="#11182B"
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        ctk.CTkLabel(
            self.sidebar,
            text="✦  NEXUS",
            font=("Arial", 25, "bold"),
            text_color="#65A9FF"
        ).pack(pady=(35, 8))

        ctk.CTkLabel(
            self.sidebar,
            text="YOUR WORKSPACE",
            font=("Arial", 10, "bold"),
            text_color="#7F8BA5"
        ).pack(pady=(15, 20))

        self.nav_buttons = {}

        for name, icon in [
            ("Dashboard", "⌂"),
            ("My Tasks", "✓"),
            ("Analytics", "▥"),
            ("Settings", "⚙")
        ]:
            button = ctk.CTkButton(
                self.sidebar,
                text=f"   {icon}    {name}",
                anchor="w",
                height=45,
                corner_radius=10,
                fg_color="transparent",
                hover_color="#263651",
                text_color="#DCE6F7",
                font=("Arial", 14),
                command=lambda page=name: self.show_page(page)
            )
            button.pack(fill="x", padx=15, pady=5)
            self.nav_buttons[name] = button

        ctk.CTkLabel(
            self.sidebar,
            text="BUILT WITH PYTHON",
            font=("Arial", 10),
            text_color="#65738E"
        ).pack(side="bottom", pady=25)

    def create_main_area(self):
        self.main = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="#0B1020"
        )
        self.main.grid(row=0, column=1, sticky="nsew")
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(1, weight=1)

        # Top bar
        self.topbar = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )
        self.topbar.grid(
            row=0, column=0, sticky="ew",
            padx=35, pady=(25, 10)
        )
        self.topbar.grid_columnconfigure(0, weight=1)

        self.page_title = ctk.CTkLabel(
            self.topbar,
            text="Dashboard",
            font=("Arial", 28, "bold"),
            text_color="#F1F5FF"
        )
        self.page_title.grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            self.topbar,
            text=datetime.now().strftime("%d %b %Y"),
            font=("Arial", 12),
            text_color="#8E9BB5"
        ).grid(row=0, column=1, padx=10)

        # Page content
        self.content = ctk.CTkScrollableFrame(
            self.main,
            fg_color="transparent",
            scrollbar_button_color="#34425D"
        )
        self.content.grid(
            row=1, column=0, sticky="nsew",
            padx=25, pady=(5, 20)
        )
        self.content.grid_columnconfigure(0, weight=1)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_page(self, page):
        self.page_title.configure(text=page)
        self.clear_content()

        for name, button in self.nav_buttons.items():
            button.configure(
                fg_color="#263B5D" if name == page else "transparent"
            )

        if page == "Dashboard":
            self.dashboard_page()
        elif page == "My Tasks":
            self.tasks_page()
        elif page == "Analytics":
            self.analytics_page()
        elif page == "Settings":
            self.settings_page()

    def dashboard_page(self):
        ctk.CTkLabel(
            self.content,
            text="Welcome back! 👋",
            font=("Arial", 23, "bold"),
            text_color="#F1F5FF"
        ).grid(row=0, column=0, sticky="w", pady=(15, 5))

        ctk.CTkLabel(
            self.content,
            text="Manage your work, track progress and stay focused.",
            font=("Arial", 13),
            text_color="#8E9BB5"
        ).grid(row=1, column=0, sticky="w", pady=(0, 20))

        # Statistics cards
        cards = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )
        cards.grid(row=2, column=0, sticky="ew", pady=5)
        cards.grid_columnconfigure((0, 1, 2), weight=1)

        completed = sum(1 for task in self.tasks if task["done"])
        total = len(self.tasks)

        stats = [
            ("TOTAL TASKS", str(total), "#65A9FF"),
            ("COMPLETED", str(completed), "#55D6A5"),
            ("REMAINING", str(total - completed), "#F4BC68")
        ]

        for i, (title, value, color) in enumerate(stats):
            card = ctk.CTkFrame(
                cards,
                fg_color="#151E33",
                corner_radius=15
            )
            card.grid(
                row=0, column=i, sticky="ew",
                padx=6, pady=5
            )

            ctk.CTkLabel(
                card, text=title,
                font=("Arial", 10, "bold"),
                text_color="#8E9BB5"
            ).pack(anchor="w", padx=15, pady=(18, 5))

            ctk.CTkLabel(
                card, text=value,
                font=("Arial", 30, "bold"),
                text_color=color
            ).pack(anchor="w", padx=15, pady=(0, 18))

        # Quick task entry
        ctk.CTkLabel(
            self.content,
            text="Quick Add",
            font=("Arial", 18, "bold"),
            text_color="#F1F5FF"
        ).grid(row=3, column=0, sticky="w", pady=(25, 10))

        entry_frame = ctk.CTkFrame(
            self.content,
            fg_color="#151E33",
            corner_radius=12
        )
        entry_frame.grid(row=4, column=0, sticky="ew")
        entry_frame.grid_columnconfigure(0, weight=1)

        self.task_entry = ctk.CTkEntry(
            entry_frame,
            placeholder_text="What do you need to do?",
            height=43,
            fg_color="#1B263D",
            border_color="#2C3B57"
        )
        self.task_entry.grid(
            row=0, column=0, sticky="ew",
            padx=(12, 8), pady=12
        )
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        ctk.CTkButton(
            entry_frame,
            text="+ Add Task",
            width=115,
            height=43,
            corner_radius=9,
            command=self.add_task
        ).grid(row=0, column=1, padx=(0, 12), pady=12)

        # Recent tasks
        ctk.CTkLabel(
            self.content,
            text="Recent Tasks",
            font=("Arial", 18, "bold"),
            text_color="#F1F5FF"
        ).grid(row=5, column=0, sticky="w", pady=(25, 10))

        self.task_list = ctk.CTkFrame(
            self.content,
            fg_color="#151E33",
            corner_radius=12
        )
        self.task_list.grid(row=6, column=0, sticky="ew")
        self.task_list.grid_columnconfigure(0, weight=1)

        self.refresh_task_list()

    def refresh_task_list(self):
        for widget in self.task_list.winfo_children():
            widget.destroy()

        if not self.tasks:
            ctk.CTkLabel(
                self.task_list,
                text="No tasks yet. Add your first task above!",
                text_color="#8E9BB5"
            ).grid(row=0, column=0, pady=22)
            return

        for i, task in enumerate(self.tasks[-5:]):
            index = len(self.tasks) - min(len(self.tasks), 5) + i

            checkbox = ctk.CTkCheckBox(
                self.task_list,
                text=task["name"],
                font=("Arial", 13),
                text_color="#8E9BB5" if task["done"] else "#E0E8F7",
                hover_color="#4B91E2",
                checkbox_width=20,
                checkbox_height=20,
                command=lambda idx=index: self.toggle_task(idx)
            )
            checkbox.grid(
                row=i, column=0, sticky="w",
                padx=18, pady=12
            )

            if task["done"]:
                checkbox.select()

    def add_task(self):
        name = self.task_entry.get().strip()

        if not name:
            return

        self.tasks.append({"name": name, "done": False})
        self.task_entry.delete(0, "end")
        self.show_page("Dashboard")

    def toggle_task(self, index):
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.show_page("Dashboard")

    def tasks_page(self):
        ctk.CTkLabel(
            self.content,
            text="All your tasks in one place.",
            font=("Arial", 14),
            text_color="#8E9BB5"
        ).pack(anchor="w", pady=(15, 20))

        for i, task in enumerate(self.tasks):
            row = ctk.CTkFrame(
                self.content,
                fg_color="#151E33",
                corner_radius=10
            )
            row.pack(fill="x", pady=5)

            checkbox = ctk.CTkCheckBox(
                row,
                text=task["name"],
                command=lambda idx=i: self.toggle_task(idx)
            )
            checkbox.pack(side="left", padx=15, pady=15)

            if task["done"]:
                checkbox.select()

            ctk.CTkButton(
                row,
                text="Delete",
                width=70,
                fg_color="#702D3D",
                hover_color="#983B50",
                command=lambda idx=i: self.delete_task(idx)
            ).pack(side="right", padx=12, pady=10)

        if not self.tasks:
            ctk.CTkLabel(
                self.content,
                text="Your task list is empty.",
                text_color="#8E9BB5"
            ).pack(pady=30)

    def delete_task(self, index):
        self.tasks.pop(index)
        self.show_page("My Tasks")

    def analytics_page(self):
        completed = sum(1 for task in self.tasks if task["done"])
        total = len(self.tasks)
        remaining = total - completed
        progress = completed / total if total else 0

        ctk.CTkLabel(
            self.content,
            text="Your productivity overview",
            font=("Arial", 17),
            text_color="#8E9BB5"
        ).pack(anchor="w", pady=(15, 20))

        for title, value in [
            ("Total tasks", total),
            ("Completed tasks", completed),
            ("Remaining tasks", remaining)
        ]:
            ctk.CTkLabel(
                self.content,
                text=f"{title}: {value}",
                font=("Arial", 16),
                text_color="#E0E8F7"
            ).pack(anchor="w", pady=10)

        ctk.CTkLabel(
            self.content,
            text=f"Completion: {progress:.0%}",
            font=("Arial", 18, "bold"),
            text_color="#55D6A5"
        ).pack(anchor="w", pady=(20, 10))

        bar = ctk.CTkProgressBar(
            self.content,
            height=15,
            progress_color="#55D6A5"
        )
        bar.pack(fill="x", pady=10)
        bar.set(progress)

    def settings_page(self):
        ctk.CTkLabel(
            self.content,
            text="Appearance",
            font=("Arial", 19, "bold"),
            text_color="#F1F5FF"
        ).pack(anchor="w", pady=(20, 10))

        ctk.CTkLabel(
            self.content,
            text="Choose your preferred theme:",
            text_color="#8E9BB5"
        ).pack(anchor="w", pady=8)

        theme_menu = ctk.CTkOptionMenu(
            self.content,
            values=["Dark", "Light", "System"],
            command=self.change_theme
        )
        theme_menu.set("Dark")
        theme_menu.pack(anchor="w", pady=10)

    def change_theme(self, theme):
        ctk.set_appearance_mode(theme.lower())


if __name__ == "__main__":
    app = ModernDashboard()
    app.mainloop()
