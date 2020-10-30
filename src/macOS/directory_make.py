import splash_screen
import getpass 
import os 
import sys 

sys.setrecursionlimit(10**6)  

def geek_dictionarySoftwareFolder():
    username = getpass.getuser() 
    if not os.path.exists('/Users/' + username + '/Library/Preferences/GeekDictionary Software/'):
        path = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/'
        os.makedirs(path)
        applications_folder() 
    else: 
        splash_screen.splashscreen() 

def applications_folder(): 
    username = getpass.getuser()
    if not os.path.exists('/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/'):
        path = '/Users/' + username + '/Library/Preferences/GeekDictionary Software'
        path += '/Applications'
        os.makedirs(path)
        currency_exchangeFolder() 
    else: 
        splash_screen.splashscreen() 

def currency_exchangeFolder(): 
    username = getpass.getuser()
    if not os.path.exists('/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/Currency Exchange'):
        path = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications'
        path += '/Currency Exchange/'
        os.makedirs(path)
        splash_screen.grabImage() 
    else: 
        splash_screen.splashscreen()  