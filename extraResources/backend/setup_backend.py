from cx_Freeze import setup, Executable

packages = ['queue']
includefiles = ['chromedriver.exe']

setup(
	options = {'build_exe': {'packages':packages, 'include_files':includefiles}},
	executables = [Executable("csgovaluecalculator.py")]
)
