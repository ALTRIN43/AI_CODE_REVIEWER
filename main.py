import customtkinter as ctk
from ui import create_ui

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("AI Code Reviewer")
    root.geometry("700x500")

    create_ui(root)
    root.mainloop()
