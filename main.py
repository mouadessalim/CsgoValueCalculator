import requests
from bs4 import BeautifulSoup
import time
from PyQt5 import QtWidgets, uic
import updater
import threading 

def window():
	app = QtWidgets.QApplication([])
	window.call = uic.loadUi("gui.ui")

	window.call.progressBar.setMinimum(0)
	window.call.progressBar.setMaximum(100)
	window.call.progressBar.setValue(0)

	window.call.pushButton.clicked.connect(calc)

	window.call.show()
	app.exec()

def calc():
	window.call.pushButton.setText("Verification ✔")
	SteamID = window.call.lineEdit.text()
	window.call.progressBar.setValue(15)
	time.sleep(1)
	if(SteamID.isdigit()):
		window.call.pushButton.setText("Searching... 🛠")
		window.call.progressBar.setValue(30)
		time.sleep(1)
		if int(SteamID) > 9999999999999999:
			window.call.label_2.setText("Don't worry if the app is crashing, just wait 😋")
			window.call.progressBar.setValue(40)
			response = requests.get("https://csgopedia.com/inventory-value/?profiles=" + SteamID)
			window.call.progressBar.setValue(65)
			time.sleep(1)
			if response.ok:
				page = BeautifulSoup(response.text, features="html.parser")
				rank = page.find("table", class_="table-cell")
				value = rank.find_all("strong")[1].get_text()
				value_float = float(value[1:])
				window.call.progressBar.setValue(80)
				time.sleep(1)
				responseip = requests.get("https://api.techniknews.net/ipgeo/").json()
				if responseip['currency'] == "USD":
					window.call.progressBar.setValue(100)
					window.call.pushButton.setText("Success! ✅")
					calc.final_response = str(value_float) + " USD 💰"
				else:
					window.call.pushButton.setText("Converting... 🧐")
					response = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/{responseip['currency'].lower()}.json").json()
					window.call.progressBar.setValue(90)
					conversion = response[responseip['currency'].lower()] * value_float
					conversion_finished = round(conversion, 2)
					window.call.progressBar.setValue(100)
					window.call.pushButton.setText("Success! ✅")
					calc.final_response = str(conversion_finished) + " " + responseip['currency'] + " 💰"		 		
			else:
				window.call.progressBar.setValue(100)
				window.call.pushButton.setText("Error ❌")
				calc.final_response = "Could not find your profile or the server is down retry later if it's not working 🤔"
		else:
			window.call.pushButton.setText("Error ❌")
			window.call.progressBar.setValue(100)
			calc.final_response = "Steam ID64 (DEC) incorrect ❗"
	else:
		window.call.pushButton.setText("Error ❌")
		window.call.progressBar.setValue(100)
		calc.final_response = "Steam ID64 (DEC) incorrect ❗"
	reponse()

def reponse():
	window.call.label_2.setText(calc.final_response)

cpu1 = threading.Thread(target=window).start()
cpu2 = threading.Thread(target=updater.updatefunc).start()
