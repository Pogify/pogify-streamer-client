import os
import shutil
import sys
from pathlib import Path


# From https://stackoverflow.com/questions/26577574/python-pyinstaller-onefile-executable
def resource(relative_path):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath('.'), relative_path)

chrome = resource("GoogleChromePortable") # "GoogleChromePortable.exe"))
newpath = Path.home() / ".pogify" / "GoogleChromePortable"

print("Relocating chrome executable")

try:
    os.mkdir(Path.home() / ".pogify")
except FileExistsError:
    pass

try:
    shutil.copytree(chrome, newpath)
except FileExistsError:
    pass

os.system(
    f"start {newpath / 'GoogleChromePortable.exe'} --app=http://pogify.net/"
)
