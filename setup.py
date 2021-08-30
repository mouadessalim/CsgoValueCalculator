from cx_Freeze import setup, Executable

packages = ['queue']

setup(
	options = {'build_exe': {'packages':packages}},
	executables = [Executable("csgovaluecalculator.py")]
)