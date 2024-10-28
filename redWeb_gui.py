
# Import the required libraries
import time
import ipapi
import requests
from tkinter import *
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style






# Link Extractor Function
def link_extract():
    try:
        # Making Text Widget Writable
        text.config(state=NORMAL)


        # Banner Inserting to text widget
        text.insert(END, """\n              
====================================================================
                    [+[+[+  Website Link Extractor +]+]+]          
                    Developed by: Royal Coder 71                   
                    Developer Version: 1.2.24LTx0                    
====================================================================\n
""")
        

        # https://example.com
        full_url = "http://" + entry.get()    

        # Sending requests & Getting Response
        response = requests.get(full_url) 
        # Reading all html content
        soup = BeautifulSoup(response.text, 'html.parser')         
        
        # Inserting Informations to Text Widget
        text.insert(INSERT, f"\n\n-----------Target's Information Found!-----------")
        count = 0
        for link in soup.find_all("a"):
            count += 1
            data = link.get('href')
            data = str(data)                
            text.insert(END, f"\n Link:[{count}] " +  data)
            time.sleep(0.1)

        # Cursor remain at last
        text.see(END)

        # Making Text Widget Read-Only or !Writable
        text.config(state=DISABLED)


    except Exception:

        # Inserting Informations to Text Widget
        text.insert(END, "\n\nError Found! You Should Enter only Domain to extract Links\n\n")

        # Cursor remain at last
        text.see(END)

        # Making Text Widget Read-Only or !Writable
        text.config(state=DISABLED)





# DNS-Hook Function
def hook_dns():
    try:
        # Making Text Widget Writable
        text.config(state=NORMAL)


        # Banner Inserting to text widget
        text.insert(END, """\n              
====================================================================
                    [+[+[+     HOOK DNS NOW    +]+]+]          
                    Developed by: Royal Code 71                   
                    Developer Version: 1.2.24LTx0                    
====================================================================\n
""")
         

        # User Input:
        user_input = entry.get()

        # Api
        url = f"https://api.hackertarget.com/dnslookup/?q={user_input}"

        # Response
        response = requests.get(url)
        data = response.text

        # Inserting Informations to Text Widget
        text.insert(END, f"\n\n-----------Target's Information Found!-----------\n " +  data)

        # Cursor remain at last
        text.see(END)

        # Making Text Widget Read-Only or !Writable
        text.config(state=DISABLED)


    except Exception:

        # Inserting Informations to Text Widget
        text.insert(END, "\n\nError Found! You Should Enter only Domain to get DNS Info\n\n")

        # Cursor remain at last
        text.see(END)

        # Making Text Widget Read-Only or !Writable
        text.config(state=DISABLED)






def geoLocation():
    try:
        # Making Text Widget Writable
        text.config(state=NORMAL)


        # Banner Inserting to text widget
        text.insert(END, """\n              
====================================================================
                    [+[+[+ Geolocation Grabber  +]+]+]          
                    Developed by: Royal Coder 71                   
                    Developer Version: 1.2.24LTx0                    
====================================================================\n
""") 

        # User Input:
        target_ip = entry.get()    

        # Api      
        geoTracker = ipapi.location(ip=target_ip)
        
        # Cracked Informations:
        ip = geoTracker["ip"]
        city = geoTracker["city"]
        region = geoTracker["region"]
        postal = geoTracker["postal"]
        country = geoTracker["country"]
        longitude = geoTracker["longitude"]
        latitude = geoTracker["latitude"]
        
        # Inserting Informations to Text Widget
        text.insert(END, f"\n\n-----------Target's Information Found!----------- \n" +  f"IP: {ip} \n" + f"City: {city} \n" + f"Region: {region} \n" + f"Postal: {postal} \n" + f"Country: {country} \n" + f"Longitude: {longitude} \n" + f"Latitude: {latitude} \n")
        
        # Cursor remain at last
        text.see(END)

        # Making Text Widget Read-Only or !Writable
        text.config(state=DISABLED)


    except Exception:

        # Inserting Informations to Text Widget
        text.insert(END, "\n\nError Found! You Should Put an IP address correctly to get IP location\n\n")

        # Cursor remain at last
        text.see(END)

        # Making Text Widget Read-Only or !Writable
        text.config(state=DISABLED)



def whois_report():
        try:
            # Making Text Widget Writable
            text.config(state=NORMAL)
            

            # Banner Inserting to text widget
            text.insert(END, """\n              
====================================================================
                    [+[+[+ Whois Report Checker +]+]+]          
                    Developed by: Royal Coder 71                   
                    Developer Version: 1.2.24LTx0                    
====================================================================\n
""")   


             # Api data:
            api_key = "555adb7fa5616fb5a7bc437bfdb0c40c00a58ea2dc313fdbf3604b1d43b59bbe"        
            api_url = 'https://www.virustotal.com/api/v3/domains/'

            # User Input:
            target_domain = entry.get()
            full_url = api_url + target_domain


            # Request Header:
            headers = {
                "accept": "application/json",
                "x-apikey": f"{api_key}"
            }

             # ================================================ Get Response & convert to json ======================================================================================================
            response = requests.get(full_url, headers=headers)
            json_response = response.json()

            # ================================================ Whois Report ======================================================================================================
            text.insert(END, "\n\n====================== Whois Report ======================\n\n")
            try:
                whois = json_response["data"]["attributes"]["whois"]
                text.insert(END, whois)  
            except Exception:
                text.insert(END, "NO Whois Report Found, Use another Website")
                pass     
            
            # Cursor remain at last
            text.see(END)

            # Making Text Widget Read-Only or !Writable
            text.config(state=DISABLED)

        except Exception:
            # Inserting Informations to Text Widget
            text.insert(END,"\nError Found! You Should Enter only Domain to get Domain Report\n")

            # Cursor remain at last
            text.see(END)

            # Making Text Widget Read-Only or !Writable
            text.config(state=DISABLED)


def malware_report():
    try:
        # Making Text Widget Writable
        text.config(state=NORMAL)
            

        # Banner Inserting to text widget
        text.insert(END, """\n              
====================================================================
                    [+[+[+ Malware Scan Report  +]+]+]          
                    Developed by: Royal Coder 71                   
                    Developer Version: 1.2.24LTx0                    
====================================================================\n
""")      




        # Api data:
        api_key = "555adb7fa5616fb5a7bc437bfdb0c40c00a58ea2dc313fdbf3604b1d43b59bbe"        
        api_url = 'https://www.virustotal.com/api/v3/domains/'

        # User Input:
        target_domain = entry.get()
        full_url = api_url + target_domain


        # Request Header:
        headers = {
            "accept": "application/json",
            "x-apikey": f"{api_key}"
        }

        # ================================================ Get Response & convert to json ======================================================================================================
        response = requests.get(full_url, headers=headers)
        json_response = response.json() 
            
            


        # ================================================ Malware Scanning Report ======================================================================================================
        text.insert(END, "\n\n====================== Malware Scanning Report ======================\n\n")
        try:

            # Scan Result in Summary:
            malicious_report = json_response["data"]["attributes"]["last_analysis_stats"]["malicious"]
            suspicious_report = json_response["data"]["attributes"]["last_analysis_stats"]["suspicious"]
            harmless_report = json_response["data"]["attributes"]["last_analysis_stats"]["harmless"]
            undetected_report = json_response["data"]["attributes"]["last_analysis_stats"]["undetected"]
            text.insert(END, f"Malicious Found: {malicious_report}\nSuspicious Found: {suspicious_report}\nHarmless Found: {harmless_report}\nUndetected Found: {undetected_report}\n")


            text.insert(END, "\n====================== Report in Details ======================\n\n")            
            # Scan Report in Details 
            Engine_Scan_Report = json_response["data"]["attributes"]["last_analysis_results"]
            for single_engine in Engine_Scan_Report:
                engine_name = Engine_Scan_Report[single_engine]['engine_name']
                category_result = Engine_Scan_Report[single_engine]['category']
                text.insert(END, f"[+] Engine Name: [{engine_name}] and Scan Report: [{category_result}]\n")

            # Cursor remain at last
            text.see(END)

            # Making Text Widget Read-Only or !Writable
            text.config(state=DISABLED)
        except Exception:
            text.insert(END, "!!! Scanning Failed Due to Some Reason")     


            # Cursor remain at last
            text.see(END)

            # Making Text Widget Read-Only or !Writable
            text.config(state=DISABLED)

    except Exception:
        # Inserting Informations to Text Widget
        text.insert(END,"\nError Found! You Should Enter only Domain to get Domain Report\n")

        # Cursor remain at last
        text.see(END)

        # Making Text Widget Read-Only or !Writable
        text.config(state=DISABLED)



def clr_screen():
    text.configure(state=NORMAL)
    text.delete("1.0", "end")
    text.configure(state=DISABLED)



# Create an instance of tkinter frame
root = Tk()
root.geometry("1000x695")
root.title("RedWEB Pro 1.2.24LTx0 | Authorized by Royal Coder 71")
root.configure(background="black")
#Set the resizable property False
root.resizable(False, False)




# Create 2 label widgets for showing text
label = Label(root, font=("Helvetica", 23), text="Enter Your Target 'example.com' or 'IP address' ",bg="black", fg="red")
label.grid(padx=45,pady=2, column=0)
label = Label(root, font=("Helvetica", 17, "bold"), text="Developed By Royal Coder 71",bg="black", fg="lime")
label.grid(padx=45,pady=1, column=0)


# Create an entry  widget for user input of domain 
link_var = StringVar()
entry = Entry(root,textvariable = link_var, font=('Helveticaow',20,'normal'), bg="white",fg="black",width=40,insertbackground="green")
entry.grid(padx=45, pady=3, column=0)


# Create a text box Widget to display the response body
text = Text(root, font=("Helvetica", 12), height=29, width=100, wrap="word")
text.grid(padx=45, pady=2, column=0)


# Create Extract and DNS-Hook and Ip-Location and Domain Reporter Button
b1 = Button(root, text="Extract Links", command=link_extract, bg="darkorchid", fg="white")
b1.place(x=80,y=655)

b2 = Button(root, text="Hook the DNS", command=hook_dns, bg="darkorchid", fg="white")
b2.place(x=240,y=655)

b3 = Button(root, text="IP Location", command=geoLocation, bg="darkorchid", fg="white")
b3.place(x=420,y=655)

b4 = Button(root, text="Get Whois Report", command=whois_report, bg="darkorchid", fg="white")
b4.place(x=580,y=655)

b5 = Button(root, text="Check Malware", command=malware_report, bg="darkorchid", fg="white")
b5.place(x=790,y=655)

b6 = Button(root, text="Clear Screen", command=clr_screen, bg="red2", fg="white", height=2, width=10)
b6.place(x=871,y=76)

# Close
root.mainloop()




# Convert python file to exe by auto-py-to-exe 
# Installation Command: "pip install auto-py-to-exe"








