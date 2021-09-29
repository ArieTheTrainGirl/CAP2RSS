
import requests
import time

polltime = 60 # Poll every x seconds
urls = ['https://kj7bre.com/ipaws/server2server_bridge/ipaws.php?pin=209fbab696dcbe0adac2491335475a50&feed=eas', 'https://kj7bre.com/ipaws/server2server_bridge/ipaws.php?pin=209fbab696dcbe0adac2491335475a50&feed=wea'] # URLs to pull from. 

while True:
    for url in urls:
        try:
            r = requests.get(url)
        except: 
            print('Error encountered while polling the S2SB server! Exiting cleanly...')
            exit(1)
        try:    
            with open('s2sb.xml', 'wb') as f:
                f.write(r.content)
        except:
            print('Error encountered while writing the XML file! Exiting cleanly...')
            exit(2)
        
        print('Polled from server and saved!')
    time.sleep(polltime)