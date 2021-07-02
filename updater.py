import requests
from tkinter import *
from tkinter import messagebox
import webbrowser
import json 
import base64

def updatefunc():
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
        response = requests.get("https://github.com/mouadessalim/CsgoValueCalculator/releases/latest")
        if base64.b64decode(data["version_"].encode('ascii')).decode('ascii') == response.url[65:]:
            return 
        else:
            window = Tk()
            window.withdraw()

            if messagebox.askyesno('Update', f' A new update is available, Download version {response.url[65:]} ?') == True:
                webbrowser.open("https://github.com/mouadessalim/CsgoValueCalculator/releases/latest")
            else:
                return
            window.deiconify()
            window.destroy()
            window.quit()
    except:
        return
