from cx_Freeze import setup, Executable
from csgovaluecalculator import version_chromedriver

packages = ['queue']
includefiles = [f'chromedriver_{version_chromedriver}.exe']

setup(
	options = {'build_exe': {'packages':packages, 'include_files':includefiles}},
	executables = [Executable("csgovaluecalculator.py")]
)
