# Port Poirot

![Python application](https://github.com/jeroenbellen/PortPoirot/workflows/Python%20application/badge.svg)

Port Poirot displays a list of all ports that are in use. It provides filtering capabilities and a way to kill the process
that is using a specific port.

Tested on macos running python 3.8, root access is required to run the program.

Tested on ubuntu running python 3.7, root access is optional. To kill a process of another user you must become root.

## Installation from source
```bash
git clone git@github.com:jeroenbellen/PortPoirot.git
pip3 install PySide2
pip3 install psutil
pip3 install elevate
sudo python3 PortPoirot/port_poirot.py
```

## Creating a mac app
Currently pyinstaller doesn't work with python 3.8, fallback to python 3.7.
Note that we cannot use the --onefile option, the elevate module doesn't like it.
```bash
pip install pyinstaller
python -m PyInstaller --icon detective.icns --noconfirm --clean --windowed port_poirot.py
```
Make sure to set the 'NSHighResolutionCapable' property too 'True' within the info.plist file.
```
<dict>
    ....
	<key>NSHighResolutionCapable</key>
	<string>True</string>
</dict>
</plist>
```
