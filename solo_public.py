from email.utils import collapse_rfc2231_value
from turtle import colormode
import psutil
import path
import time
from colorama import Fore
import colorama
import os

os.system('title Solo Public Session Creater')

process_found = False
colorama.init(True)


print(Fore.LIGHTCYAN_EX + """
█▀ █▀█ █░░ █▀█   █▀█ █░█ █▄▄ █░░ █ █▀▀   █▀ █▀▀ █▀ █▀ █ █▀█ █▄░█   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀█
▄█ █▄█ █▄▄ █▄█   █▀▀ █▄█ █▄█ █▄▄ █ █▄▄   ▄█ ██▄ ▄█ ▄█ █ █▄█ █░▀█   █▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▀▄\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

def is_gta(f_name):
    if f_name.lower() == 'gta5.exe':
        return True
    return False
print(Fore.LIGHTWHITE_EX+ ">>> Scanning Processes <<<")
for process in psutil.process_iter():
    file = path.Path(process.name())
    if is_gta(f_name=file.name):
        print(Fore.LIGHTWHITE_EX + ">>> Suspending GTA Process <<<")
        process.suspend()
        time.sleep(9)
        print(Fore.LIGHTWHITE_EX + ">>> Resuming GTA Process <<<")
        process.resume()
        process_found = True
        break
    
if process_found is False:
    print(Fore.LIGHTRED_EX +"""> Could not detect GTA5.exe""")
    while True:
        pass


print(Fore.LIGHTYELLOW_EX + "Created Solo Public Session")

while True:
    pass