
import os
import sys
import requests
from colorama import Fore, Back, Style
# --My module--
from Modules.Designing_Module.banner import Banner



class DnsHook:
    def dns_finder():
        try:
            # Clear the terminal screen
            #  In Linux: os.system("clear")
            os.system("clear")

            # Banner:
            Banner.banner5() # calling class "Banner" and function "banner5"

            print(Fore.WHITE + Style.BRIGHT + f"                     {Back.RED}[!*] Alert! Hide Your IP First [*!]" + Back.RESET)
            print()
            
            # User Input:
            user_input = input(Fore.LIGHTGREEN_EX + " +[+[ Set Domain(example.com) :>> ")

            # Api
            url = f"https://api.hackertarget.com/dnslookup/?q={user_input}"

            # Response
            response = requests.get(url)
            data = response.text

            print(Fore.RED + "Output: " + data + Fore.RESET)
            
            # For Going Back to Menu:
            try:
                print(Fore.GREEN + "Back To Menu [:PRESS ENTER:] ")
            except:
                print("")
                sys.exit()

        except Exception:
            print(Fore.LIGHTRED_EX + "\n[(err) !Expected exit code 0 but 1 found]\n")

# _____________COMPLETE___________WORK________________