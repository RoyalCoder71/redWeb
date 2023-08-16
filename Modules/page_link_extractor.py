
import os
import sys
import time
import random
import requests
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
# --My modules--
from Modules.Designing_Module.banner import Banner
from Modules.Designing_Module.color import Color

class LinkExtractor:
    def link_extractor():
        try:
            # Clear the terminal screen
            os.system("clear")

            # Banner
            Banner.banner4()

            print(Fore.WHITE + Style.BRIGHT + f"                     {Back.RED}[!*] Alert! Hide Your IP First [*!]" + Back.RESET)
            print()
            
            # User Input:
            urls = input(Fore.LIGHTGREEN_EX + " +[+[ Set Target Link(example.com) :>> ")
            full_url = "https://" + urls

            # Sending requests & Getting Response
            response = requests.get(full_url) 
            # Reading all html content
            soup = BeautifulSoup(response.text, 'html.parser') 

            # traverse paragraphs from soup
            print(
                f"{Fore.LIGHTYELLOW_EX} Working on process. Please wait for the response.... {Fore.RESET}\n")
        
            colors = Color.colors # class:"Color" > all_the_colors > run

            # System is sleeping for 5 sec.
            time.sleep(5)

            count = 0
            for link in soup.find_all("a"):
                count += 1
                data = link.get('href')
                data = str(data)
                time.sleep(0.3)
                print(colors[random.randint(1, 10)] +f"Output[{count}] " +  data)
            
            # For Going Back to Menu:
            try:
                input(Fore.GREEN+"Back To Menu [:PRESS ENTER:] ")
            except:
                print("")
                sys.exit()

        except Exception:
            print(Fore.LIGHTRED_EX + "\n[(err) !Expected exit code 0 but 1 found]\n")

# _____________COMPLETE___________WORK________________
   
