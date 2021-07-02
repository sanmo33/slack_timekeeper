import os
import datetime
import urllib.request
import webbrowser


def make_scrapbox(scrapbox_junban:str):
    dt = datetime.datetime.now()
    today = dt.strftime('%Y%m%d')

    scrapbox_junban = urllib.parse.quote(scrapbox_junban)

    URL = 'https://scrapbox.io/ishibashi-lab-22/'+today+"?body="+scrapbox_junban

    webbrowser.open(URL)