#!/usr/bin/python

import os
import getpass

username = getpass.getuser()
username = str(username)

makeava = str('chmod 755 /home/' + username + '/saphire/firefox/*.sh')

os.system(makeava)

deskitem = str("""
[Desktop Entry]
Name=Firefox
Comment=Firefox for Saphire
Categories=GNOME;Utility;
Exec=firefox --new-window="http://pegasus.zohosites.com"
Icon=/home/""" + username + """/saphire/firefox/firefox.svg
Terminal=false
Type=Application
""")

activate = str('echo "' + deskitem + '" > /home/' + username + '/saphire/firefox/firefox.desktop && chmod 755 /home/' + username + '/saphire/firefox/firefox.desktop')

os.system(activate)

os.system('clear')

runnit = str('cp /home/' + username + '/saphire/firefox/firefox.desktop /home/' + username + '/Desktop/firefox.desktop')

os.system(runnit)

os.system('clear')





