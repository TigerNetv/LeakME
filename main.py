#Modules
import os
import datetime
from colored import fg, attr

from src.config import *
from src.mysqlconnector import *
from src.credits import *

whitecolor = fg('#FFFFFF')
redcolor = fg('#8B0000')
greencolor = fg('#009900')
timecolor = fg('#9400D3')
res = attr('reset')

now = datetime.datetime.now()


print("")
print(greencolor + "  _                _    __  __ ______ ")
print(greencolor + " | |              | |  |  \/  |  ____|")
print(greencolor + " | |     ___  __ _| | _| \  / | |__   ")
print(greencolor + " | |    / _ \/ _` | |/ / |\/| |  __|  ")
print(greencolor + " | |___|  __/ (_| |   <| |  | | |____ ")
print(greencolor + " |______\___|\__,_|_|\_\_|  |_|______|")
print("")

commandloop = 1;
while commandloop == 1:
    print("")
    print ((timecolor + now.strftime("%d/%m/%Y %H:%M:%S") + res) + (whitecolor + " Select a module" + res))
    print("")
    print ((greencolor + "        [1] " + res + whitecolor + "Search by Username" + res))
    print ((greencolor + "        [2] " + res + whitecolor + "Search by Email" + res))
    print ((greencolor + "        [3] " + res + whitecolor + "Search by Password" + res))    
    print ((greencolor + "        [4] " + res + whitecolor + "Credits" + res))  
    print ((greencolor + "        [5] " + res + whitecolor + "Exit" + res))  
    
    commandinput = input(whitecolor + " > " + res) 
    if commandinput == '1':
        mysqlsearch_username()
    if commandinput == '2':
        mysqlsearch_email()
    if commandinput == '3':
        mysqlsearch_password()
    if commandinput == '4':
        credits()
    if commandinput == '5':
        exit()
    