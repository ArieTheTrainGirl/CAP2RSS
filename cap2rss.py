import time
import requests
import os
import xml.etree.ElementTree as ET
ns = {'alert': 'urn:oasis:names:tc:emergency:cap:1.2'}
capserverURL = "https://kj7bre.com/ipaws/server2server_bridge/ipaws.php?pin=209fbab696dcbe0adac2491335475a50&feed=public"



# tree = ET.parse("sample.xml")
# root = tree.getroot()

def pollCAP():
    return requests.get(capserverURL).content

xml = ET.fromstring(pollCAP())
print(xml)

for alerts in xml.findall('./alert:alert', ns):
            if alerts.find('alert:msgType', ns).text == "Alert":
                CAPidentifier = alerts.find('alert:identifier', ns).text
                CAPsender = alerts.find('alert:sender', ns).text
                CAPinfo = alerts.find('alert:info', ns).text
                for info in alerts.findall('alert:info', ns):
                    CAPdescription = info.find('alert:description', ns).text
                    CAPevent = info.find('alert:event', ns).text
                    print(CAPevent)

