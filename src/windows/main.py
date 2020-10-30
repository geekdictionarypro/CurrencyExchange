"""
Unit 1: Coding Project 
main.py - Developed by Alen Jo 
[Database and all information is accredited to coinbase for cryptocurrency and morningstar for print]

# and Multi-Lined show titles as well as the functions blurred out because of techsmart's system
**This is the lowest amount of lines of code because this is easier to analyze**
"""
# - Import Statement (back-end), where all the magic happens - # 
import menuOption
import splash_screen 

### - Front-End (user can see this) - ###
# - Splash Screen - # 
splash_screen.splashscreen() 
# - Print the Introduction - # 
menuOption.introduction()

# - Print the list of currencies - # 
menuOption.printList() 

# - Ask user for base currency to target currency and the program continues to another file --> conversion.py - # 
menuOption.currency_matcher() 

