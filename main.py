import requests
from bs4 import BeautifulSoup
import time
from PyQt5 import QtWidgets, uic


def calc():
	SteamID= call.lineEdit.text()
	call.progressBar.setValue(15)
	if(SteamID.isdigit()):
		call.progressBar.setValue(30)
		if int(SteamID) > 9999999999999999:
			call.progressBar.setValue(40)
			response = requests.get("https://csgopedia.com/inventory-value/?profiles=" + SteamID)
			call.progressBar.setValue(70)
			time.sleep(2)
			if response.ok:
				page = BeautifulSoup(response.text, features="html.parser")
				rank = page.find("table", class_="table-cell")
				value = rank.find_all("strong")[1].get_text()
				value_float = float(value[1:])
				call.progressBar.setValue(80)
				responseip = requests.get("https://api.techniknews.net/ipgeo/").json()
				if responseip['currency'] == "USD":
					call.progressBar.setValue(100)
					calc.final_response = str(value_float) + " USD"
				else:
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
					calc.final_response = str(conversion_finished) + " " + responseip['currency']			
			else:
				call.progressBar.setValue(100)
				calc.final_response = "Impossible de trouver votre profil ou les serveur sont indisponible"
		else:
			call.progressBar.setValue(100)
			calc.final_response = "Steam ID64 (DEC) incorrecte"
	else:
		call.progressBar.setValue(100)
		calc.final_response = "Steam ID64 (DEC) incorrecte"
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
