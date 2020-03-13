# Port Poirot

![Python application](https://github.com/jeroenbellen/PortPoirot/workflows/Python%20application/badge.svg)

Port Poirot displays a list of all ports that are in use. It provides filtering capabilities and a way to kill the process
that is using a specific port.

Tested on macos running python 3.8, root access is required to run the program.

## Installation from source
```bash
git clone git@github.com:jeroenbellen/PortPoirot.git
pip3 install PySide2
pip3 install psutil
sudo python3 PortPoirot/app.py
```

## Creating a mac app
Currently pyinstaller doesn't work with python 3.8, fallback to python 3.7.
Note that we cannot use the --onefile option, the elevate module doesn't like it.
```bash
pip install pyinstaller
python -m PyInstaller --icon detective.icns --noconfirm --clean --windowed app.py
```
