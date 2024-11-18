# By @LeZinzin - Version 1.0 
# Github : https://github.com/LeZinzin
# Thanks for using my tools !

import time 
import sys
import os
import platform

def CustodiaClear():
    system_name = platform.system().lower()

    if system_name == "windows":
        os.system("cls")  
    elif system_name in ["linux", "darwin"]:  
        os.system("clear")
    else:
        print("\n" * 100) 

class Custodia():
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Black = '\033[90m'
    Reset = '\033[0m'

def CustodiaCreator():
    banner = f"""{Custodia.Yellow}
                                [By LeZinzin]
    _____________________________________________________________________________
    |This tool scans files for suspicious patterns and potential malicious code,| 
    |including backdoors, dual hooks, obfuscation techniques, and various types | 
    |of malware. It works across multiple languages such as Python, JavaScript, |  
    |PowerShell, PHP, and more.                                                 |
    |                                                                           |
    |It will identify and flag the following:                                   |
    |- Malicious execution patterns (e.g., eval, exec, subprocess)              |
    |- Suspicious commands and file operations (e.g., os.system, subprocess)    |
    |- Potential backdoors (e.g., system calls, user creation)                  |
    |- Obfuscation techniques (e.g., base64 encoding, dynamic eval calls)       |
    |                                                                           |
    |If a malicious pattern is found, it will log the results and attempt to    |
    |automatically open the log file for you.                                   |
    |                                                                           |
    |GitHub: https://github.com/LeZinzin                                        |
    |___________________________________________________________________________|
{Custodia.Reset}"""
    
    for line in banner.splitlines():
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.1)  

def CustodiaBanner():
    banner = f"""{Custodia.Yellow}
   ______           __            ___          
  / ____/_  _______/ /_____  ____/ (_)___ _    
 / /   / / / / ___/ __/ __ \/ __  / / __ `/    
/ /___/ /_/ (__  ) /_/ /_/ / /_/ / / /_/ /     
\____/\__,_/____/\__/\____/\__,_/_/\__,_/      
    ____       __            __                
   / __ \___  / /____  _____/ /_____  _____    
  / / / / _ \/ __/ _ \/ ___/ __/ __ \/ ___/    
 / /_/ /  __/ /_/  __/ /__/ /_/ /_/ / /        
/_____/\___/\__/\___/\___/\__/\____/_/ (1.0)        
                                               """
    
    for line in banner.splitlines():
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.1) 

