import time
import requests
import os
import xml.etree.ElementTree as ET
import PyRSS2Gen
import datetime
ns = {'alert': 'urn:oasis:names:tc:emergency:cap:1.2'}
capserverURL = "https://kj7bre.com/ipaws/server2server_bridge/ipaws.php?pin=209fbab696dcbe0adac2491335475a50&feed=eas"



# tree = ET.parse("sample.xml")
# root = tree.getroot()

def pollCAP():
    return requests.get(capserverURL).content

xml = ET.fromstring(pollCAP())
print(xml)

rssitemlist = []

rss = PyRSS2Gen.RSS2(
title = "IPAWSCAP RSS Feed",
link = "https://www.wdfaradio.com/alerts/ipaws.html",
description = "Integrated Public Alert Warning System Common Alert Protocol RSS feed.",
items = rssitemlist
)

while True:

    for alerts in xml.findall('./alert:alert', ns):
        try:
            CAPidentifier = alerts.find('alert:identifier', ns).text
            CAPsender = alerts.find('alert:sender', ns).text
            CAPinfo = alerts.find('alert:info', ns).text
            for info in alerts.findall('alert:info', ns):
                CAPdescription = info.find('alert:description', ns).text
                CAPevent = info.find('alert:event', ns).text
                print(CAPevent)
                rssitemlist.append(
                    PyRSS2Gen.RSSItem(
                    title = CAPevent,
                    link = "https://www.wdfaradio.com/",
                    description = CAPdescription,
                    ),
                )
        except:
            print("rip bozo")
    try:
        rss.write_xml(open("eas.xml", "w"))
        print("FEMA IPAWS successfully converted to RSS!")
    except:
        print("FEMA IPAWS failed to write to XML...")
    time.sleep(60)
