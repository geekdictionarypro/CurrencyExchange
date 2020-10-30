## - For Windows Only - ## 
# from tkinter import *
# import tkinter as tk
#************************#
## - For Linux Only - ## 
import PySimpleGUI as sg 
# macOS and Windows 
# import getpass 
import os 
import urllib.request  
import ctypes, sys
import time 

def grabImage(): 
    # username = getpass.getuser() 
    url = 'https://lh3.googleusercontent.com/pw/ACtC-3fHOEA9MFJ8hd7XkNKJWGNJ3DW4SFx0DbJtE91dQYSUMiyrjH2z1wh4nfeI7x7EifwcB3I64H-5V6YyaeoLReMpwBJyycFmwdS0xAJHuV-UL9wnSmV6_aeB-9GPebTfTZ4FWVPjnjpsv3KvjUrdxw6j=w300-h500-no?authuser=0'
    '''
    # Windows Path 
    path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications/Currency Exchange/'
    '''
    '''
    # macOS Path 
    path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/Currency Exchange/'
    '''
    # Linux Path 
    path_linux = '/usr/local/bin/GeekDictionary Software/Applications/Currency Exchange/'
    fullfilename = os.path.join(path_linux, 'SplashScreen.gif')
    urllib.request.urlretrieve(url, fullfilename)

def geek_dictionarySoftwareFolder():
    try: 
        # - Windows and macOS - # 
        # username = getpass.getuser() 
        '''
        # Windows Operating System 
        path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications/Currency Exchange/'
        '''
        '''
        # - macOS 
        path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/'
        '''
        # Linux Path 
        path_linux = '/usr/local/bin/GeekDictionary Software/'
        if not os.path.exists(path_linux):
            # path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/'
            # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/' 
            path_linux = '/usr/local/bin/GeekDictionary Software/'
            os.makedirs(path_linux)
            applications_folder() 
        else: 
            # splashscreen()
            linux_splashScreen()  
    except FileExistsError: 
        try: 
           # path_macOS = 'C:/Users/' + username + '/GeekDictionary Software/'
           # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/'
           path_linux = '/usr/local/bin/GeekDictionary Software/'
           os.rmdir(path_linux)
           user_input = input("Type continue > ")
           if user_input in ["continue", "Continue"]: 
               linux_splashScreen()
           else: 
               print("Sorry, Invalid input. Redirecting anyways")
               time.sleep(3)
               applications_folder() 
        except OSError: 
            print("Re-run the program!")
            time.sleep(5)
            sys.exit(1)
    except RecursionError: 
        print("Restart app to continue to main program!")
        time.sleep(10) 
        sys.exit("Restart application to run main program!")

def applications_folder(): 
    try: 
        # username = getpass.getuser()
        # path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/'
        # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications/'
        path_linux = '/usr/local/bin/GeekDictionary Software/Applications/'
        if not os.path.exists(path_linux):
            # path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/'
            # path_windows = 'C:/Users/' + username + '/GeekDictionary Software'
            path_linux = '/usr/local/bin/GeekDictionary Software'
            # path_macOS += '/Applications'
            # path_windows += '/Applications'
            path_linux += '/Applications'
            os.makedirs(path_linux)
            currency_exchangeFolder() 
        else: 
            linux_splashScreen() 
    except FileExistsError: 
        try: 
           # path_macOS = '/Users/' + username + '/GeekDictionary Software/Applications/'
           # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications/'
           path_linux = '/usr/local/bin/GeekDictionary Software/Applications/'
           os.rmdir(path_linux)
           user_input = input("Type continue > ")
           if user_input in ["continue", "Continue"]: 
               linux_splashScreen()
           else: 
               print("Sorry, Invalid input. Redirecting anyways")
               time.sleep(3)
               applications_folder() 
        except OSError: 
            print("Re-run the program!")
            time.sleep(5)
            sys.exit(1)
    except RecursionError: 
        print("Restart app to continue to main program!")
        time.sleep(10) 
        sys.exit("Restart application to run main program!")

def currency_exchangeFolder(): 
    try: 
        # username = getpass.getuser()
        # path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/Currency Exchange/'
        # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications/Currency Exchange/'
        path_linux = '/usr/local/bin/GeekDictionary Software/Applications/Currency Exchange/'
        if not os.path.exists(path_linux):
            # path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications'
            # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications'
            path_linux = '/usr/local/bin/GeekDictionary Software/Applications' 
            # path_macOS += '/Currency Exchange/'
            # path_windows += '/Currency Exchange/'
            path_linux += '/Currency Exchange'
            os.makedirs(path_linux)
            grabImage() 
        else: 
            # splashscreen()  
            linux_splashScreen()
    except FileExistsError: 
        try: 
           # path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/Currency Exchange/'
           # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications/Currency Exchange/'
           path_linux = '/usr/local/bin/GeekDictionary Software/Applications/Currency Exchange' 
           os.rmdir(path_linux)
           user_input = input("Type continue > ")
           if user_input in ["continue", "Continue"]: 
               # splashscreen()
               linux_splashScreen()
           else: 
               print("Sorry, Invalid input. Redirecting anyways")
               time.sleep(3)
               applications_folder() 
        except OSError: 
            print("Re-run the program!")
            time.sleep(5)
            sys.exit(1)
    except RecursionError: 
        print("Restart app to continue to main program!")
        time.sleep(10) 
        sys.exit("Restart application to run main program!")

def createDirectory():
    # username = getpass.getuser() 
    # path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/Currency Exchange/'
    # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications/Currency Exchange/'
    path_linux = '/usr/local/bin/GeekDictionary Software/Applications/Currency Exchange'
    if not os.path.exists(path_linux):
        geek_dictionarySoftwareFolder() 
        applications_folder() 
        currency_exchangeFolder() 
    else: 
        # splashscreen() 
        linux_splashScreen()
'''
def splashscreen(): 
    username = getpass.getuser() 
    path_2 = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/Currency Exchange/SplashScreen.gif'
    # Check for Splashscreen 
    if not os.path.exists(path_2): 
        createDirectory() 
        #creating window
        window = Tk()
        #display attributes
        ## - display attributes - ## 
        # - Get app_width (predefined) - # 
        app_width = 300
        app_height = 500
        # - Get screen_width (defined by every user specified screen) - # 
        screen_width = window.winfo_screenwidth()
        screen_height =  window.winfo_screenheight() 
        # - Function to make it in the middle - # 
        x = (screen_width / 2) - (app_width / 2) 
        y = (screen_height / 2) - (app_height / 2) 
        # - Settings to help remove the top-bar - # 
        window.overrideredirect(True)
        # - Define and place the location of the Window - # 
        window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        canvas = Canvas(window, width = 300, height = 500)
        canvas.pack()
        #GIF in my_image variable
        my_image = tk.PhotoImage(file=path_2)
        canvas.create_image(0, 0, anchor = NW, image=my_image)
        canvas.pack()
        window.after(4500, window.destroy)
        window.mainloop()
    else: 
        #creating window
        window = Tk()
        ## - display attributes - ## 
        # - Get app_width (predefined) - # 
        app_width = 300
        app_height = 500
        # - Get screen_width (defined by every user specified screen) - # 
        screen_width = window.winfo_screenwidth()
        screen_height =  window.winfo_screenheight() 
        # - Function to make it in the middle - # 
        x = (screen_width / 2) - (app_width / 2) 
        y = (screen_height / 2) - (app_height / 2) 
        # - Settings to help remove the top-bar - # 
        window.overrideredirect(True)
        # - Define and place the location of the Window - # 
        window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        canvas = Canvas(window, width = 450, height = 700)
        canvas.pack()
        #GIF in my_image variable
        my_image = tk.PhotoImage(file=path_2)
        canvas.create_image(0, 0, anchor = NW, image=my_image)
        canvas.pack()
        window.after(4500, window.destroy)
        window.mainloop()
'''

def linux_splashScreen(): 
    # username = getpass.getuser() 
    # path_macOS = '/Users/' + username + '/Library/Preferences/GeekDictionary Software/Applications/Currency Exchange/SplashScreen.gif'
    # path_windows = 'C:/Users/' + username + '/GeekDictionary Software/Applications/Currency Exchange/SplashScreen.gif'
    path_linux = '/usr/local/bin/GeekDictionary Software/Applications/Currency Exchange'
    sg.PopupAnimated(path_linux)
    time.sleep(3)
    sg.PopupAnimated(None)
