# After we restart the program as root, we end up with a useless process on mac
# Which adds another icon in the dock
import psutil
import os

def check_and_kill():
	if psutil.MACOS and os.getuid() == 0:
		name = 'osascript'
		search = '/Contents/MacOS/Port Poirot\\\'" with administrator privileges without altering line endings'
		
		for proc in psutil.process_iter():
			if proc.name() == name and search in str(proc.cmdline()):
				proc.kill() 