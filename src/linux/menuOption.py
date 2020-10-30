"""
Unit 1: Coding Project 
menuOption.py - Developed by Alen Jo 

[Database and all information is accredited to coinbase for cryptocurrency and morningstar for print]
**This is the second-largest file in this whole system** 
"""
# - Import Statements - # 
import conversion 
import time 
import sys 

# - Python Dictionaries, print and crypto - # 
print_currencies = {
    "BRL":"(Brazilian Real)",
    "USD":"(US Dollar)",
    "EUR":"(Euro)",
    "GBP":"(Great Britain Pound)", 
    "INR":"(Indian Rupee)", 
    "JPY":"(Japanese Yen)", 
    "CHF":"(Swiss Franc)", 
    "CAD":"(Canadian Dollar)"
}

crypto_currencies = {
    "ETH":"(Ethereum)", 
    "XBT":"(Bitcoin)"
}

### - Environment Back-End - ### 
def introduction(): 
    print("Welcome to currency exchange.")
    print("")
    time.sleep(4)
    conversion.clear_screen() 
    print("*Note that this program isn't real time as that would take weeks to develop")
    print("")
    time.sleep(4)
    conversion.clear_screen() 
    print("**Please remember that if you input a negative, fraction, or a word, the program is designed to close automatically**")
    print("")
    time.sleep(4)
    conversion.clear_screen() 
    print("***You can also type exit on both Convert and To if you'd like to leave the program!***")
    print("")
    time.sleep(4)
    conversion.clear_screen() 
    print("Credits to coinbase and morningstar for the data!")
    print("")
    time.sleep(4)
    conversion.clear_screen() 
    print("Supported currencies:")
    print("")

### - For statements to print the List - ### 
def printList(): 
    print("-" * 3 + "Print Currencies" + "-" * 3)
    for x, y in print_currencies.items():
        print(x, y)
    print("-" * 3 + "Crypto Currencies" + "-" * 3)
    for a, b in crypto_currencies.items(): 
        print(a, b)

def currency_matcher(): 
    user_choice1 = input("Convert: ")
    user_choice2 = input("To: ")
    if user_choice1 == "BRL" and user_choice2 == "USD":
        conversion.brl_to_usd() 
    ### - Brazilian Rubles - ### 
    elif user_choice1 == "BRL" and user_choice2 == "EUR":
        conversion.brl_to_eur() 
    elif user_choice1 == "BRL" and user_choice2 == "GBP":
        conversion.brl_to_gbp() 
    elif user_choice1 == "BRL" and user_choice2 == "INR": 
        conversion.brl_to_inr() 
    elif user_choice1 == "BRL" and user_choice2 == "JPY":
        conversion.brl_to_jpy()
    elif user_choice1 == "BRL" and user_choice2 == "CHF":
        conversion.brl_to_chf()
    elif user_choice1 == "BRL" and user_choice2 == "CAD":
        conversion.brl_to_cad() 
    elif user_choice1 == "BRL" and user_choice2 == "ETH":
        conversion.brl_to_eth() 
    elif user_choice1 == "BRL" and user_choice2 == "XBT":
        conversion.brl_to_xbt() 
    ### - U.S Dollars - ### 
    elif user_choice1 == "USD" and user_choice2 == "BRL":
        conversion.usd_to_brl() 
    elif user_choice1 == "USD" and user_choice2 == "EUR":
        conversion.usd_to_eur() 
    elif user_choice1 == "USD" and user_choice2 == "GBP":
        conversion.usd_to_gbp() 
    elif user_choice1 == "USD" and user_choice2 == "INR":
        conversion.usd_to_inr() 
    elif user_choice1 == "USD" and user_choice2 == "JPY":
        conversion.usd_to_jpy() 
    elif user_choice1 == "USD" and user_choice2 == "CHF":
        conversion.usd_to_chf() 
    elif user_choice1 == "USD" and user_choice2 == "CAD":
        conversion.usd_to_cad() 
    elif user_choice1 == "USD" and user_choice2 == "ETH":
        conversion.usd_to_eth() 
    elif user_choice1 == "USD" and user_choice2 == "XBT":
        conversion.usd_to_xbt() 
    ### - European Euros - ### 
    elif user_choice1 == "EUR" and user_choice2 == "BRL":
        conversion.eur_to_brl() 
    elif user_choice1 == "EUR" and user_choice2 == "USD":
        conversion.euro_to_usd() 
    elif user_choice1 == "EUR" and user_choice2 == "GBP":
        conversion.euro_to_gbp() 
    elif user_choice1 == "EUR" and user_choice2 == "INR":
        conversion.euro_to_inr() 
    elif user_choice1 == "EUR" and user_choice2 == "JPY":
        conversion.euro_to_jpy() 
    elif user_choice1 == "EUR" and user_choice2 == "CHF":
        conversion.euro_to_chf() 
    elif user_choice1 == "EUR" and user_choice2 == "CAD":
        conversion.euro_to_cad() 
    elif user_choice1 == "EUR" and user_choice2 == "ETH":
        conversion.euro_to_eth() 
    elif user_choice1 == "EUR" and user_choice2 == "XBT":
        conversion.euro_to_xbt() 
    ### - Great British Pounds - ### 
    elif user_choice1 == "GBP" and user_choice2 == "BRL":
        conversion.gbp_to_brl() 
    elif user_choice1 == "GBP" and user_choice2 == "USD":
        conversion.gbp_to_usd() 
    elif user_choice1 == "GBP" and user_choice2 == "EUR": 
        conversion.gbp_to_eur()
    elif user_choice1 == "GBP" and user_choice2 == "INR": 
        conversion.gbp_to_inr() 
    elif user_choice1 == "GBP" and user_choice2 == "JPY": 
        conversion.gbp_to_jpy() 
    elif user_choice1 == "GBP" and user_choice2 == "CHF": 
        conversion.gbp_to_chf() 
    elif user_choice1 == "GBP" and user_choice2 == "CAD": 
        conversion.gbp_to_cad() 
    elif user_choice1 == "GBP" and user_choice2 == "ETH": 
        conversion.gbp_to_eth() 
    elif user_choice1 == "GBP" and user_choice2 == "XBT": 
        conversion.gbp_to_xbt() 
    ### - Indian Rupee - ### 
    elif user_choice1 == "INR" and user_choice2 == "BRL": 
        conversion.inr_to_brl() 
    elif user_choice1 == "INR" and user_choice2 == "USD": 
        conversion.inr_to_usd() 
    elif user_choice1 == "INR" and user_choice2 == "EUR": 
        conversion.inr_to_eur() 
    elif user_choice1 == "INR" and user_choice2 == "GBP": 
        conversion.inr_to_gbp() 
    elif user_choice1 == "INR" and user_choice2 == "JPY":
        conversion.inr_to_jpy() 
    elif user_choice1 == "INR" and user_choice2 == "CHF": 
        conversion.inr_to_chf()  
    elif user_choice1 == "INR" and user_choice2 == "CAD": 
        conversion.inr_to_cad() 
    elif user_choice1 == "INR" and user_choice2 == "ETH": 
        conversion.inr_to_eth() 
    elif user_choice1 == "INR" and user_choice2 == "XBT": 
        conversion.inr_to_xbt() 
    ### - Japanese Yen - ### 
    elif user_choice1 == "JPY" and user_choice2 == "BRL": 
        conversion.jpy_to_brl() 
    elif user_choice1 == "JPY" and user_choice2 == "USD": 
        conversion.jpy_to_usd() 
    elif user_choice1 == "JPY" and user_choice2 == "EUR":
        conversion.jpy_to_eur() 
    elif user_choice1 == "JPY" and user_choice2 == "GBP":  
        conversion.jpy_to_gbp() 
    elif user_choice1 == "JPY" and user_choice2 == "INR":
        conversion.jpy_to_inr() 
    elif user_choice1 == "JPY" and user_choice2 == "CHF":
        conversion.jpy_to_chf() 
    elif user_choice1 == "JPY" and user_choice2 == "CAD":
        conversion.jpy_to_cad() 
    elif user_choice1 == "JPY" and user_choice2 == "ETH":    
        conversion.jpy_to_eth() 
    elif user_choice1 == "JPY" and user_choice2 == "XBT": 
        conversion.jpy_to_xbt() 
    ### - Swiss Franc - ### 
    elif user_choice1 == "CHF" and user_choice2 == "BRL":
        conversion.chf_to_brl() 
    elif user_choice1 == "CHF" and user_choice2 == "USD":
        conversion.chf_to_usd() 
    elif user_choice1 == "CHF" and user_choice2 == "EUR":  
        conversion.chf_to_eur() 
    elif user_choice1 == "CHF" and user_choice2 == "GBP":
        conversion.chf_to_gbp() 
    elif user_choice1 == "CHF" and user_choice2 == "INR":
        conversion.chf_to_inr() 
    elif user_choice1 == "CHF" and user_choice2 == "JPY":
        conversion.chf_to_jpy() 
    elif user_choice1 == "CHF" and user_choice2 == "CAD":    
        conversion.chf_to_cad() 
    elif user_choice1 == "CHF" and user_choice2 == "ETH": 
        conversion.chf_to_eth() 
    elif user_choice1 == "CHF" and user_choice2 == "XBT": 
        conversion.chf_to_xbt() 
    ### - Canadian Dollars - ### 
    elif user_choice1 == "CAD" and user_choice2 == "BRL": 
        conversion.cad_to_brl() 
    elif user_choice1 == "CAD" and user_choice2 == "USD":
        conversion.cad_to_usd() 
    elif user_choice1 == "CAD" and user_choice2 == "EUR":
        conversion.cad_to_eur()
    elif user_choice1 == "CAD" and user_choice2 == "GBP":
        conversion.cad_to_gbp() 
    elif user_choice1 == "CAD" and user_choice2 == "INR":
        conversion.cad_to_inr() 
    elif user_choice1 == "CAD" and user_choice2 == "JPY":
        conversion.cad_to_jpy() 
    elif user_choice1 == "CAD" and user_choice2 == "CHF":
        conversion.cad_to_chf() 
    elif user_choice1 == "CAD" and user_choice2 == "ETH":
        conversion.cad_to_eth() 
    elif user_choice1 == "CAD" and user_choice2 == "XBT":
        conversion.cad_to_xbt() 
    ### - Etherum (Crypto) - ### 
    elif user_choice1 == "ETH" and user_choice2 == "BRL":
        conversion.eth_to_brl() 
    elif user_choice1 == "ETH" and user_choice2 == "USD":
        conversion.eth_to_usd() 
    elif user_choice1 == "ETH" and user_choice2 == "EUR":
        conversion.eth_to_eur() 
    elif user_choice1 == "ETH" and user_choice2 == "GBP":
        conversion.eth_to_gbp() 
    elif user_choice1 == "ETH" and user_choice2 == "INR":
        conversion.eth_to_inr() 
    elif user_choice1 == "ETH" and user_choice2 == "JPY":
        conversion.eth_to_jpy() 
    elif user_choice1 == "ETH" and user_choice2 == "CHF":
        conversion.eth_to_chf() 
    elif user_choice1 == "ETH" and user_choice2 == "CAD":
        conversion.eth_to_cad() 
    elif user_choice1 == "ETH" and user_choice2 == "XBT":
        conversion.eth_to_xbt() 
    ### - Bitcoin (Crypto) - ### 
    elif user_choice1 == "XBT" and user_choice2 == "BRL":
        conversion.xbt_to_brl() 
    elif user_choice1 == "XBT" and user_choice2 == "USD": 
        conversion.xbt_to_usd() 
    elif user_choice1 == "XBT" and user_choice2 == "EUR":
        conversion.xbt_to_eur() 
    elif user_choice1 == "XBT" and user_choice2 == "GBP":
        conversion.xbt_to_gbp() 
    elif user_choice1 == "XBT" and user_choice2 == "INR":
        conversion.xbt_to_inr() 
    elif user_choice1 == "XBT" and user_choice2 == "JPY":
        conversion.xbt_to_jpy() 
    elif user_choice1 == "XBT" and user_choice2 == "CHF":
        conversion.xbt_to_chf() 
    elif user_choice1 == "XBT" and user_choice2 == "CAD":
        conversion.xbt_to_cad() 
    elif user_choice1 == "XBT" and user_choice2 == "ETH":
        conversion.xbt_to_eth() 
    ### - Special Status Codes - ### 
    elif user_choice1 in ["Exit", "exit"] and user_choice2 in ["Exit", "exit"]: 
        sys.exit(1)
    else: 
        print("Sorry, try again!")
        currency_matcher()