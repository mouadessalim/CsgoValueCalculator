import requests
import webbrowser
import json
import os
from datetime import datetime
import socket
from sys import argv
import sys

def exec_main():
    with open(f"{os.getenv('APPDATA')}\csgo-value-calculator\csgoaccount.json", 'r') as f:
        data = json.load(f)
    with open(f"{os.getenv('APPDATA')}\csgo-value-calculator\historical.txt", 'w') as k:
        k.write("  /$$$$$$                           /$$    /$$        /$$                   /$$$$$$          /$$                  /$$           /$$                      \n")
        k.write(" /$$__  $$                         | $$   | $$       | $$                  /$$__  $$        | $$                 | $$          | $$                      \n")
        k.write("| $$  \__//$$$$$$$ /$$$$$$  /$$$$$$| $$   | $$/$$$$$$| $$/$$   /$$ /$$$$$$| $$  \__/ /$$$$$$| $$ /$$$$$$$/$$   /$| $$ /$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$ \n")
        k.write("| $$     /$$_____//$$__  $$/$$__  $|  $$ / $$|____  $| $| $$  | $$/$$__  $| $$      |____  $| $$/$$_____| $$  | $| $$|____  $|_  $$_/  /$$__  $$/$$__  $$\n")
        k.write("| $$    |  $$$$$$| $$  \ $| $$  \ $$\  $$ $$/ /$$$$$$| $| $$  | $| $$$$$$$| $$       /$$$$$$| $| $$     | $$  | $| $$ /$$$$$$$ | $$   | $$  \ $| $$  \__/\n")
        k.write("| $$    $\____  $| $$  | $| $$  | $$ \  $$$/ /$$__  $| $| $$  | $| $$_____| $$    $$/$$__  $| $| $$     | $$  | $| $$/$$__  $$ | $$ /$| $$  | $| $$      \n")
        k.write("|  $$$$$$/$$$$$$$|  $$$$$$|  $$$$$$/  \  $/ |  $$$$$$| $|  $$$$$$|  $$$$$$|  $$$$$$|  $$$$$$| $|  $$$$$$|  $$$$$$| $|  $$$$$$$ |  $$$$|  $$$$$$| $$      \n")
        k.write(" \______|_______/ \____  $$\______/    \_/   \_______|__/\______/ \_______/\______/ \_______|__/\_______/\______/|__/\_______/  \___/  \______/|__/      \n")
        k.write("                  /$$  \ $$                                                                                                                              \n")
        k.write("                 |  $$$$$$/                                                                                                                              \n")
        k.write("                  \______/                                                                                                                               \n")

        for x, y in data.items():
            if response['currency'] == "EUR":
                k.write("------------------------------------------------------------------\n")
                k.write(str(f"Account name: {y['name']}\n"))
                k.write(str(f"Profile inventory value: {y['value']} EUR\n"))
                k.write(str(f"Steam ID64: {x}\n"))
                k.write(str(f"Custom URL: {y['custom_URL']}\n"))
                k.write(str(f"Profile state: {y['profile_state']}\n"))
                k.write(str(f"Profile created: {y['profile_created']}\n"))
                k.write(str(f"Profile location: {y['location']}\n"))
                k.write(str(f"Profile URL: {y['profile_url']}\n"))
                k.write("------------------------------------------------------------------\n")
            else:
                response_c = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/{response['currency'].lower()}.json").json()
                k.write("------------------------------------------------------------------\n")
                k.write(str(f"Account name: {y['name']}\n"))
                k.write(str(f"Profile inventory value: {round(float(response_c[response['currency'].lower()]) * float(y['value']), 2)} {response['currency']}\n"))
                k.write(str(f"Steam ID64: {x}\n"))
                k.write(str(f"Custom URL: {y['custom_URL']}\n"))
                k.write(str(f"Profile state: {y['profile_state']}\n"))
                k.write(str(f"Profile created: {y['profile_created']}\n"))
                k.write(str(f"Profile location: {y['location']}\n"))
                k.write(str(f"Profile URL: {y['profile_url']}\n"))
                k.write("------------------------------------------------------------------\n")

    params = (
        ('expires', '1w'),
    )
    fileopener = open(f"{os.getenv('APPDATA')}\csgo-value-calculator\historical.txt", 'rb')
    namefile = f'all_csgo-{datetime.now().strftime("%d_%m_%Y")}.txt'
    files = {
        'file': (namefile, fileopener),
    }

    response_u = requests.post('https://file.io/', params=params, files=files)
    response_upload = response_u.json()
    if response_u.ok:
        if response_upload["success"] == True:
            webbrowser.open(response_upload["link"])
            print("your web browser was opened, you can download the file.")

        else:
            print("the app can't upload the file, please retry or contact me.")
    else:
        print("Fatal error detected when communicating with server.")

    fileopener.close()
    os.remove(f"{os.getenv('APPDATA')}\csgo-value-calculator\historical.txt")

def test_connexion():
    try:
        socket.create_connection(('google.com', 80))
        return True
    except:
        return False

def check_server():
    try:
        socket.create_connection(('file.io', 80))
        global response
        check_response = requests.get("https://api.techniknews.net/ipgeo/")
        response = check_response.json()
        if response['status'] == "success" and check_response.ok:
            return True
        else:
            if check_response.ok:
                print("There is something weird with your internet connexion, please check it.")
            else:
                return False
    except:
        return False

def declared():
    try:
        x = argv[1]
        if x == "KEY_FILEIO":
            return True
        else:
            return False
    except:
        return False

if test_connexion() and check_server() and declared():
    exec_main()
else:
    if test_connexion() and declared():
        print("Server down, please retry later.")
    else:
        if declared():
            print("No connexion found, please check it.")
        else:
            try:
                sys.exit()
            except:
                try:
                    quit()
                except:
                    pass