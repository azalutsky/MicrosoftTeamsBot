import pymsteams
import requests
import re
import os

ip_address = ""

# this is the easiest way to get the exact ip address (whatsmyipaddress actually modifies it)
url = 'https://api.ipify.org'
try:
    response = requests.get(url)
    ip_address = response.text.strip()
    print("IP Address found: {}",ip_address)
except:
    print("Couldn't figure out IP address!")
    return

# Check .ipaddress for an already existing ipaddress we have read in
filename = os.path.expanduser("/home/ebots/.ipaddress")
try:
    with open(filename, "r") as f:
        stored_ip_address = f.read().strip()
except FileNotFoundError:
    stored_ip_address = ""

# if the ipaddress we just got is different from the one in the file
# we will modify the file and post the new address to teams
if ip_address != stored_ip_address:
    with open(filename, "w") as f:
        print("Writing to file")
        f.write(ip_address)
        
        # Create a connector object with the webhook URL
        webhook_url = "input webhook id here"
        connector_card = pymsteams.connectorcard(webhook_url)

        # Create a pymsteams_card object and set the title and text
        connector_card.title("New Host Computer Public URL")
        connector_card.text(ip_address)

        # Serialize the card and send the message using the connector
        connector_card.send()
