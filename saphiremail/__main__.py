#!/usr/bin/python

import os
import getpass

os.system('clear')

mailfrom = raw_input('FROM (username@gmail.com): ')
mailfrom = str(mailfrom)

os.system('clear')

mailto = raw_input('TO (recipient@email.com): ')
mailto = str(mailto)

os.system('clear')

mailmsg = raw_input('MESSAGE (mail text): ')
mailmsg = str(mailmsg)

os.system('clear')

blankmail = str('''
To: ''' + mailto + '''
From: ''' + mailfrom + '''

''' + mailmsg + '''

''')

command = str('echo "' + blankmail + '" > ~/Desktop/msg.txt')

newmail = str('''sendmail ''' + mailfrom + ''' < ~/Desktop/msg.txt''')

os.system(command)

os.system('clear')

print ('Sending Email..')

os.system(newmail)

print ('..Email Sent!')

os.system('sleep 3 && clear')

os.system('rm -r ~/Desktop/msg.txt && clear')






