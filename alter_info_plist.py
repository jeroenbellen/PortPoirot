import plistlib

print('altering info.plist')
path = './dist/Port Poirot.app/Contents/Info.plist'
info = plistlib.readPlist(path)
info['NSHighResolutionCapable'] = 'True'

plistlib.writePlist(info, path)