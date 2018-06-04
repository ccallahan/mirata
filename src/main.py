#Mirata v.1 by tbcr
#coded in Python 2.9
#released under GNU GPL,
#a copy of which is in
#the same folder as this

import os
import grabber
import time
import subprocess
from whichcraft import which
import argparse
import sys



from urlgrabber.grabber import URLGrabber
from urlgrabber.progress import text_progress_meter
url = "http://174.109.47.119/files/alephone.snap"

parser = argparse.ArgumentParser()
parser.add_argument("--override-snap-bugout", help="Overrides sanity check for snapcraft.", action="store_true")
args = parser.parse_args()


os.system('clear')
print("MIRATA, the AlephOne Linux setup tool")
print("Version .1 by tbcr")
print("-----------------------------------------")
print("")
time.sleep(3)

print("Before we begin, please select your distro")
print("------------------------------------------")
print("1)Fedora")
print("2)Ubuntu")
print("3)Arch")
print("4)Gentoo")
print("5)openSUSE")
print ("6)Sabayon(Equo)")
print("")
option = input("Selection: ")

def distro_install_cmd(option):
    switcher = {
        1:  import
    }



print('Part 1: Downloading Snap')
g = URLGrabber(reget='simple')
local_file=g.urlgrab(url, filename='alephone.snap')
print("DONE!")

def check_for_snap():
    # Checks if snap is in the system PATH
    if which('snap') is not None:
        installmirata()
    else:
        bugout_nosnap()

def bugout_nosnap():
    #Checks if we are overriding the bugout
    if args.override-snap-bugout is True:
        installmirata()
    else:
        print("I can't seem to find snapcraft on this system. Either add it to your path, or use --override-snap-bugout to bypass this sanity check")
        #Sweet Dreams
        sys.exit()



print('Part 2: Detecting snapd Installation')



print('Part 3: Setting up Snap')
