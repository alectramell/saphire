#!/usr/bin/python

import os
import getpass

username = getpass.getuser()
username = str(username)

deskitem = str("""
[Desktop Entry]
Name=Saphire Mail
Comment=ssmtp utility for gmail
Categories=GNOME;Utility;
Exec=python /home/""" + username + """/saphire/saphiremail/__main__.py &
Icon=/home/""" + username + """/saphire/saphiremail/saphiremail64x64.png
Terminal=true
Type=Application
""")

activate = str('echo "' + deskitem + '" > /home/' + username + '/saphire/saphiremail/saphiremail.desktop && chmod 755 /home/' + username + '/saphire/saphiremail/saphiremail.desktop')

os.system(activate)

os.system('clear')

runnit = str('cp /home/' + username + '/saphire/saphiremail/saphiremail.desktop /home/' + username + '/Desktop/saphiremail.desktop')

os.system(runnit)

os.system('clear')




