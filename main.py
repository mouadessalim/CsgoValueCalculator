import requests
from bs4 import BeautifulSoup
import time
from PyQt5 import QtWidgets, uic


def calc():
	call.pushButton.setText("Verification ✔")
	SteamID= call.lineEdit.text()
	call.progressBar.setValue(15)
	time.sleep(1)
	if(SteamID.isdigit()):
		call.pushButton.setText("Searching... 🛠")
		call.progressBar.setValue(30)
		time.sleep(1)
		if int(SteamID) > 9999999999999999:
			call.label_2.setText("Don't worry if the app is crashing, just wait 😋")
			call.progressBar.setValue(40)
			response = requests.get("https://csgopedia.com/inventory-value/?profiles=" + SteamID)
			call.progressBar.setValue(65)
			time.sleep(1)
			if response.ok:
				page = BeautifulSoup(response.text, features="html.parser")
				rank = page.find("table", class_="table-cell")
				value = rank.find_all("strong")[1].get_text()
				value_float = float(value[1:])
				call.progressBar.setValue(80)
				time.sleep(1)
				responseip = requests.get("https://api.techniknews.net/ipgeo/").json()
				if responseip['currency'] == "USD":
					call.progressBar.setValue(100)
					call.pushButton.setText("Success! ✅")
					calc.final_response = str(value_float) + " USD 💰"
				else:
					call.pushButton.setText("Converting... 🧐")
					url = "https://exchangerate-api.p.rapidapi.com/rapid/latest/USD"

					headers = {
    					'x-rapidapi-key': "c787e69104msha02a28785e07404p156082jsn3bc083a5ebca",
    					'x-rapidapi-host': "exchangerate-api.p.rapidapi.com"
    					}
					response = requests.request("GET", url, headers=headers).json()
					call.progressBar.setValue(90)
					conversion = response['rates'][responseip['currency']] * value_float
					conversion_finished = round(conversion, 2)
					call.progressBar.setValue(100)
					call.pushButton.setText("Success! ✅")
					calc.final_response = str(conversion_finished) + " " + responseip['currency'] + " 💰"		 		
			else:
				call.progressBar.setValue(100)
				call.pushButton.setText("Error ❌")
				calc.final_response = "Could not find your profile or the server is down retry later if it's not working 🤔"
		else:
			call.pushButton.setText("Error ❌")
			call.progressBar.setValue(100)
			calc.final_response = "Steam ID64 (DEC) incorrect ❗"
	else:
		call.pushButton.setText("Error ❌")
		call.progressBar.setValue(100)
		calc.final_response = "Steam ID64 (DEC) incorrect ❗"
	reponse()

def reponse():
	call.label_2.setText(calc.final_response)

app = QtWidgets.QApplication([])
call = uic.loadUi("gui.ui")

n = 100

call.progressBar.setMinimum(0)
call.progressBar.setMaximum(n)
call.progressBar.setValue(0)

call.pushButton.clicked.connect(calc)

call.show()
app.exec()
