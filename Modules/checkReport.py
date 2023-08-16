import os
import sys
import requests
from colorama import Fore, Back, Style
# --My module--
from Modules.Designing_Module.banner import Banner

class CheckReport:  
    def domain_report():
        try:
            # Clear the terminal screen
            os.system("clear")

            # Banner:
            Banner.banner6() # calling class "Banner" and function "banner6"

            print(Fore.WHITE + Style.BRIGHT + f"                     {Back.RED}[!*] Alert! Hide Your IP First [*!]" + Back.RESET)
            print()
            
            # Api data:
            api_key = "{Your API Key}"        
            api_url = 'https://www.virustotal.com/vtapi/v2/domain/report'

            # User Input:
            target_domain = input(Fore.RED + "+[+[ Set Target Domain(example.com) :>> ")

            # Get response:
            parameters = {'apikey':api_key,'domain':target_domain}
            response = requests.get(api_url, params = parameters)
            json_response = response.json()
            # print(json_response)

                    
            # Access to json_response:
            sub_domains = json_response["subdomains"]
            who_is = json_response["whois"]
            resolutions = json_response['resolutions']
            category = json_response["alphaMountain.ai category"]

                    

            # WebSite Informations:
            print(Fore.YELLOW + "================+[+[ WebSite's Informations ]+]+===============")
            print(who_is)
            print()


            # Category of Website:
            print(Fore.GREEN + "==================+[+[ WebSite's Catagory ]+]+=================")
            print(category)
            print()


            # Subdomain Finder:
            print(Fore.CYAN + "=================+[+[ WebSite's Subdomains ]+]+================")
            i = 0
            for subdomain in sub_domains:
                i += 1
                print(f"Subdomain-{i}: {subdomain}")
            print()

            # More Informations:
            print(Fore.RED + "==================+[+[ More informations ]+]+==================")
            for data in resolutions:
                ip_address = data["ip_address"]
                last_updated = data["last_resolved"]
                print(f"IP Address: {ip_address}, Last Updated: {last_updated}")
            print(Fore.RESET)


            # For Going Back to Menu:
            try:
                input(Fore.GREEN + "Back To Menu [:PRESS ENTER:] ")
            except:
                print("")
                sys.exit()

        except Exception:
            print(Fore.RED + "\n[(err) !Expected exit code 0 but 1 found]\n")
            
# _____________COMPLETE___________WORK________________



