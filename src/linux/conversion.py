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
    user_value *= 18.67
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
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 7.31
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Brazilian Reals.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
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

def gbp_to_chf(): 
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.18
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Swiss Francs.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def gbp_to_cad(): 
    print("You have selected the " + print_currencies.get("GBP") + " to " + print_currencies.get("CAD"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.72
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Canadian Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def gbp_to_eth(): 
    print("You have selected the " + print_currencies.get("GBP") + " to " + crypto_currencies.get("ETH"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.0033
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete()  

def gbp_to_xbt(): 
    print("You have selected the " + print_currencies.get("GBP") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many Great British Pounds? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.000099
    print("")
    print(str(base_value) + " Great British Pound is equal to " + str(user_value) + " Great British Pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

### - Indian Rupees - ###

def inr_to_brl(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.076
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Brazilian Reals.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def inr_to_usd(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.014
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " US Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def inr_to_eur(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("EUR"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.011
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " European Euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def inr_to_gbp(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.010
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Great British Pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def inr_to_jpy(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 1.42
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Japanese Yen.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def inr_to_chf(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.012
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Swiss Franc.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def inr_to_cad(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + print_currencies.get("CAD"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.018
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Canadian Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def inr_to_eth(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + crypto_currencies.get("ETH"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.000034
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def inr_to_xbt(): 
    print("You have selected the " + print_currencies.get("INR") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many Indian Rupees? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.0000010
    print("")
    print(str(base_value) + " Indian Rupees is equal to " + str(user_value) + " Bitcoins.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

### - Japanese Yen - ### 

def jpy_to_brl(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many Japanese Yen? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.054
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Brazilian Reals.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def jpy_to_usd(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many Japanese Yen? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.0095
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " U.S Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def jpy_to_eur(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("EUR"))
    print("")
    user_value = float(input("How many Japanese Yen? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.0081
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " European Euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def jpy_to_gbp(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many Japanese Yen? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.0073
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Great British Pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def jpy_to_inr(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many Japanese Yen? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.71
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Indian Rupee.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def jpy_to_chf(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many Japanese Yen? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.0087
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Swiss Francs.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def jpy_to_cad(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + print_currencies.get("CAD"))
    print("")
    print("Converting...")
    time.sleep(3)
    user_value = float(input("How many Japanese Yen? "))
    base_value = user_value
    user_value *= 0.013
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Canadian Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def jpy_to_eth(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + crypto_currencies.get("ETH"))
    print("")
    user_value = float(input("How many Japanese Yen? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.000025
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def jpy_to_xbt(): 
    print("You have selected the " + print_currencies.get("JPY") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many Japanese Yen? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value
    user_value *= 0.00000075
    print("")
    print(str(base_value) + " Japanese Yen is equal to " + str(user_value) + " Bitcoins.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

### - Swiss Franc - ### 

def chf_to_brl(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 6.21
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Brazilian Reals.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def chf_to_usd(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 1.10
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " U.S Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def chf_to_eur(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("EUR"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.93
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " European Euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def chf_to_gbp(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.85
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Great British Pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def chf_to_inr(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.85
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Indian Rupees.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def chf_to_jpy(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 115.54
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Japanese Yen.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def chf_to_cad(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + print_currencies.get("CAD"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 1.46
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Canadian Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def chf_to_eth(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + crypto_currencies.get("ETH"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.0028
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def chf_to_xbt(): 
    print("You have selected the " + print_currencies.get("CHF") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many Swiss Franc? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.000085
    print("")
    print(str(base_value) + " Swiss Franc is equal to " + str(user_value) + " Bitcoins.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

### - Canadian Dollars - ### 

def cad_to_brl(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 4.26
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Brazilan Rules.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def cad_to_usd(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.76
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " U.S Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def cad_to_eur(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("EUR"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.64
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " European Euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def cad_to_gbp(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.58
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Great British Pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def cad_to_inr(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 56.02
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Indian Rupee.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def cad_to_jpy(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 79.41
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Japanese Yen.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def cad_to_chf(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.69
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Swiss Franc.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def cad_to_eth(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + crypto_currencies.get("ETH"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.0019
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def cad_to_xbt(): 
    print("You have selected the " + print_currencies.get("CAD") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many Canadian Dollars? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.000058
    print("")
    print(str(base_value) + " Canadian Dollars is equal to " + str(user_value) + " Bitcoins.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

### - Etherums - ### 

def eth_to_brl(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 2190.59
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Brazilian Rules.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def eth_to_usd(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 389.41
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " U.S Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def eth_to_eur(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("EUR"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 329.66
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " European Euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def eth_to_gbp(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 299.08
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Great Britain Pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def eth_to_inr(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 28801.78
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Indian Rupee.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def eth_to_jpy(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 40830.54
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Japanese Yen.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def eth_to_chf(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 353.32
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Swiss Franc.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def eth_to_cad(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + print_currencies.get("CAD"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 513.99
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Canadian Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def eth_to_xbt(): 
    print("You have selected the " + crypto_currencies.get("ETH") + " to " + crypto_currencies.get("XBT"))
    print("")
    user_value = float(input("How many Etherums? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 0.030
    print("")
    print(str(base_value) + " Etherums is equal to " + str(user_value) + " Bitcoins.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

### - Bitcoins - ### 

def xbt_to_brl(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("BRL"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 72899.48
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Brazilian Rules.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def xbt_to_usd(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("USD"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 12953.00
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " U.S Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def xbt_to_eur(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("EUR"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 10965.56
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " European Euros.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def xbt_to_gbp(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("GBP"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 9946.80
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Great British pounds.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def xbt_to_inr(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("INR"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 958062.17
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Indian Rupee.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def xbt_to_jpy(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("JPY"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 1358109.10
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Japanese Yen.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def xbt_to_chf(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("CHF"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 11755.06
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Swiss Franc.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def xbt_to_cad(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + print_currencies.get("CAD"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 17106.54
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Canadian Dollars.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
    conversionComplete() 

def xbt_to_eth(): 
    print("You have selected the " + crypto_currencies.get("XBT") + " to " + crypto_currencies.get("ETH"))
    print("")
    user_value = float(input("How many Bitcoins? "))
    print("Converting...")
    time.sleep(3)
    base_value = user_value 
    user_value *= 33.25
    print("")
    print(str(base_value) + " Bitcoins is equal to " + str(user_value) + " Etherums.")
    print("*Clearing in 5 seconds*") 
    time.sleep(5)
    clear_screen()
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