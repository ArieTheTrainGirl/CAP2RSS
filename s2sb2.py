import requests
import time

polltime = 60 # Poll every x seconds
weas2sb = "https://kj7bre.com/ipaws/server2server_bridge/ipaws.php?pin=209fbab696dcbe0adac2491335475a50&feed=wea"
eass2sb = "https://kj7bre.com/ipaws/server2server_bridge/ipaws.php?pin=209fbab696dcbe0adac2491335475a50&feed=eas"

while True:
        try:
            r1 = requests.get(weas2sb)
            r2 = requests.get(eass2sb)
        except: 
            print('Error encountered while polling the S2SB server! Exiting cleanly...')
            exit(1)
        try:    
            with open('weas2sb.xml', 'wb') as f:
                f.write(r1.content)
            with open('eass2sb.xml', 'wb') as f:
                f.write(r1.content)
        except:
            print('Error encountered while writing the XML file! Exiting cleanly...')
            exit(2)
        
        print('Polled from server and saved!')
        time.sleep(polltime)
