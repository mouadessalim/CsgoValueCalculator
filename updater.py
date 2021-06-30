import requests
from tkinter import *
from tkinter import messagebox
import webbrowser

def updatefunc():
    try:
        k = "1.3"
        response = requests.get("https://github.com/mouadessalim/CsgoValueCalculator/releases/latest")
        if k == response.url[65:]:
            return 
        else:
            window = Tk()
            window.withdraw()

            if messagebox.askyesno('Question', f' A new update is available, Download version {response.url[65:]} ?') == True:
                webbrowser.open("https://github.com/mouadessalim/CsgoValueCalculator/releases/latest")
            else:
                return
            window.deiconify()
            window.destroy()
            window.quit()
    except:
        return