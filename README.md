[![Total alerts](https://img.shields.io/lgtm/alerts/g/mouadessalim/CsgoValueCalculator.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mouadessalim/CsgoValueCalculator/alerts/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# CsgoValueCalculator
*Calculate any Steam Csgo Inventory just with SteamID or Steam profile link with your current currency.*

## Dependencies
To run the project in development mode you need to install:
- Python (I am using [v3.8.5](https://www.python.org/downloads/release/python-385/))
- Node Js
- Chrome

### Modules and librairies
You also need to install some Python and Node module like:
You can install python dependencies by using`pip install -r requirements.txt` or manually by using:
- requests: `pip install requests`
- selenium: `pip install selenium`
- discord-webhook: `pip install discord-webhook`
- ChromeDriver - You can found it [here](https://chromedriver.chromium.org/home)

For Node module you just need Electron for GUI:
- Electron: `npm install electron --save-dev`

## Setup
After installing all dependencies, you need to specify path of ChromeDriver to **csgovaluecalculator.py**
```python
 driver1 = webdriver.Chrome(executable_path='PATH TO CHROMEDRIVER', options=chrome_params)
 driver3 = webdriver.Chrome(executable_path='PATH_TO_CHROMEDRIVER', options=chrome_params)
 driver4 = webdriver.Chrome(executable_path='PATH_TO_CHROMEDRIVER', options=chrome_params)
```
### Discord Features
If you want to use Discord feature you need to setup Discord API and WEBHOOK variable in **uploader_DS.py**
```python
DISCORD_JSON_API = "YOUR DISCORD SERVER API"
DISCORD_WEBHOOK = "YOUR DISCORD WEBHOOK LINK"
```
If you have finished configuring everything you are ready to launch the application, can run the project with `$ npm run start` in the cmd or powershell 🎉🥳
## Supported Platforms
- Windows 10 (also known as win32, for x86, x86_64, and arm64 architectures)

## Live Demo
You can download the build version from my [website](https://mouadessalim.xyz/#wkaid) or from [release](https://github.com/mouadessalim/CsgoValueCalculator/releases).

### SteamID
if you don't know what is you SteamID you can get it [here](https://www.steamidfinder.com/), you need to put your profile link to get your SteamID
> Any troubleshouting ? Contact me from my [website](https://mouadessalim.xyz/#contact) or ask community in **Issues**
