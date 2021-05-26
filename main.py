import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, uic
import json 
import time


def calc():
	SteamID= call.lineEdit.text()
	call.progressBar.setValue(15)
	call.pushButton.setText("Verification...")
	if(SteamID.isdigit()):
		call.progressBar.setValue(30)
		time.sleep(2)
		if int(SteamID) > 9999999999999999:
			call.pushButton.setText("Calculating...")
			call.progressBar.setValue(40)
			params = (
    			('api_key', 'd7da4500-f32d-4c9d-a3b6-145ce70397d3'),
    			('url', 'http://csgobackpack.net/api/GetInventoryValue/?id={}'.format(SteamID)),
			)
			response = requests.get('https://api.webscraping.ai/html', params=params)
			response_html = BeautifulSoup(response.text, features="html.parser")
			response_html_brute = response_html.find('body').get_text()
			response_json = json.loads(response_html_brute)
			#response = requests.get("https://csgopedia.com/inventory-value/?profiles=" + SteamID)
			call.progressBar.setValue(70)
			time.sleep(2)
			if response.ok and response_json['success'] == 'true':
				call.progressBar.setValue(80)
				responseip = requests.get("https://api.techniknews.net/ipgeo/").json()
				if responseip['currency'] == "USD":
					call.progressBar.setValue(100)
					calc.final_response = str(response_json['value']) + " USD"
				else:
					url = "https://exchangerate-api.p.rapidapi.com/rapid/latest/USD"

					headers = {
    					'x-rapidapi-key': "c787e69104msha02a28785e07404p156082jsn3bc083a5ebca",
    					'x-rapidapi-host': "exchangerate-api.p.rapidapi.com"
    					}
					response = requests.request("GET", url, headers=headers).json()
					call.progressBar.setValue(90)
					conversion = response['rates'][responseip['currency']] * float(response_json['value'])
					conversion_finished = round(conversion, 2)
					call.progressBar.setValue(100)
					calc.final_response = str(conversion_finished) + " " + responseip['currency']			
			else:
				call.progressBar.setValue(100)
				calc.final_response = "Impossible de trouver votre profil"
		else:
			call.progressBar.setValue(100)
			calc.final_response = "Steam ID64 (DEC) incorrecte"
	else:
		call.progressBar.setValue(100)
		calc.final_response = "Steam ID64 (DEC) incorrecte"
	call.pushButton.setText("Success !")
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
