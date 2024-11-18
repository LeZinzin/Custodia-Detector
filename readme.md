![CustodiaDetector](https://github.com/user-attachments/assets/81d516fd-21ca-4e6b-8212-b44c86244b76)


---


# 🌟 **Custodia-Detector - Version 1.0**  
*By: @LeZinzin*  

[GitHub Repository](https://github.com/LeZinzin)  
Thanks for using my tool! 🙌

---

### 📌 **Overview**  
**Custodia-Detector** is a Python-based tool designed to scan files for suspicious patterns and potentially malicious code. It supports multiple file types, including Python, JavaScript, PowerShell, Batch, PHP, and HTML, making it an essential tool for developers, security analysts, and anyone wanting to ensure their code is free from harmful snippets or exploits.

---

### 🚀 **Features**  
- **Multi-Language Support:** Detects suspicious code in Python, JavaScript, PowerShell, Batch, PHP, and HTML files.
- **Customizable Patterns:** Easily extend the scanner by adding custom patterns to match your needs.
- **Detailed Logs:** Generates a detailed log file with results for further analysis.
- **Cross-Platform:** Works on both **Windows** and **Linux**.
- **Clean Output:** Provides clear, human-readable outputs and logs.

---

### 🧑‍💻 **Usage**

#### 1. **Running the Tool**
- **Windows:**  
  Open Command Prompt, navigate to the folder with the script, and run:
  ```bash
  python Custodia-Detector.py
  ```

- **Linux:**  
  Open a terminal, navigate to the folder, and run:
  ```bash
  python3 Custodia-Detector.py
  ```

#### 2. **Scanning Files**  
When prompted, input the full path of the file you want to scan:
```plaintext
/path/to/your/file.py
```

The tool will process the file and check for suspicious patterns based on its type (e.g., Python, JavaScript, PHP). If anything is detected, a log file will be created with details about the suspicious code.

---

### 🔍 **File Types Supported**

- **Python (.py):** Detects dangerous functions like `eval()`, `exec()`, `subprocess`, `os.system()`, and more.
- **JavaScript (.js):** Identifies `eval()`, `XMLHttpRequest`, and other risky client-side functions.
- **PowerShell (.ps1):** Scans for malicious PowerShell commands like `Invoke-Expression`, `Start-Process`, etc.
- **Batch (.bat):** Detects harmful commands like `powershell -nop`, `cmd.exe /c`, and others.
- **PHP (.php):** Flags dangerous PHP functions such as `eval()`, `exec()`, `base64_decode()`.
- **HTML (.html):** Searches for embedded JavaScript or suspicious `src` attributes.

---

### 📊 **Example Output**

When suspicious code is found, you’ll see an output like this:

```plaintext
[!] Suspicious pattern found at line 23: eval(
[+] Matches: ['eval(somePotentiallyHarmfulCode());']
```

This will also be saved in a log file for later inspection.

---

### 📝 **Log Files**

The tool generates a log file inside the **logs/** directory. Each log includes:
- **File Scanned**  
- **Timestamp**  
- **Suspicious Patterns Found**  
- **Matches and Line Numbers**

**Log File Format:**  
`<filename>_scan_<timestamp>.log`

Example log content:

```plaintext
By @LeZinzin - Version 1.0  
Github: https://github.com/LeZinzin  
Thanks for using my tools!

CustodiaScan results for /path/to/your/file.py  
CustodiaTimestamp: 2024-11-18 10:20:30

[!] Suspicious pattern found at line 23: eval(
[+] Matches: ['eval(somePotentiallyHarmfulCode());']
```

---

### ⚙️ **Troubleshooting**

- **Python Not Found:**  
  Ensure Python is installed and added to your system's PATH.
  
- **Missing File:**  
  Double-check the file path you're trying to scan. The tool will alert you if the file is missing.

- **Permissions Issue (Linux):**  
  If you encounter permission issues, run:
  ```bash
  chmod +x Custodia-Detector.py
  ```

---

### 📑 **License**  
This project is open-source under the MIT License. See the LICENSE file for more details.

---

### 🙏 **Credits**  
- Developed by @LeZinzin  
- Inspired by the need for efficient detection of potentially malicious code across multiple languages.

---

### 💬 **Contributing**  
Feel free to contribute by opening issues or submitting pull requests. Your input and suggestions are always welcome!  

---

**Enjoy using Custodia-Detector!** 🎉

---
