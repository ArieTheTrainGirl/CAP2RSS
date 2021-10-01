import time
import requests
import os
import xml.etree.ElementTree as ET
import PyRSS2Gen
import datetime
ns = {'alert': 'urn:oasis:names:tc:emergency:cap:1.2'}
capserverURL = "https://kj7bre.com/ipaws/server2server_bridge/ipaws.php?pin=209fbab696dcbe0adac2491335475a50&feed=eas"



def pollCAP():
    return requests.get(capserverURL).content

rssitemlist = []

rss = PyRSS2Gen.RSS2(
title = "WDFARadio IPAWSCAP RSS Alert Feed",
link = "https://www.wdfaradio.com/alerts/ipaws.html",
description = "FEMA's Integrated Public Alert Warning System in an RSS feed, brought to you by WDFARadio.com.",
items = rssitemlist
)

while True:
    xml = ET.fromstring(pollCAP())
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
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("Polled IPAWS and wrote to RSS at " + current_time)
    except:
        print("FEMA IPAWS failed to write to XML...")
    time.sleep(30)
    rssitemlist.clear()
