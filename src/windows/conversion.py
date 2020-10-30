"""
Unit 1: Coding Project 
Conversion.py - Developed by Alen Jo 
[Database and all information is accredited to coinbase for cryptocurrency and morningstar for print]

# and Multi-Lined show titles as well as the functions blurred out because of techsmart's system
**This code by the way is super massive, upto 1K lines of code programmed** 
"""
### - Import Statements - ### 
import sys 
import time 
import menuOption 
import os 
from os import system, name 

### - Dictionary - ### 
print_currencies = {
    "BRL":"Brazilian Real",
    "USD":"US Dollar",
    "EUR":"European Euro",
    "GBP":"Great Britain Pound", 
    "INR":"Indian Rupee", 
    "JPY":"Japanese Yen", 
    "CHF":"Swiss Franc", 
    "CAD":"Canadian Dollar" 
}

crypto_currencies = {
    "ETH":"Ethereum", 
    "XBT":"Bitcoin"
}

### - Clear Function - ### 
def clear_screen(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

#### - Currency Exchance - #### 
### - Brazilian Reals Conversion - ###
def brl_to_usd():
    print("You have selected the " + print_currencies.get("BRL") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.18
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " U.S dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def brl_to_eur(): 
    print("You have selected the " + print_currencies.get("BRL") + " to " + print_currencies.get("EUR"))
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.15 
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " European euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen() 
    conversionComplete() 

def brl_to_gbp(): 
    print("You have selected the " + print_currencies.get("BRL") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.14
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " Great British pounds.") 
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete()  

def brl_to_inr(): 
    print("You have selected the " + print_currencies.get("BRL") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 13.14
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " Indian rupees.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def brl_to_jpy(): 
    print("You have selected the " + print_currencies.get("BRL") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 18.67
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " Japanese yens.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def brl_to_chf(): 
    print("You have selected the " + print_currencies.get("BRL") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.16
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " Swiss francs.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def brl_to_cad(): 
    print("You have selected the " + print_currencies.get("BRL") + " to " + print_currencies.get("CAD"))
    print("")
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.23
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " Canadian dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def brl_to_eth(): 
    print("You have selected the " + print_currencies.get("BRL") + " to " + crypto_currencies.get("ETH"))
    print("")
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.00044
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def brl_to_xbt(): 
    print("You have selected the " + print_currencies.get("BRL") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many reais? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.000013
    print("")
    print(str(base_value) + " Brazilian reais is equal to " + str(user_value) + " Bitcoins.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete()  

### - US Dollar Conversion - ###

def usd_to_brl(): 
    print("You have selected the " + print_currencies.get("USD") +  " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 5.62
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " Brazilian Reals.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def usd_to_eur(): 
    print("You have selected the " + print_currencies.get("USD")  + " to "  + print_currencies.get("EUR"))
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.85
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " European Euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def usd_to_gbp(): 
    print("You have selected the " + print_currencies.get("USD") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.77
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " Great British Pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def usd_to_inr(): 
    print("You have selected the " + print_currencies.get("USD") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 73.99
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " Indian Rupees.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def usd_to_jpy(): 
    print("You have selected the " + print_currencies.get("USD") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 105
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " Japanese Yens.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def usd_to_chf(): 
    print("You have selected the " + print_currencies.get("USD") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.91
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " Swiss Francs.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def usd_to_cad(): 
    print("You have selected the " + print_currencies.get("USD") + " to " + print_currencies.get("CAD"))
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.32
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " Canadian Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def usd_to_eth(): 
    print("You have selected the " + print_currencies.get("USD") + " to " + crypto_currencies.get("ETH")) 
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.0025
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def usd_to_xbt(): 
    print("You have selected the " + print_currencies.get("USD") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many US dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.000076
    print("")
    print(str(base_value) + " US Dollar is equal to " + str(user_value) + " Bitcoins.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

### - European Euro - ### 

def eur_to_brl(): 
    print("You have selected the " + print_currencies.get("EUR") + " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 6.65
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " Brazilian Reals.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def euro_to_usd(): 
    print("You have selected  the " + print_currencies.get("EUR") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.18
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " US Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def euro_to_gbp(): 
    print("You have selected the " + print_currencies.get("EUR") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.91
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " Great Britain Pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def euro_to_inr(): 
    print("You have selected the " + print_currencies.get("EUR") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.91
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " Indian Rupees.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def euro_to_jpy(): 
    print("You have selected the " + print_currencies.get("EUR") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 123.90
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " Japanese Yens.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def euro_to_chf(): 
    print("You have selected the " + print_currencies.get("EUR") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.07
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " Swiss Francs.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def euro_to_cad(): 
    print("You have selected the " + print_currencies.get("EUR") + " to " + print_currencies.get("CAD"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.56
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " Canadian Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def euro_to_eth(): 
    print("You have selected the " + print_currencies.get("EUR") + " to " + crypto_currencies.get("ETH"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.0030
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def euro_to_xbt(): 
    print("You have selected the " + print_currencies.get("EUR") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many Euros? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.000090
    print("")
    print(str(base_value) + " European Euro is equal to " + str(user_value) + " Bitcoins.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

### - Great British Pounds - ### 

def gbp_to_brl(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("BRL"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Great British Pounds? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - #  
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 7.31
    # - new line - # 
    print("")
    # - Return new message of I/O - # 
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Brazilian Reals.")
    # - Show 5 Second Warning - # 
    print("*Clearing in 5 seconds*") 
    # - wait - # 
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - # 
    conversionComplete() 

def gbp_to_usd(): 
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.30
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " US Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def gbp_to_eur(): 
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("EUR"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.10
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " European Euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def gbp_to_inr(): 
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 96.18
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Indian Rupees.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def gbp_to_jpy(): 
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 136.45
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Japanese Yens.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

## - GBP --> CHF Function- ## 
def gbp_to_chf(): 
    # - message confirm conversion - #
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("CHF"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Great British Pounds? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 1.18
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Swiss Francs.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def gbp_to_cad(): 
    # - message confirm conversion - #
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("CAD"))
    # - new line - #
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Great British Pounds? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 1.72
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Canadian Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def gbp_to_eth(): 
    # - message confirm conversion - #
    print("You have selected the " + print_currencies.get("GBP") + " to " + crypto_currencies.get("ETH"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Great British Pounds? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.0033
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Etherums.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete()  

def gbp_to_xbt(): 
    # - message confirm conversion - #
    print("You have selected the " + print_currencies.get("GBP") + " to " + crypto_currencies.get("XBT"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Great British Pounds? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.000099
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Great British Pounds.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

### - Indian Rupees - ###

def inr_to_brl(): 
    # - message confirm conversion - #
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("BRL"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.076
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Brazilian Reals.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def inr_to_usd(): 
    # - message confirm conversion - #  
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("USD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.014
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " US Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def inr_to_eur(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("EUR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.011
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " European Euros.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def inr_to_gbp(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("GBP"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.010
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Great British Pounds.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def inr_to_jpy(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("JPY"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 1.42
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Japanese Yen.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def inr_to_chf(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("CHF"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.012
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Swiss Franc.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def inr_to_cad(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("CAD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.018
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Canadian Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def inr_to_eth(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("INR") + " to " + crypto_currencies.get("ETH"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.000034
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Etherums.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def inr_to_xbt(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("INR") + " to " + crypto_currencies.get("XBT"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Indian Rupees? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.0000010
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Bitcoins.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

### - Japanese Yen - ### 
## - JPY --> BRL - ## 
def jpy_to_brl(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("BRL"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Japanese Yen? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.054
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Brazilian Reals.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - JPY --> USD - ## 
def jpy_to_usd(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("USD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Japanese Yen? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.0095
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " U.S Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - JPY --> EUR - ## 
def jpy_to_eur(): 
    # - message confirm conversion - #
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("EUR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Japanese Yen? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.0081
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " European Euros.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - JPY --> GBP - ## 
def jpy_to_gbp(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("GBP"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Japanese Yen? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.0073
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Great British Pounds.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - JPY --> INR - ## 
def jpy_to_inr(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("INR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Japanese Yen? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.71
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Indian Rupee.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - JPY --> CHF - ## 
def jpy_to_chf(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("CHF"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Japanese Yen? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.0087
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Swiss Francs.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - JPY --> CAD - ## 
def jpy_to_cad(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("CAD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    print("Converting...")
    # - Show converting message - #
    time.sleep(3)
    # - wait - # 
    user_value = float(input("How many Japanese Yen? "))
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.013
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Canadian Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - JPY --> ETH - ## 
def jpy_to_eth(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("JPY") + " to " + crypto_currencies.get("ETH"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Japanese Yen? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.000025
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Etherums.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - JPY --> XBT - ## 
def jpy_to_xbt(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("JPY") + " to " + crypto_currencies.get("XBT"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Japanese Yen? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value
    user_value *= 0.00000075
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Bitcoins.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

### - Swiss Franc - ### 

## - CHF --> BRL - ## 
def chf_to_brl(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("BRL"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 6.21
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Brazilian Reals.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CHF --> USD - ## 
def chf_to_usd(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("USD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 1.10
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " U.S Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CHF --> EUR - ## 
def chf_to_eur(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("EUR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.93
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " European Euros.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CHF --> GBP - ## 
def chf_to_gbp(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("GBP"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.85
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Great British Pounds.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CHF --> INR - ## 
def chf_to_inr(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("INR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.85
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Indian Rupees.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CHF --> JPY - ## 
def chf_to_jpy(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("JPY"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 115.54
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Japanese Yen.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CHF --> CAD - ## 
def chf_to_cad(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("CAD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 1.46
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Canadian Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CHF --> ETH - ## 
def chf_to_eth(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + crypto_currencies.get("ETH"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.0028
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Etherums.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CHF --> XBT - ## 
def chf_to_xbt(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CHF") + " to " + crypto_currencies.get("XBT"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Swiss Franc? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.000085
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Bitcoins.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

### - Canadian Dollars - ### 

## - CAD --> BRL - ## 
def cad_to_brl(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("BRL"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 4.26
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Brazilan Rules.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CAD --> USD - ## 
def cad_to_usd(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("USD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.76
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " U.S Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CAD --> EUR - ## 
def cad_to_eur(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("EUR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.64
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " European Euros.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CAD --> GBP - ## 
def cad_to_gbp(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("GBP"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.58
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Great British Pounds.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CAD --> INR - ## 
def cad_to_inr(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("INR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 56.02
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Indian Rupee.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CAD --> JPY - ## 
def cad_to_jpy(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("JPY"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 79.41
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Japanese Yen.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CAD --> CHF - ## 
def cad_to_chf(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("CHF"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.69
    # - mathmatical multiplication of input --> output - # 
    print("")
    # - new line - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Swiss Franc.")
    # - Return new message of I/O - #
    print("*Clearing in 5 seconds*") 
    # - Show 5 Second Warning - #
    time.sleep(5)
    # - wait - #
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CAD --> ETH - ##
def cad_to_eth(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + crypto_currencies.get("ETH"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.0019
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Etherums.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - CAD --> XBT - ## 
def cad_to_xbt(): 
    # - message confirm conversion - # 
    print("You have selected the " + print_currencies.get("CAD") + " to " + crypto_currencies.get("XBT"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Canadian Dollars? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.000058
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Bitcoins.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

### - Etherums - ### 

## - ETH --> BRL - ## 
def eth_to_brl(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("BRL"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 2190.59
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Brazilian Rules.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - ETH --> USD - ## 
def eth_to_usd(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("USD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 389.41
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " U.S Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - ETH --> EUR - ## 
def eth_to_eur(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("EUR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 329.66
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " European Euros.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - ETH --> GBP - ## 
def eth_to_gbp(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("GBP"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 299.08
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Great Britain Pounds.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - ETH --> INR - ## 
def eth_to_inr(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("INR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 28801.78
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Indian Rupee.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - ETH --> JPY - ## 
def eth_to_jpy(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("JPY"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 40830.54
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Japanese Yen.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - ETH --> CHF - ## 
def eth_to_chf(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("CHF"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 353.32
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Swiss Franc.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - ETH --> CAD - ## 
def eth_to_cad(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("CAD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 513.99
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Canadian Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - ETH --> XBT - ## 
def eth_to_xbt(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + crypto_currencies.get("XBT"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Etherums? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 0.030
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Bitcoins.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

### - Bitcoins - ### 

## - XBT --> BRL - ## 
def xbt_to_brl(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("BRL"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 72899.48
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Brazilian Rules.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - XBT --> USD - ## 
def xbt_to_usd(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("USD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 12953.00
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " U.S Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - XBT --> EUR - ## 
def xbt_to_eur(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("EUR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 10965.56
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " European Euros.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - XBT --> GBP - ## 
def xbt_to_gbp(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("GBP"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 9946.80
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Great British pounds.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - XBT --> INR - ## 
def xbt_to_inr(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("INR"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value     
    user_value *= 958062.17
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Indian Rupee.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - XBT --> JPY - ## 
def xbt_to_jpy(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("JPY"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 1358109.10
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Japanese Yen.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - XBT --> CHF - ## 
def xbt_to_chf(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("CHF"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 11755.06
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Swiss Franc.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - XBT --> CAD - ## 
def xbt_to_cad(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("CAD"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 17106.54
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Canadian Dollars.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

## - XBT --> ETH - ##  
def xbt_to_eth(): 
    # - message confirm conversion - # 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + crypto_currencies.get("ETH"))
    # - new line - # 
    print("")
    # - ask user of base currency amount - #
    user_value = float(input("How many Bitcoins? "))
    # - Show converting message - #
    print("Converting...")
    # - wait - # 
    time.sleep(3)
    # - mathmatical multiplication of input --> output - # 
    base_value = user_value 
    user_value *= 33.25
    # - new line - #
    print("")
    # - Return new message of I/O - #
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Etherums.")
    # - Show 5 Second Warning - #
    print("*Clearing in 5 seconds*") 
    # - wait - #
    time.sleep(5)
    clear_screen()
    # - goto function to repeat program - #
    conversionComplete() 

def conversionComplete(): 
    print("")
    user_input = input("Would you like to continue? [Type Yes or No] ")
    if user_input in ["YES", "y", "Yes", "yes"]: 
        menuOption.printList() 
        menuOption.currency_matcher() 
    elif user_input in ["NO", "No", "no", "n"]: 
        sys.exit(1)
    else: 
        print("Invalid option, restarting question!")
        time.sleep(3)
        clear_screen() 
        conversionComplete() 