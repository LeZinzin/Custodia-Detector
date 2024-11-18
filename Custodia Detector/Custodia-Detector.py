# By @LeZinzin - Version 1.0 
# Github : https://github.com/LeZinzin
# Thanks for using my tools !

import re
import os
from datetime import datetime
import time
import unicodedata
from func.config import Custodia, CustodiaBanner, CustodiaCreator, CustodiaClear

os.system("title Custodia Detector (1.0)")

CustodiaCreator()
time.sleep(1)
CustodiaClear()
CustodiaBanner()
time.sleep(0.5)

suspicious_patterns = {
    'python': [
        r"import\s+(os|sys|subprocess|shutil|socket|requests|platform|hashlib|re)",  
        r"eval\(", 
        r"exec\(", 
        r"subprocess\.",  
        r"os\.system\(",  
        r"open\(", 
        r"base64\.b64decode\(",  
        r"pickle\.load\(",  
        r"socket\.connect\(",  
        r"import\s+(ctypes|win32api)",  
        r"getattr\(",  
        r"setattr\(", 
        r"__import__\(", 
        r"import\s+(shutil|ctypes|ctypes.windll)",  
        r"os\.popen\(",  
        r"subprocess\.Popen\(",  
        r"exec\(\s*\'\s*import\s+.*\'", 
        r"eval\s*\(\s*.*\)\s*", 
        r"base64\.b64encode\(", 
        r"urllib\.request\.urlopen\(", 
        r"requests\.get\(",  
        r"socket\.send\(",  
        r"open\(\s*'.*\.exe'",  
        r"subprocess\.call\(", 
        r"request\.post\(",   
        r"import\s+(ctypes|pywin32)", 
        r"import\s+(psutil|win32com|pywin32)", 
        r"eval\(\s*globals\(", 
        r"subprocess\.check_output\(", 
        r"shutil\.rmtree\(", 
        r"os\.remove\(", 
        r"os\.rename\(",  
        r"os\.unlink\(", 
        r"subprocess\.call\(\s*['\"].*['\"]\)",  
        r"shutil\.move\(",  
        r"socket\.recv\(",  
    ],
    'javascript': [
        r"eval\(",  
        r"setTimeout\(",  
        r"setInterval\(",  
        r"document\.write\(",  
        r"XMLHttpRequest\(",  
        r"window\.atob\(",  
        r"Function\(",  
        r"$.ajax\(",  
        r"window\.location\s*=\s*['\"].*['\"]",  
        r"Function\s*\(",  
        r"document\.cookie\s*=",  
        r"src\s*=\s*['\"]data:.*['\"]",  
        r"eval\s*\(.*\)\s*;", 
        r"window\.open\(",  
        r"document\.createElement\('script'\)",  
        r"window\.setInterval\(",  
        r"window\.location\s*=\s*['\"].*\.exe['\"]", 
        r"javascript:.*\s*alert\(", 
        r"eval\(\s*String\(\s*fromCharCode\s*\(",  
        r"window\.postMessage\(",  
        r"window\.location\s*=\s*['\"]http[s]?\:\/\/.*['\"]",  
        r"document\.cookie\s*=\s*['\"]?.*['\"]", 
    ],
    'powershell': [
        r"Invoke-Expression",  
        r"Start-Process",  
        r"Invoke-WebRequest",  
        r"New-Object\s+Net.WebClient",  
        r"iex\s+",  
        r"powershell\s+-nop",  
        r"powershell\s+-ep\s+Bypass",  
        r"bypass\s+executionpolicy",  
        r"cmd.exe\s+/c\s+.*",  
        r"Add-Type\s+-TypeDefinition",  
        r"New-Object\s+System\.Diagnostics\.Process",  
        r"echo\s+.*|.*\s+Invoke-Expression", 
        r"net\s+user\s+.*",  
        r"wget\s+.*\s+exec",  
        r"Invoke-Command\s+.*\s+scriptblock",  
        r"Get-WmiObject",  
        r"Get-Content\s+.*\s+|.*\s+Invoke-Expression",  
        r"New-Object\s+System\.IO\.FileInfo",  
        r"Add-Content\s+.*\s+|.*\s+Invoke-Expression",  
    ],
    'batch': [
        r"powershell\s+-nop",  
        r"cmd\.exe\s+/c",  
        r"del\s+",  
        r"rmdir\s+/s\s+/q",  
        r"start\s+.*\.vbs",  
        r"start\s+.*\.js",  
        r"mshta\s+.*",  
        r"start\s+.*\.exe",  
        r"echo\s.*|.*\s+cmd",  
        r"wget\s+.*\s+exec",  
        r"reg\s+add\s+.*\s+/f",  
        r"reg\s+add\s+.*\s+/v\s+.*\s+/d\s+.*\s+/f",  
        r"start\s+http[s]?:\/\/.*",  
        r"start\s+ftp\s+.*",  
        r"powershell\s+-ep\s+unrestricted",  
        r"cmd\.exe\s+\/c\s+.*\s+set\s+\%.*\s*=\s*.*",  
    ],
    'php': [
        r"eval\(",  
        r"exec\(",  
        r"shell_exec\(",  
        r"system\(",  
        r"passthru\(",  
        r"popen\(",  
        r"proc_open\(",  
        r"base64_decode\(",  
        r"assert\(", 
        r"preg_replace\s*\(.*\)/e", 
        r"system\('.*'\)",  
        r"base64_encode\(",  
        r"curl\s*.*\s+exec",  
        r"file_get_contents\(",  
        r"phpinfo\(",  
        r"file_put_contents\(",  
        r"$_GET\['.*'\]",  
        r"$_POST\['.*'\]",  
        r"shell_exec\(\s*['\"].*['\"]\)",  
        r"fopen\(\s*['\"].*\.exe['\"]\)",  
        r"unlink\(\s*['\"].*['\"]\)",  
        r"system\(\s*['\"].*\.exe['\"]\)", 
    ],
    'html': [
        r"javascript:",  
        r"onerror=",  
        r"onload=",  
        r"eval\(",  
        r"document\.write\(",  
        r"src\s*=\s*['\"]data:.*['\"]",  
        r"src\s*=\s*['\"]javascript:.*['\"]", 
        r"onmouseover=",  
        r"setTimeout\(", 
        r"setInterval\(", 
        r"window\.open\(",  
        r"javascript:.*\s*alert\(", 
        r"document\.cookie\s*=\s*['\"].*['\"]",  
        r"src\s*=\s*['\"]http://.*['\"]",  
        r"src\s*=\s*['\"]https?:\/\/.*\.exe['\"]", 
        r"src\s*=\s*['\"]http:\/\/.*\s*base64\s*['\"]",  
        r"src\s*=\s*['\"]javascript:.*\s*prompt\(",  
        r"eval\(\s*unescape\s*\(",  
        r"eval\(\s*String\(\s*fromCharCode\s*\(",  
    ]
}


def detect_malicious_code(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    file_type = get_file_type(file_path)
    if file_type not in suspicious_patterns:
        print(f"{Custodia.Yellow}[!] No pattern set for file type: {file_type}{Custodia.Reset}")
        return
    
    log_entries = []
    line_number = 1
    for line in content.splitlines():
        for pattern in suspicious_patterns[file_type]:
            matches = re.findall(pattern, line)
            if matches:
                log_entries.append(f"{Custodia.Red}[!] Suspicious pattern found at line {line_number}: {pattern}{Custodia.Reset}")
                log_entries.append(f"{Custodia.Cyan}[+] Matches: {matches}{Custodia.Reset}")
        line_number += 1

    if log_entries:
        create_log_file(file_path, log_entries)

def get_file_type(file_path):
    if file_path.endswith('.py'):
        return 'python'
    elif file_path.endswith('.js'):
        return 'javascript'
    elif file_path.endswith('.ps1'):
        return 'powershell'
    elif file_path.endswith('.bat'):
        return 'batch'
    elif file_path.endswith('.php'):
        return 'php'
    elif file_path.endswith('.html'):
        return 'html'
    else:
        return 'unknown'

def sanitize_text(text):
    normalized_text = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in normalized_text if ord(c) < 128])

def create_log_file(file_path, log_entries):
    log_dir = 'logs'  
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file_name = os.path.join(log_dir, f"{os.path.basename(file_path)}_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    
    try:
        with open(log_file_name, 'w', encoding='utf-8') as log_file:
            log_file.write(f"""By @LeZinzin - Version 1.0 
Github : https://github.com/LeZinzin
Thanks for using my tools !\n\n""")
            log_file.write(f"CustodiaScan results for {file_path}\n")
            log_file.write(f"CustodiaTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            for entry in log_entries:
                sanitized_entry = sanitize_text(entry)
                log_file.write(sanitized_entry + "\n")
        
        print(f"{Custodia.Green}[+] Log file created: {log_file_name}{Custodia.Reset}")
        
        open_log_file(log_file_name)
    except IOError as e:
        print(f"{Custodia.Red}[!] Error while creating log file: {e}{Custodia.Reset}")

def open_log_file(log_file_name):
    if os.name == 'nt':  
        os.startfile(log_file_name)  
    elif os.name == 'posix': 
        try:
            os.system(f'xdg-open "{log_file_name}"') 
        except Exception as e:
            print(f"{Custodia.Red}[!] Error opening log file: {e}{Custodia.Reset}")
            os.system(f'open "{log_file_name}"')  
    else:
        print(f"{Custodia.Red}[!] Unable to open log file. Please open it manually: {log_file_name}{Custodia.Reset}")

if __name__ == "__main__":
    file_path = input(f"{Custodia.Magenta}-> Enter the file path to scan: {Custodia.Reset}")
    detect_malicious_code(file_path)
