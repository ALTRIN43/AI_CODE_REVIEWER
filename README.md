# 🚀 AI Code Reviewer

## 📌 Description  
AI-powered code review tool that automatically analyzes and fixes syntax errors in Python, C, C++, and Java files. It supports **voice commands**, uses **Google Gemini AI** for intelligent corrections, and provides **real-time feedback** through a GUI.  

## 🌟 Features  
✅ Supports Python, C, C++, and Java file analysis  
✅ Detects and fixes syntax errors automatically  
✅ Voice commands for hands-free operation  
✅ Text-to-Speech (TTS) for responses  
✅ GUI built with **CustomTkinter**  
✅ Uses **Google Gemini AI** for smart code correction  

## 🛠️ Technologies Used  
- **Python**  
- **CustomTkinter** (for GUI)  
- **SpeechRecognition** (for voice commands)  
- **pyttsx3** (for text-to-speech)  
- **Google Gemini AI** (for AI-powered code fixing)  
- **subprocess** (for running compilers)  
- **Regular Expressions** (for extracting errors)  

## ⚙️ Installation  
1. **Clone the Repository**  
   ```sh
   git clone https://github.com/yourusername/ai-code-reviewer.git
   cd ai-code-reviewer
   ```
   

## Set Up Google Gemini AI API Key
Open config.py and replace YOUR_GEMINI_API_KEY with your actual API key.

## Usage
   **Run the project:** <br>
         cd python main.py
         

2. **Click 📂 Select and Review File to choose a file for analysis.**
3. **Click 🎙️ Use Voice Command and say:** <br>
      "Review file" → to analyze a code file<br>
      "Exit now" → to close the application

4. **View the corrected errors in the output panel.**

5. ## ⚡ How It Works

* User selects a code file (Python, C, C++, Java).<br>
* Code is analyzed using subprocess to catch compilation errors.<br>
* Errors are extracted using regex and mapped to line numbers.<br>
* Google Gemini AI fixes the errors and updates the file.<br>
* Voice feedback is provided using pyttsx3.<br>

## 📌 Example Output:
<br>
Errors Found & Fixed in example.py:

Line 3: print("Hello World"<br>
  → ERROR: SyntaxError: unexpected EOF while parsing<br>
✅ Fixed Code Saved!<br>

## 🛠️ Customization
Modify speech rate in voice_commands.py:<br>
engine.setProperty('rate', 150)  # Change to preferred speed<br>
Add support for other programming languages in code_analyzer.py.<br>

## 🔧 Troubleshooting
🔹 No errors detected but code doesn’t run?
<br>
Ensure your code logic is correct; this tool only fixes syntax errors.<br>
🔹 Voice commands not working?<br>
Check your microphone and try again in a quieter environment.<br>

## 🚀 Future Enhancements
🔹 Add support for JavaScript, PHP, and Rust<br>
🔹 Improve AI corrections with more context-aware fixes<br>
🔹 Enhance UI design with better themes<br>

## Author
ALTRIN - Developer & Maintainer

## 📜 License
This project is licensed under the MIT License
