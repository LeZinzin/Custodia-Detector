Custodia-Detector - Version 1.0
By: @LeZinzin

Github: https://github.com/LeZinzin
Thanks for using my tools!
Overview

Custodia-Detector is a Python-based tool designed to scan files for suspicious patterns and potentially malicious code. It can detect a wide range of suspicious code patterns in various types of files including Python, JavaScript, PowerShell, Batch, PHP, and HTML.

This tool is useful for developers, security analysts, or anyone who wants to ensure that their codebase is free of harmful code snippets, potentially malicious operations, or exploits.
Features

    Multi-language detection: Scans Python, JavaScript, PowerShell, Batch, PHP, and HTML files for suspicious patterns.
    Customizable patterns: Easily update and add custom patterns to extend the scanner's functionality.
    Log generation: Creates a detailed log file with scan results for further analysis.
    Cross-platform compatibility: Runs on both Windows and Linux systems.
    Clean output: The scanner provides clear outputs and generates logs that are easy to read.

Requirements

    Python 3.x
    This tool is written in Python, so you'll need Python installed on your system.

    Libraries required:
    The following Python libraries are used:
        re (Regular Expressions)
        os
        time
        unicodedata
        datetime

If you're missing any of these libraries, you can install them using pip:

pip install -r requirements.txt

Installation

    Clone the repository: You can download the project from GitHub using git clone:

git clone https://github.com/LeZinzin/Custodia-Detector.git

Install dependencies: Make sure you have the required Python libraries. If you are using requirements.txt, you can install them using:

    pip install -r requirements.txt

    Place Custodia-Detector.py and the script in the same folder
    Ensure the script Custodia-Detector.py exists in the same directory where you run the batch or Python command.

Usage
Running the Tool

    Windows:
        Open a Command Prompt and navigate to the folder containing the script.
        Run the batch file run.bat or execute the following command:

    python Custodia-Detector.py

Linux:

    Open a terminal and navigate to the folder where the script is located.
    Run the Python script directly:

        python3 Custodia-Detector.py

Scanning Files

When you run the tool, you will be prompted to enter the file path of the file you wish to scan.

    Enter the full path to the file you want to scan, for example:

    /path/to/your/file.py

    The tool will then process the file and check for suspicious patterns based on the type of file (e.g., Python, JavaScript, PHP).

    Output:
        If suspicious patterns are found, the tool will generate a log file in the logs directory.
        If no suspicious patterns are found, it will let you know that the file is clean.

File Types Supported

    Python (.py files): Searches for dangerous functions like eval(), exec(), subprocess, os.system(), and more.
    JavaScript (.js files): Scans for eval(), XMLHttpRequest, and other dangerous client-side functions.
    PowerShell (.ps1 files): Looks for malicious PowerShell commands such as Invoke-Expression, Start-Process, etc.
    Batch (.bat files): Detects potentially harmful commands like powershell -nop, cmd.exe /c, and more.
    PHP (.php files): Scans for potentially dangerous PHP functions like eval(), exec(), and base64_decode().
    HTML (.html files): Looks for embedded JavaScript or suspicious src attributes.

Example Output

When the tool detects suspicious code, it will output the following message:

[!] Suspicious pattern found at line 23: eval(
[+] Matches: ['eval(somePotentiallyHarmfulCode());']

This information will also be saved in a log file within the logs/ directory for further inspection.
Log Files

The tool will create a log file in a folder called logs/ inside the working directory. Each log file will contain detailed information about:

    The file scanned
    Timestamp of the scan
    Suspicious patterns found
    Exact matches and the line numbers where they were found

Log file name format:
<filename>_scan_<timestamp>.log

Example log file content:

By @LeZinzin - Version 1.0
Github: https://github.com/LeZinzin
Thanks for using my tools!

CustodiaScan results for /path/to/your/file.py
CustodiaTimestamp: 2024-11-18 10:20:30

[!] Suspicious pattern found at line 23: eval(
[+] Matches: ['eval(somePotentiallyHarmfulCode());']

Troubleshooting

    Python not found:
    If the tool can't find Python in your system PATH, please ensure Python is installed and added to the system PATH environment variable.

    Missing file:
    Ensure the file you're trying to scan exists in the specified location. If the file is missing, the tool will prompt you with an error.

    Permissions issue:
    On Linux, ensure the script has permission to execute and access the file you want to scan. You can adjust permissions using:

    chmod +x Custodia-Detector.py

License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
Credits

    Developed by @LeZinzin
    Inspired by the need for easier detection of potentially malicious code in various languages.

Contributing

Feel free to open issues and pull requests if you'd like to contribute to the project or suggest new features. Contributions are always welcome!