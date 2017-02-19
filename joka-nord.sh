#!/bin/bash

dialog --backtitle "NordVPN Feature Selection" \
  --radiolist "Select VPN Type:" 12 40 4 \
        1 Dedicated IP \
        2 TOR Optimised \
        3 P2P Optimised \
        4 Random Location

dialog --menu "Choose a location:" 11 30 4 1 USA 2 Russia 3 Australia 4 Canada

dialog --infobox "Connecting to RU-004 via OpenVPN" 4 30 ; sleep 2

clear
toilet -F gay -f smblock Connected!
