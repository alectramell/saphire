#!/usr/bin/python

import os
import getpass

username = getpass.getuser()
username = str(username)

deskitem = str("""
[Desktop Entry]
Name=Pegasus
Comment=Pegasus ADM Code Network
Categories=GNOME;Utility;
Exec=sensible-browser --new-window="http://pegasus.zohosites.com"
Icon=/home/""" + username + """/saphire/pegasus/pegasus64x64.png
Terminal=false
Type=Application
""")

activate = str('echo "' + deskitem + '" > /home/' + username + '/saphire/pegasus/pegasus.desktop && chmod 755 /home/' + username + '/saphire/pegasus/pegasus.desktop')

os.system(activate)

os.system('clear')

runnit = str('cp /home/' + username + '/saphire/pegasus/pegasus.desktop /home/' + username + '/Desktop/pegasus.desktop')

os.system(runnit)

os.system('clear')





