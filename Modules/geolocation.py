
# from [module] import [class]
import os
import sys
import time
import ipapi
from colorama import Fore, Back, Style
# --My module--
from Modules.Designing_Module.banner import Banner



class GeoLocation: # class 'Geolocation'
    def geolocation(): # function 'geolocation' in class "Gelolocation"
        try:

            # Clear the terminal screen
            os.system("clear")

            # Banner:
            Banner.banner2() # calling class "Banner" and function "banner2"

            print(Fore.WHITE + Style.BRIGHT + f"                     {Back.RED}[!*] Alert! Hide Your IP First [*!]" + Back.RESET)
            print()

            # User Input:
            target_ip = input(Fore.LIGHTGREEN_EX + " +[+[ Set Target Ip :>> ")

            # # HackerTarget api
            # urls = "https://api.hackertarget.com/ipgeo/?q={}".format(target_ip)
            # response = requests.get(urls)
            # print(response.text)

            # json request getting by ipapi.location()
            geoTracker = ipapi.location(ip=target_ip)

            print(
                f"{Fore.LIGHTYELLOW_EX} Working on process. Please wait for the response.... {Fore.RESET}\n")
            time.sleep(5.0)  # system sleping for 5 sec.

            # Cracked Informations:
            ip = geoTracker["ip"]
            city = geoTracker["city"]
            region = geoTracker["region"]
            postal = geoTracker["postal"]
            country = geoTracker["country"]
            longitude = geoTracker["longitude"]
            latitude = geoTracker["latitude"]
            # google_api_key = "AIzaSyD5TbwN_zheFV8cM5ZcpDdCNipEAV9LEMA"

            print(
                "======================[Target Information]==========================")
            # print(geoTracker)
            print(Fore.LIGHTGREEN_EX + "[!] Victim's IP     :>> {}".format(ip))
            print(Fore.LIGHTMAGENTA_EX + "[!] Victim's City   :>> {}".format(city))
            print(Fore.LIGHTCYAN_EX + "[!] Victim's Region :>> {}".format(region))
            print(Fore.LIGHTRED_EX + "[!]Victim's postal  :>> {}".format(postal))
            print(Fore.LIGHTBLUE_EX +
                "[!]Victim's Country :>> {}".format(country))
            print(Fore.LIGHTYELLOW_EX + "[!]Victim's latitude  :>> {}".format(latitude))
            print(Fore.LIGHTRED_EX + "[!]Victim's longtitude  :>> {}".format(longitude) + Fore.RESET)

           # For Going Back to Menu:
            try:
                input(Fore.GREEN + "Back To Menu [:PRESS ENTER:] ")
            except:
                print("")
                sys.exit()
            
        except Exception:
                print(Fore.LIGHTRED_EX + "\n[(err) !Expected exit code 0 but 1 found]\n")


# _____________COMPLETE___________WORK________________

