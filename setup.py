import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.

includefiles = ['gui.ui']
packages = ['queue']

setup(
	name = "CSGO VALUE CALCULATOR",
	version = "1.2"
	options = {'build_exe': {'include_files':includefiles, 'packages':packages}},
	executables = [Executable("main.py", base=base)]
)
