import requests
import json
from sys import argv
import sys
import os
import socket 
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

version_chromedriver = "94"

def writter(s, v):
    if os.path.exists(f"{os.getenv('APPDATA')}\csgo-value-calculator\csgoaccount.json"):
        with open(f"{os.getenv('APPDATA')}\csgo-value-calculator\csgoaccount.json", 'r') as f:
            data = json.load(f)
            data[s] = {}
            data[s]['value'] = str(v)
            data[s]['custom_URL'] = str(get_info.custom_URL)
            data[s]['profile_state'] = str(get_info.profile_state)
            data[s]['profile_created'] = str(get_info.profile_created)
            data[s]['name'] = str(get_info.name_)
            data[s]['location'] = str(get_info.location_)
            data[s]['profile_url'] = str(get_info.profile_url)
            with open(f"{os.getenv('APPDATA')}\csgo-value-calculator\csgoaccount.json", 'w') as n:
                n.write(str(json.dumps(data, indent=2)))
    else:
        with open(f"{os.getenv('APPDATA')}\csgo-value-calculator\csgoaccount.json", 'w') as k:
            k.write("{}")
        with open(f"{os.getenv('APPDATA')}\csgo-value-calculator\csgoaccount.json", 'r') as f:
            data = json.load(f)
            data[s] = {}
            data[s]['value'] = str(v)
            data[s]['custom_URL'] = str(get_info.custom_URL)
            data[s]['profile_state'] = str(get_info.profile_state)
            data[s]['profile_created'] = str(get_info.profile_created)
            data[s]['name'] = str(get_info.name_)
            data[s]['location'] = str(get_info.location_)
            data[s]['profile_url'] = str(get_info.profile_url)
            with open(f"{os.getenv('APPDATA')}\csgo-value-calculator\csgoaccount.json", 'w') as n:
                n.write(str(json.dumps(data, indent=2)))

def get_info():
    global get_info_status
    try:
        chrome_params = Options()
        chrome_params.add_argument("--log-level=3")
        chrome_params.headless = True
        driver2 = webdriver.Chrome(executable_path='chromedriver_94.exe', options=chrome_params)
        driver2.get(f"https://steamid.io/lookup/{SteamID}")
        try:
            get_info.custom_URL = driver2.find_element(By.XPATH, "//*[@id='content']/dl/dd[4]/a").text
        except:
            get_info.custom_URL = driver2.find_element(By.XPATH, "//*[@id='content']/dl/dd[4]").text
        get_info.profile_state = driver2.find_element(By.XPATH, "//*[@id='content']/dl/dd[5]/span").text
        get_info.profile_created = driver2.find_element(By.XPATH, "//*[@id='content']/dl/dd[6]").text
        get_info.name_ = driver2.find_element(By.XPATH, "//*[@id='content']/dl/dd[7]").text
        try:
            get_info.location_ = driver2.find_element(By.XPATH, "//*[@id='content']/dl/dd[8]/a").text
        except:
            get_info.location_ = driver2.find_element(By.XPATH, "//*[@id='content']/dl/dd[8]").text
        get_info.profile_url = driver2.find_element(By.XPATH, "//*[@id='go2steamcom']").text
        get_info_status = True
    except:
        get_info_status = False
    finally:
        try:
            driver2.quit()
        except:
            pass

def main_():
    global main_status
    valid_response = requests.get(f"https://www.steamidfinder.com/lookup/{SteamID}")
    if valid_response.ok:
        try:
            chrome_params = Options()
            chrome_params.add_argument("--window-size=0,0")
            chrome_params.add_argument("--log-level=3")
            driver1 = webdriver.Chrome(executable_path='chromedriver_94.exe', options=chrome_params)
            driver1.set_window_position(-10000,0)
            driver1.get(f"https://csgobackpack.net//?nick={SteamID}")
            element = WebDriverWait(driver1, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body//div[@id='info']//p"))
            )
            global data_float
            data_float = float(element.text[:-1])
            responseip = requests.get("https://api.techniknews.net/ipgeo/").json()
            if responseip['currency'] == "EUR":
                #writter(SteamID, str(data_float))
                print(str(data_float) + " EUR")
                main_status = True
            else:
                response = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/{responseip['currency'].lower()}.json").json()
                conversion = response[responseip['currency'].lower()] * data_float
                conversion_finished = round(conversion, 2)
                #writter(SteamID, str(data_float))
                print(str(conversion_finished) + " " + responseip['currency'])
                main_status = True
        except:
            print("This inventory is private or user doesn't have any items in inventory")
        finally:
            driver1.quit()
    else:
        print("This SteamID doesn't exist.")

def test_connexion():
    try:
        socket.create_connection(('google.com', 80))
        return True
    except:
        return False

def check_server():
    try:
        socket.create_connection(('csgobackpack.net', 80))
        socket.create_connection(('cdn.jsdelivr.net', 80))
        socket.create_connection(('steamidfinder.com', 80))
        if requests.get("https://api.techniknews.net/ipgeo/").ok:
            return True
        else:
            return False
    except:
        return False

def get_version():
    try:
        chrome_params = Options()
        chrome_params.headless = True
        driver3 = webdriver.Chrome(executable_path='chromedriver_94.exe', options=chrome_params)
        if 'browserVersion' in driver3.capabilities:
            v = driver3.capabilities['browserVersion']
            if v[:2] == version_chromedriver:
                return True
            else:
                return False
        else:
            old_v = driver3.capabilities['version']
            if old_v[:2] == version_chromedriver:
                return True
            else:
                return False
    except:
        return False
    finally:
        try:
           driver3.quit() 
        except:
            pass

def start_threads():
    th1 = threading.Thread(target=main_())
    th2 = threading.Thread(target=get_info())
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    if 'main_status' and 'get_info_status' in globals():
        if main_status and get_info_status:
            writter(SteamID, data_float)

def verification():
    if test_connexion() and get_version() and check_server():
        if argv[1].isdigit() and int(argv[1]) > 9999999999999999:
            global SteamID
            SteamID = argv[1]
            start_threads()
        else:
            if not argv[1].isdigit():
                chrome_params = Options()
                chrome_params.add_argument("--log-level=3")
                chrome_params.headless = True
                driver4 = webdriver.Chrome(executable_path='chromedriver_94.exe', options=chrome_params)
                driver4.get("https://steamid.io/")
                try:
                    driver4.find_element(By.XPATH, "//input[@id='input']").send_keys(argv[1])
                    driver4.find_element(By.XPATH, "//button[@class='btn btn-danger input-lg']").click()
                    SteamID = driver4.find_element(By.XPATH, "//dd[@class='value short'][3]/a").text
                    start_threads()
                except:
                    print('Steam profile link not found !')
            else:
                print("Format not valid!")
    else:
        if test_connexion() and check_server():
            if os.path.exists('C:\Program Files\Google\Chrome\Application\chrome.exe') or os.path.exists('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'):
                print(f'Chrome detected, but you need to have version {version_chromedriver}')
            else:
                print("Chrome not detected, please install it")
        elif test_connexion():
            print('Server down, please retry later.')
        else:
            print("No connexion found, please check it.")

def declared():
    try:
        x = argv[1]
        if x == "build":
            return False
        else:
            return True
    except:
        return False

if declared():
    verification()
else:
    try:
        sys.exit()
    except:
        try:
            quit()
        except:
            pass
