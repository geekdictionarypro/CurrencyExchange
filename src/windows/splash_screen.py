from tkinter import *
import tkinter as tk
import getpass 
import os 
import urllib.request  
import ctypes, sys
import time 

def grabImage(): 
    username = getpass.getuser() 
    url = 'https://lh3.googleusercontent.com/pw/ACtC-3fHOEA9MFJ8hd7XkNKJWGNJ3DW4SFx0DbJtE91dQYSUMiyrjH2z1wh4nfeI7x7EifwcB3I64H-5V6YyaeoLReMpwBJyycFmwdS0xAJHuV-UL9wnSmV6_aeB-9GPebTfTZ4FWVPjnjpsv3KvjUrdxw6j=w300-h500-no?authuser=0'
    path_1 = 'C:/Users/' + username + '/GeekDictionary Software/Applications/Currency Exchange/'
    fullfilename = os.path.join(path_1, 'SplashScreen.gif')
    urllib.request.urlretrieve(url, fullfilename)

def geek_dictionarySoftwareFolder():
    try: 
        username = getpass.getuser() 
        if not os.path.exists('C:/Users/' + username + '/GeekDictionary Software/'):
            path = 'C:/Users/' + username + '/GeekDictionary Software/'
            os.makedirs(path)
            applications_folder() 
        else: 
            splashscreen() 
    except FileExistsError: 
        try: 
           path = 'C:/Users/' + username + '/GeekDictionary Software/'
           os.rmdir(path)
           user_input = input("Type continue > ")
           if user_input in ["continue", "Continue"]: 
               splashscreen()
           else: 
               print("Sorry, Invalid input. Redirecting anyways")
               time.sleep(3)
               applications_folder() 
        except OSError: 
            print("Re-run the program!")
            time.sleep(5)
            sys.exit(1)

def applications_folder(): 
    try: 
        username = getpass.getuser()
        if not os.path.exists('C:/Users/' + username + '/GeekDictionary Software/Application/'):
            path = 'C:/Users/' + username + '/GeekDictionary Software'
            path += '/Applications'
            os.makedirs(path)
            currency_exchangeFolder() 
        else: 
            splashscreen() 
    except FileExistsError: 
        try: 
           path = 'C:/Users/' + username + '/GeekDictionary Software/'
           os.rmdir(path)
           user_input = input("Type continue > ")
           if user_input in ["continue", "Continue"]: 
               splashscreen()
           else: 
               print("Sorry, Invalid input. Redirecting anyways")
               time.sleep(3)
               applications_folder() 
        except OSError: 
            print("Re-run the program!")
            time.sleep(5)
            sys.exit(1)

def currency_exchangeFolder(): 
    try: 
        username = getpass.getuser()
        if not os.path.exists('C:/Users/' + username + '/GeekDictionary Software/Application/Currency Exchange/'):
            path = 'C:/Users/' + username + '/GeekDictionary Software/Applications'
            path += '/Currency Exchange/'
            os.makedirs(path)
            grabImage() 
        else: 
            splashscreen()  
    except FileExistsError: 
        try: 
           path = 'C:/Users/' + username + '/GeekDictionary Software/Application/Currency Exchange/'
           os.rmdir(path)
           user_input = input("Type continue > ")
           if user_input in ["continue", "Continue"]: 
               splashscreen()
           else: 
               print("Sorry, Invalid input. Redirecting anyways")
               time.sleep(3)
               applications_folder() 
        except OSError: 
            print("Re-run the program!")
            time.sleep(5)
            sys.exit(1)

def createDirectory():
    username = getpass.getuser() 
    if not os.path.exists('C:/Users/' + username + '/GeekDictionary Software/Application/Currency Exchange/'):
        geek_dictionarySoftwareFolder() 
        applications_folder() 
        currency_exchangeFolder() 
    else: 
        splashscreen() 

def splashscreen(): 
    username = getpass.getuser() 
    path_2 = 'C:/Users/' + username + '/GeekDictionary Software/Applications/Currency Exchange/SplashScreen.gif'
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

splashscreen()