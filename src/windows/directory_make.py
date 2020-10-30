import splash_screen
import getpass 
import os 
import sys 

sys.setrecursionlimit(10**6)  

def geek_dictionarySoftwareFolder():
    username = getpass.getuser() 
    if not os.path.exists('C:/Users/' + username + '/GeekDictionary Software/'):
        path = 'C:/Users/' + username + '/GeekDictionary Software/'
        os.makedirs(path)
        applications_folder() 
    else: 
        splash_screen.splashscreen() 

def applications_folder(): 
    username = getpass.getuser()
    if not os.path.exists('C:/Users/' + username + '/GeekDictionary Software/Application/'):
        path = 'C:/Users/' + username + '/GeekDictionary Software'
        path += '/Applications'
        os.makedirs(path)
        currency_exchangeFolder() 
    else: 
        splash_screen.splashscreen() 

def currency_exchangeFolder(): 
    username = getpass.getuser()
    if not os.path.exists('C:/Users/' + username + '/GeekDictionary Software/Application/Currency Exchange/'):
        path = 'C:/Users/' + username + '/GeekDictionary Software/Applications/'
        path += '/Currency Exchange/'
        os.makedirs(path)
        splash_screen.grabImage() 
    else: 
        splash_screen.splashscreen()  