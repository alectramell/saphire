#!/usr/bin/python

import os
import getpass

username = getpass.getuser()
username = str(username)

deskitem = str("""
[Desktop Entry]
Name=Gmail
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

os.system('touch ~/Desktop/GMAIL-README')

os.system('echo "# Google Mail | Send Utility for Saphire" > ~/Desktop/GMAIL-README')

os.system('echo " " >> ~/Desktop/GMAIL-README')

os.system('echo "This utilty works along side ssmtp, make sure you have viewed ~/saphire/saphiremail/ssmtp-hot-to.png before use!" >> ~/Desktop/GMAIL-README')

os.system('clear')





