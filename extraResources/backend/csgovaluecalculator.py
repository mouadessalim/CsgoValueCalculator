import requests
from sys import argv
import socket 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main_():
    SteamID = argv[1]
    if SteamID.isdigit() and int(SteamID) > 9999999999999999:
        valid_response = requests.get(f"https://www.steamidfinder.com/lookup/{SteamID}")
        if valid_response.ok:
            try:
                chrome_params = Options()
                #chrome_params.headless = True
                chrome_params.add_argument("--window-size=0,0")
                chrome_params.add_argument("--log-level=3")
                driver1 = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_params)
                driver1.set_window_position(-10000,0)
                driver1.get(f"https://csgobackpack.net//?nick={SteamID}")
                element = WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body//div[@id='info']//p"))
                )
                data_float = float(element.text[:-1])
                responseip = requests.get("https://api.techniknews.net/ipgeo/").json()
                if responseip['currency'] == "EUR":
                    print(str(data_float) + " EUR")
                else:
                    response = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/{responseip['currency'].lower()}.json").json()
                    conversion = response[responseip['currency'].lower()] * data_float
                    conversion_finished = round(conversion, 2)
                    print(str(conversion_finished) + " " + responseip['currency'])
            except:
                print("Server Down, please retry later !")
            finally:
                driver1.quit()
        else:
            print("This SteamID doesn't exist")
    else:
        print("Format not valid !")

def test_connexion():
    try:
        socket.create_connection(('google.com', 80))
        return True
    except:
        return False

def get_version():
    try:
        chrome_params = Options()
        chrome_params.headless = True
        driver3 = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_params)
        if 'browserVersion' in driver3.capabilities:
            v = driver3.capabilities['browserVersion']
            if v[:2] == "93":
                return True
            else:
                return False
        else:
            old_v = driver3.capabilities['version']
            if old_v[:2] == "93":
                return True
            else:
                return False
    except:
        return False
    finally:
        driver3.quit()

if test_connexion() and get_version():
    main_()
else:
    if test_connexion():
        print("Verifie that Chrome 93 is installed !")
    else:
        print("No connexion found, please check it")
