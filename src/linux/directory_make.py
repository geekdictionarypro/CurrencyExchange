import splash_screen
# import getpass 
import os 
import sys 

sys.setrecursionlimit(10**6)  

def geek_dictionarySoftwareFolder():
    # username = getpass.getuser() 
    if not os.path.exists('/usr/local/bin/GeekDictionary Software/'):
        path = '/usr/local/bin/GeekDictionary Software/'
        os.makedirs(path)
        applications_folder() 
    else: 
        splash_screen.slinuxscreen() 

def applications_folder(): 
    # username = getpass.getuser()
    if not os.path.exists('/usr/local/bin/GeekDictionary Software/Applications/'):
        path = '/usr/local/bin/GeekDictionary Software/'
        path += '/Applications'
        os.makedirs(path)
        currency_exchangeFolder() 
    else: 
        splash_screen.linuxscreen() 

def currency_exchangeFolder(): 
    # username = getpass.getuser()
    if not os.path.exists('/usr/local/bin/GeekDictionary Software/Applications/Currency Exchange/'):
        path = '/usr/local/bin/GeekDictionary Software/Applications'
        path += '/Currency Exchange/'
        os.makedirs(path)
        splash_screen.grabImage() 
    else: 
        splash_screen.linuxscreen()  