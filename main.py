import requests
from bs4 import BeautifulSoup
import time
from PyQt5 import QtWidgets, uic
import updater
import threading 
import json
import os
from datetime import datetime
import webbrowser

def window():
	app = QtWidgets.QApplication([])
	window.call = uic.loadUi("gui.ui")

	window.call.progressBar.setMinimum(0)
	window.call.progressBar.setMaximum(100)
	window.call.progressBar.setValue(0)

	window.call.pushButton.clicked.connect(calc)
	window.call.pushButton_2.clicked.connect(uploader)

	window.call.show()
	app.exec()
	

def calc():
	window.call.pushButton.setText("Verification ✔")
	calc.SteamID = window.call.lineEdit.text()
	window.call.progressBar.setValue(15)
	time.sleep(1)
	if(calc.SteamID.isdigit()):
		window.call.pushButton.setText("Searching... 🛠")
		window.call.progressBar.setValue(30)
		time.sleep(1)
		if int(calc.SteamID) > 9999999999999999:
			window.call.label_2.setText("Don't worry if the app is crashing, just wait 😋")
			window.call.progressBar.setValue(40)
			response = requests.get("https://csgopedia.com/inventory-value/?profiles=" + calc.SteamID)
			window.call.progressBar.setValue(65)
			time.sleep(1)
			if response.ok:
				page = BeautifulSoup(response.text, features="html.parser")
				rank = page.find("table", class_="table-cell")
				value = rank.find_all("strong")[1].get_text()
				calc.value_float = float(value[1:])
				window.call.progressBar.setValue(80)
				time.sleep(1)
				responseip = requests.get("https://api.techniknews.net/ipgeo/").json()
				if responseip['currency'] == "USD":
					window.call.progressBar.setValue(100)
					window.call.pushButton.setText("Success! ✅")
					calc.final_response = str(calc.value_float) + " USD 💰"
				else:
					window.call.pushButton.setText("Converting... 🧐")
					response = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/{responseip['currency'].lower()}.json").json()
					window.call.progressBar.setValue(90)
					conversion = response[responseip['currency'].lower()] * calc.value_float
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
	if os.path.exists(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator"):
		if os.path.exists(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json"):
			with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'r') as f:
				data = json.load(f)
				try:
					data[calc.SteamID] = str(calc.value_float)
					with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'w') as n:
						n.write(str(json.dumps(data, indent=2)))
				except:
					return
		else:
			with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'w') as k:
				k.write("{}")
			with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'r') as f:
				data = json.load(f)
				try:
					data[calc.SteamID] = str(calc.value_float)
					with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'w') as n:
						n.write(str(json.dumps(data, indent=2)))
				except:
					return
	else:
		os.mkdir(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator")
		with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'w') as k:
				k.write("{}")
		with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'r') as f:
			data = json.load(f)
			try:
				data[calc.SteamID] = str(calc.value_float)
				with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'w') as n:
					n.write(str(json.dumps(data, indent=2)))
			except:
				return

def uploader():
	with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\csgoaccount.json", 'r') as f:
		data = json.load(f)
		window.call.progressBar.setValue(20)
		time.sleep(1)
		with open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\historical.txt", 'w') as k:
			window.call.progressBar.setValue(30)
			for x, y in data.items():
				response = requests.get("https://api.techniknews.net/ipgeo/").json()
				window.call.progressBar.setValue(40)
				if response['currency'] == "USD":
					k.write(str(x + " = " + y + f" {response['currency']}\n"))
					window.call.progressBar.setValue(60)
				else:
					window.call.progressBar.setValue(60)
					response_c = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/{response['currency'].lower()}.json").json()
					window.call.progressBar.setValue(70)
					k.write(str(x + " = " + f"{round(float(response_c[response['currency'].lower()]) * float(y), 2)} {response['currency']}\n"))
					window.call.progressBar.setValue(75)

	params = (
		('expires', '1w'),
	)
	fileopener = open(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\historical.txt", 'rb')
	namefile = f'all_csgo-{datetime.now().strftime("%d_%m_%Y")}.txt'
	files = {
		'file': (namefile, fileopener),
	}

	response_u = requests.post('https://file.io/', params=params, files=files)
	window.call.progressBar.setValue(90)
	response_upload = response_u.json()
	if response_u.ok:
		if response_upload["success"] == True:
			window.call.label_2.setText("your web browser was opened, you can download the file")
			window.call.progressBar.setValue(100)
			webbrowser.open(response_upload["link"])
		else:
			window.call.progressBar.setValue(100)
			window.call.label_2.setText("this is a server error, please retry later or contact me !")
	else:
		window.call.progressBar.setValue(100)
		window.call.label_2.setText("verifie your connexion or try later !")

	fileopener.close()
	os.remove(os.getenv('LOCALAPPDATA') + "\CsgoValueCalculator\historical.txt")

threading.Thread(target=window).start()
threading.Thread(target=updater.updatefunc).start()
