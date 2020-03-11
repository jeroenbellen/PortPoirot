# Port Poirot

Port Poirot displays a list of all ports that are in use. It provides filtering capabilities and a way to kill the process
that is using a specific port.

Tested on macos running python 3.8
Root access is required to run the program.

## Installation from source
```bash
git clone git@github.com:jeroenbellen/PortPoirot.git
pip3 install PySide2
pip3 install psutil
sudo python3 PortPoirot/app.py
```
