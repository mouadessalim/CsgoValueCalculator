import sys
from cx_Freeze import setup, Executable
import base64
import json

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.

includefiles = ["gui.ui", "config.json"]
packages = ['queue', 'tkinter', 'base64']

with open('config.json', 'r') as f:
    data = json.load(f)

setup(
	name = base64.b64decode(data["name_"].encode('ascii')).decode('ascii'),
	version = base64.b64decode(data["version_"].encode('ascii')).decode('ascii'),
	author = base64.b64decode(data["author_"].encode('ascii')).decode('ascii'),
	author_email=base64.b64decode(data["author_email_"].encode('ascii')).decode('ascii'),
	options = {'build_exe': {'include_files':includefiles, 'packages':packages}},
	executables = [Executable("main.py", base=base)]
)
