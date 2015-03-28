#!/usr/bin/python

import os
import getpass

username = getpass.getuser()
username = str(username)

makeava = str('chmod 755 /home/' + username + '/saphire/facebook/*.sh')

os.system(makeava)

deskitem = str("""
[Desktop Entry]
Name=Facebook
Comment=Facebook for Saphire
Categories=GNOME;Utility;
Exec=sensible-browser --new-window="https://facebook.com/apollondma"
Icon=/home/""" + username + """/saphire/facebook/fb64x64.png
Terminal=false
Type=Application
""")

activate = str('echo "' + deskitem + '" > /home/' + username + '/saphire/facebook/facebook.desktop && chmod 755 /home/' + username + '/saphire/facebook/facebook.desktop')

os.system(activate)

os.system('clear')

runnit = str('cp /home/' + username + '/saphire/facebook/facebook.desktop /home/' + username + '/Desktop/facebook.desktop')

os.system(runnit)

os.system('clear')





