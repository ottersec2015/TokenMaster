# Modules importation
import os
import base64
import time
import clipboard
import colorama

from colorama import Fore, init
init()

# COLORES

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

# COLORES

# PRINTS

banner = rf"""
{red}    ███      ▄██████▄     ▄█   ▄█▄    ▄████████ ███▄▄▄▄    ▄█  ████████▄  
{red}▀█████████▄ ███    ███   ███ ▄███▀   ███    ███ ███▀▀▀██▄ ███  ███   ▀███ 
{red}   ▀███▀▀██ ███    ███   ███▐██▀     ███    █▀  ███   ███ ███▌ ███    ███  {lred}This scripts is only for fun
{red}    ███   ▀ ███    ███  ▄█████▀     ▄███▄▄▄     ███   ███ ███▌ ███    ███  {lred}and encode UserID to Base64
{red}    ███     ███    ███ ▀▀█████▄    ▀▀███▀▀▀     ███   ███ ███▌ ███    ███  {lred}and the first characters of
{red}    ███     ███    ███   ███▐██▄     ███    █▄  ███   ███ ███  ███    ███  {lred}a DcToken are userID in Base64
{red}    ███     ███    ███   ███ ▀███▄   ███    ███ ███   ███ ███  ███   ▄███ 
{red}   ▄████▀    ▀██████▀    ███   ▀█▀   ██████████  ▀█   █▀  █▀   ████████▀  
{red}                         ▀                                                
{lred}                   github.com/ottersec2015/TokenID
"""

# PRINTS

print(banner)
userid = input("                   USER ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
clipboard.copy(encodedStr)
print(f'                   Token copied to clipboard [PASTE WITH CTRL+V]')
time.sleep(1.5)
print("                   Restarting script in 3 seconds")
time.sleep(3)
os.system('cls && py TokenMaster.py')  # Pause command in Batch (press any key to exit the code)