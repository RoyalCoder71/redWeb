from colorama import Fore
# --My modules--
from Modules.Designing_Module.banner import Banner
from Modules.geolocation import GeoLocation
from Modules.page_link_extractor import LinkExtractor
from Modules.dnsHook import DnsHook
from Modules.checkReport import CheckReport

# Banner
Banner.banner1()

print(Fore.YELLOW + "      \n+[+[ Choose Profile for Target ]+]+\n")
print(Fore.RED + "[1] GeoLocation Traker")
print(Fore.GREEN + "[2] HHR Breaker")
print(Fore.LIGHTBLACK_EX + "[3] Page Link Extractor")
print(Fore.CYAN + "[4] DNS Hook")
print(Fore.BLUE + "[5] Domain Reporter")

# User Input:
user_demand = int(input(Fore.LIGHTMAGENTA_EX + "\n[Set your demand :>> " + Fore.RESET))
def redWeb():
    try:
        if user_demand == 1:
            GeoLocation.geolocation()                
        elif user_demand == 2:
            pass
        elif user_demand == 3:
            LinkExtractor.link_extractor()           
        elif user_demand == 4:
            DnsHook.dns_finder()
        elif user_demand == 5:
            CheckReport.domain_report()
    except Exception:
         print(Fore.LIGHTRED_EX + "\n[(err) !Expected exit code 0 but 1 found]\n")



# Calling function:
redWeb()