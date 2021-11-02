#uploader.py

import requests
import webbrowser
import json
import os
from datetime import datetime
import socket
from sys import argv
import sys
from discord_webhook import DiscordWebhook, DiscordEmbed

DISCORD_JSON_API = "YOUR DISCORD SERVER API"
DISCORD_WEBHOOK = "YOUR DISCORD WEBHOOK LINK"

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
            k.write("------------------------------------------------------------------\n")
            k.write(str(f"Account name: {y['name']}\n"))
            if currency == "EUR":
                k.write(str(f"Profile inventory value: {y['value']} EUR\n"))
            else:
                k.write(str(f"Profile inventory value: {round(float(response_c[currency.lower()]) * float(y['value']), 2)} {currency}\n"))
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

def exec_discord():
    try:
        n = 0
        while response_discord['members'][n]['username'] != argv[2]:
            n += 1 
        status_members = True    
    except IndexError:
        status_members = False
        print('Pseudo not found, please verify if you are online')

    if status_members:
        content = f"Thanks you **{response_discord['members'][n]['username']}** for using my app, here are the results:"
        #allowed_mentions = {
        #    "parse": ["everyone"]
        #}
        webhook = DiscordWebhook(url=DISCORD_WEBHOOK, username='CsgoValueCalculator', avatar_url='https://pbs.twimg.com/profile_images/1389342981107318785/AL7Ha5E4_400x400.jpg', content=content)
        embed = DiscordEmbed(color='FFFFFF')

        with open(f"{os.getenv('APPDATA')}\csgo-value-calculator\csgoaccount.json", 'r') as f:
            data = json.load(f)

        for x,y in data.items():
            if currency == "EUR":
                value = y['value']
            else:
                value = round(float(response_c[currency.lower()]) * float(y['value']), 2)
            content = str(f"Profile inventory value: {value} {currency}\n") + str(f"Steam ID64: {x}\n") + str(f"Custom URL: {y['custom_URL']}\n") + str(f"Profile state: {y['profile_state']}\n") + str(f"Profile created: {y['profile_created']}\n") + str(f"Profile location: {y['location']}\n") + str(f"Profile URL: {y['profile_url']}")
            embed.add_embed_field(name=y['name'], value=content)

        embed.set_author(name=response_discord['members'][n]['username'], icon_url=response_discord['members'][n]['avatar_url'])
        embed.set_footer(text='Developed by Lemon.-_-.#3714')
        webhook.add_embed(embed)
        webhook.execute()
        print('Success, message sended by the Bot go check the channel!')
    else:
        pass

def test_connexion():
    try:
        socket.create_connection(('google.com', 80))
        return True
    except:
        return False

def check_server():
    global currency
    try:
        socket.create_connection(('file.io', 80))
        global response
        global response_discord
        global response_c
        check_response = requests.get("https://api.techniknews.net/ipgeo/")
        response = check_response.json()
        if check_response.ok:
            currency = response['currency']
        else:
            response_ip_currency = requests.get("https://ipapi.co/currency/")
            if response_ip_currency.ok:
                currency = str(response_ip_currency.text)
        check_response_1 = requests.get(DISCORD_JSON_API)
        response_discord = check_response_1.json()
        check_response_2 = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/{currency.lower()}.json")
        response_c = check_response_2.json()
        if check_response_1.ok and check_response_2.ok:
            return True
        else:
            return False
    except:
        return False

def declared():
    try:
        x = argv[1]
        if x == "KEY_FILEIO" or x=="KEY_DISCORD":
            return True
        else:
            return False
    except:
        return False

if test_connexion() and check_server() and declared():
    if argv[1] == "KEY_FILEIO":
        exec_main()
    elif argv[1] == "KEY_DISCORD":
        exec_discord()
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
