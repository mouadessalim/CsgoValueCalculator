#setup_uploader.py

from cx_Freeze import setup, Executable

packages = ['queue']

setup(
    options = {'build_exe': {'packages':packages, 'include_msvcr': True}},
	executables = [Executable("uploader_DS.py")]
)