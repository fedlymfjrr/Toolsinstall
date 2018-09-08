#!usr/bin/python
import os
import sys
import random 
from time import sleep as timeout
from module.lol import *


banners()

print ("\033[96m1.)install cupp\n2.)install Auxile\n3.)install nuyul kubik\n4.)install nuyul cashtree\n5.)install Bot Instagram\n6.)install Multi-BruteForce-Facebook\n7.)install OSIF\n8.)install reportFB\n9.)EXIT")
pilihan = raw_input("\033[91m<<Chosee What You Want>> =")
if pilihan == "1":
    cupp()

elif pilihan == "2":
    Auxile()

elif pilihan == "3":
    kubik()

elif pilihan == "4":
    cashtree()

elif pilihan == "5":
    instagram()

elif pilihan == "6":
    mbf()

elif pilihan == "7":
    OSIF()

elif pilihan == "8":
    reportfb()

elif pilihan == "9":
    print"\033[94m               THANKS FOR USING MY TOOLS :)\n             HAVE A NICE DAY AND KEEP STRONG "
    sys.exit()

else:
    print "\033[91m       WRONG INPUT (RETURN)"
    timeout (3)
    os.execl(sys.executable,sys.executable,*sys.argv)

