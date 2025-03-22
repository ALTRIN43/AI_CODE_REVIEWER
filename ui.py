import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from speech import listen_command
from compiler import analyze_file

def create_ui(root):
    # Heading
    label = ctk.CTkLabel(root, text="Code Reviewer - GIT-Pushers", font=("Arial", 22, "bold"))
    label.pack(pady=20)

    # File Review Button
    btn_review = ctk.CTkButton(root, text="📂 Select and Review File", command=analyze_file, width=300, height=40)
    btn_review.pack(pady=10)

    # Voice Command Button
    btn_voice = ctk.CTkButton(root, text="🎙 Use Voice Command", command=listen_command, width=300, height=40)
    btn_voice.pack(pady=10)

    # Output Display
    global output_text
    output_text = ctk.CTkTextbox(root, width=600, height=200, font=("Arial", 12), wrap="word")
    output_text.pack(pady=20)
    output_text.insert("1.0", "Errors and corrections will appear here...")
    output_text.configure(state="disabled")

    # Exit Button
    btn_exit = ctk.CTkButton(root, text="❌ Exit", command=root.quit, fg_color="red", width=150, height=40)
    btn_exit.pack(pady=10)

    return output_text
