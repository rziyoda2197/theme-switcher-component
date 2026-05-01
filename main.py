import tkinter as tk
from tkinter import ttk

class ThemeSwitcher:
    def __init__(self, root):
        self.root = root
        self.root.title("Theme Switcher")
        self.root.geometry("300x200")

        self.theme = tk.StringVar()
        self.theme.set("light")

        self.create_widgets()

    def create_widgets(self):
        self.theme_label = tk.Label(self.root, text="Theme:")
        self.theme_label.pack()

        self.theme_option = ttk.OptionMenu(self.root, self.theme, "light", "dark", "system")
        self.theme_option.pack()

        self.apply_button = tk.Button(self.root, text="Apply", command=self.apply_theme)
        self.apply_button.pack()

        self.status_label = tk.Label(self.root, text="Status: ")
        self.status_label.pack()

    def apply_theme(self):
        if self.theme.get() == "light":
            self.root.configure(background="#FFFFFF")
            self.theme_label.configure(background="#FFFFFF", foreground="#000000")
            self.theme_option.configure(background="#FFFFFF", foreground="#000000")
            self.apply_button.configure(background="#FFFFFF", foreground="#000000")
            self.status_label.configure(background="#FFFFFF", foreground="#000000")
        elif self.theme.get() == "dark":
            self.root.configure(background="#000000")
            self.theme_label.configure(background="#000000", foreground="#FFFFFF")
            self.theme_option.configure(background="#000000", foreground="#FFFFFF")
            self.apply_button.configure(background="#000000", foreground="#FFFFFF")
            self.status_label.configure(background="#000000", foreground="#FFFFFF")
        elif self.theme.get() == "system":
            self.root.configure(background=self.root.cget("bg"))
            self.theme_label.configure(background=self.root.cget("bg"), foreground=self.root.cget("fg"))
            self.theme_option.configure(background=self.root.cget("bg"), foreground=self.root.cget("fg"))
            self.apply_button.configure(background=self.root.cget("bg"), foreground=self.root.cget("fg"))
            self.status_label.configure(background=self.root.cget("bg"), foreground=self.root.cget("fg"))

root = tk.Tk()
theme_switcher = ThemeSwitcher(root)
root.mainloop()
