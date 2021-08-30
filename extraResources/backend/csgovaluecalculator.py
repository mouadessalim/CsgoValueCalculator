import requests
from bs4 import BeautifulSoup
import json
from sys import argv

SteamID = argv[1]
if SteamID.isdigit():
    valid_response = requests.get(f"https://www.steamidfinder.com/lookup/{SteamID}")
    if valid_response.ok and int(SteamID) > 9999999999999999 :
        response = requests.get("https://csgopedia.com/inventory-value/?profiles=" + SteamID)
        if response.ok:
            page = BeautifulSoup(response.text, features="html.parser")
            rank = page.find("table", class_="table-cell")
            value = rank.find_all("strong")[1].get_text()
            value_float = float(value[1:])
            responseip = requests.get("https://api.techniknews.net/ipgeo/").json()
            if responseip['currency'] == "USD":
                print(str(value_float) + " USD 💰")
            else:
                response = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/{responseip['currency'].lower()}.json").json()
                conversion = response[responseip['currency'].lower()] * value_float
                conversion_finished = round(conversion, 2)
                print(str(conversion_finished) + " " + responseip['currency'] + " 💰")
        else:
            print("Server down ! Please retry later.")          
    else:
        print("SteamID Incorrect")
    response = requests.get("https://csgopedia.com/inventory-value/?profiles=" + SteamID)
else:
    print("SteamID not valid !")