#!/bin/bash

clear

ANSWER=$(zenity --question --title="Firefox" --text="Saphire will open Firefox in a Private Window, continue?..") && firefox --private-window="http://pegasus.zohosites.com" &

clear


