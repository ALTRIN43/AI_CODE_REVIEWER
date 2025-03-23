import subprocess
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from ai_code_fixer import generate_fixed_code
from speech import speak_text

def extract_errors(output):
    errors = []
    for line in output.split("\n"):
        match = re.search(r"([^:]+):(\d+):\d*: (error|warning): (.+)", line)
        if match:
            _, line_number, err_type, error_message = match.groups()
            errors.append((int(line_number), f"{err_type.upper()}: {error_message.strip()}"))
    return sorted(errors, key=lambda x: x[0])

def get_errored_lines(file_path, error_lines):
    errored_lines = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line_num in error_lines:
                if 1 <= line_num <= len(lines):
                    errored_lines[line_num] = lines[line_num - 1].strip()
    except Exception as e:
        print(f"Error reading file: {e}")
    return errored_lines

def analyze_file():
    file_path = filedialog.askopenfilename(filetypes=[("Code Files", "*.py *.c *.cpp *.java")])
    if not file_path:
        return

    extension = file_path.split(".")[-1]
    command = {
        "py": ["python", "-m", "py_compile", file_path],
        "c": ["gcc", "-Wall", "-fsyntax-only", file_path],
        "cpp": ["g++", "-Wall", "-fsyntax-only", file_path],
        "java": ["javac", file_path]
    }.get(extension)

    if not command:
        messagebox.showerror("Error", "Unsupported file type! Use Python, C, C++, or Java.")
        return

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    errors = extract_errors(result.stderr)

    with open(file_path, "r", encoding="utf-8") as f:
        original_code = f.read()

    if errors:
        error_lines = [line_num for line_num, _ in errors]
        errored_code = get_errored_lines(file_path, error_lines)
        fixed_code = generate_fixed_code(original_code, errors)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed_code)

        messagebox.showinfo("Fixed", f"Errors fixed in {file_path}")
        speak_text("Errors fixed. Updated code saved.")
    else:
        messagebox.showinfo("No Errors", "No errors found!")
        speak_text("No errors found in the file.")
