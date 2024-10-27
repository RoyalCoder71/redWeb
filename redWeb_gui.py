
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





# Create an instance of tkinter frame
root = Tk()
root.geometry("1000x695")
root.title("RedWEB Pro 1.0.24-cTx0 | Authorized by Royal Coder 71")
root.configure(background="black")
#Set the resizable property False
root.resizable(False, False)




# Create 2 label widgets for showing text
label = Label(root, font=("Helvetica", 23), text="Enter Your Target 'example.com' or 'IP address' ",bg="black", fg="red")
label.grid(padx=45,pady=2, column=0)
label = Label(root, font=("Helvetica", 17, "bold"), text="Developed By Royal Coder 71",bg="black", fg="yellow")
label.grid(padx=45,pady=1, column=0)


# Create an entry  widget for user input of domain 
link_var = StringVar()
entry = Entry(root,textvariable = link_var, font=('Helveticaow',20,'normal'), bg="white",fg="black",width=40,insertbackground="green")
entry.grid(padx=45, pady=3, column=0)


# Create a text box Widget to display the response body
text = Text(root, font=("Helvetica", 12), height=29, width=100, wrap="word")
text.grid(padx=45, pady=2, column=0)


# Create Extract and DNS-Hook and Ip-Location Button
b1 = Button(root, text="Extract Links", command=link_extract)
b1.place(x=250,y=655)

b2 = Button(root, text="Hook the DNS", command=hook_dns)
b2.place(x=450,y=655)

b3 = Button(root, text="IP Location", command=geoLocation)
b3.place(x=660,y=655)




# Close
root.mainloop()




# Convert python file to exe by auto-py-to-exe 
# Installation Command: "pip install auto-py-to-exe"








