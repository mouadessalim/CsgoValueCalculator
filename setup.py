import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.

includefiles = ["gui.ui", "config.json"]
packages = ['queue', 'webbrowser', 'tkinter', 'updater', 'base64']

setup(
	name = "CSGO VALUE CALCULATOR",
	version = "1.3.1",
	author = "Mouad Essalim",
	author_email="essalim99@gmail.com",
	options = {'build_exe': {'include_files':includefiles, 'packages':packages}},
	executables = [Executable("main.py", base=base)]
)
