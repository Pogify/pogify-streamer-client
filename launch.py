import os
import requests
import zipfile
from pathlib import Path


chromedir = Path.home() / ".pogify" / "GoogleChromePortable"


def unzip(filepath: str, resultpath: str) -> None:
    with zipfile.ZipFile(filepath, "r") as zip_ref:
        zip_ref.extractall(resultpath)

try:
    os.mkdir(Path.home() / ".pogify")
    zippath = Path.home() / ".pogify" / "chrome.zip"

    with open(zippath, 'wb+') as fout:
        fout.write(
            requests.get(
                "https://github.com/Pogify/pogify-client"
                "/releases/latest/download/GoogleChromePortable.zip"
            ).content)

    unzip(str(zippath), Path.home() / ".pogify")
    os.remove(str(zippath))

except FileExistsError:
    pass


os.system(
    f"start {chromedir / 'GoogleChromePortable.exe'} --app=http://pogify.net/"
)
