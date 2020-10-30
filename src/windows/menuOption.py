"""
Unit 1: Coding Project 
menuOption.py - Developed by Alen Jo 

[Database and all information is accredited to coinbase for cryptocurrency and morningstar for print]
**This is the second-largest file in this whole system** 
"""
# - Import Statements (implicit) - # 
import conversion 
# - Import Statements (explicit) - # 
import time 
import sys 

## - Python Dictionaries, print and crypto - ##
# - Print currencies dictionary - # 
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

# - Crypto currencies dictionary - # 
crypto_currencies = {
    "ETH":"(Ethereum)", 
    "XBT":"(Bitcoin)"
}

### - Environment Back-End - ### 
## - Function introduction - ## 
def introduction(): 
    # - Show message to console - # 
    print("Welcome to currency exchange.")
    # - New Line - # 
    print("")
    # - Timeout (wait) - # 
    time.sleep(4)
    # - Show message to console - # 
    print("*Note that this program isn't real time as that would take weeks to develop")
    # - New Line - # 
    print("")
    # - Timeout (wait) - # 
    time.sleep(4)
    # - Show message to console - # 
    print("**Please remember that if you input a negative, fraction, or a word, the program is designed to close automatically**")
    # - New Line - # 
    print("")
    # - Timeout (wait) - # 
    time.sleep(4)
    # - Show message to console - # 
    print("***You can also type exit on both Convert and To if you'd like to leave the program!***")
    # - New Line - # 
    print("")
    # - Timeout (wait) - # 
    time.sleep(4)
    # - Show message to console - # 
    print("Credits to coinbase and morningstar for the data!")
    # - New Line - # 
    print("")
    # - Timeout (wait) - # 
    time.sleep(4)
    # - Show message to console - # 
    print("Supported currencies:")
    # - New Line - # 
    print("")


### - For statements to print the List - ### 
## - Function printList - ## 
def printList(): 
    # - show message title - # 
    print("-" * 3 + "Print Currencies" + "-" * 3)
    # - for loop to print each element and key for --> printCurrency - # 
    for x, y in print_currencies.items():
        # - print both the element and key - # 
        print(x, y)
    print("-" * 3 + "Crypto Currencies" + "-" * 3)
    # - for loop to print each element and key for --> crypytoCurrency - # 
    for a, b in crypto_currencies.items(): 
        # - print both the element and key - # 
        print(a, b)


## - Function currencyMatcher - ## 
def currency_matcher(): 
    # - userInput1 for base - # 
    user_choice1 = input("Convert: ")
    # - userInput2 for target - #
    user_choice2 = input("To: ")
    ### - If/Elif statement for converting from Brazilian Reals to USD - ###
    if user_choice1 == "BRL" and user_choice2 == "USD":
        conversion.brl_to_usd() 
    ### - elif statement - Brazilian Rubles BRL --> EUR - ### 
    elif user_choice1 == "BRL" and user_choice2 == "EUR":
        # - redirect - # 
        conversion.brl_to_eur() 
    ### - elif statement - Brazilian Rubles BRL --> GBP - ### 
    elif user_choice1 == "BRL" and user_choice2 == "GBP":
        # - redirect - #
        conversion.brl_to_gbp() 
    ### - elif statement - Brazilian Rubles BRL --> INR - ### 
    elif user_choice1 == "BRL" and user_choice2 == "INR": 
        # - redirect - #
        conversion.brl_to_inr() 
    ### - elif statement - Brazilian Rubles BRL --> JPY - ### 
    elif user_choice1 == "BRL" and user_choice2 == "JPY":
        # - redirect - #
        conversion.brl_to_jpy()
    ### - elif statement - Brazilian Rubles BRL --> CHF - ### 
    elif user_choice1 == "BRL" and user_choice2 == "CHF":
        # - redirect - #
        conversion.brl_to_chf()
    ### - elif statement - Brazilian Rubles BRL --> CAD - ### 
    elif user_choice1 == "BRL" and user_choice2 == "CAD":
        # - redirect - #
        conversion.brl_to_cad() 
    ### - elif statement - Brazilian Rubles BRL --> ETH - ### 
    elif user_choice1 == "BRL" and user_choice2 == "ETH":
        # - redirect - #
        conversion.brl_to_eth() 
    ### - elif statement - Brazilian Rubles BRL --> XBT - ### 
    elif user_choice1 == "BRL" and user_choice2 == "XBT":
        # - redirect - #
        conversion.brl_to_xbt() 

    #### - U.S Dollars - #### 
    ### - elif statement - U.S Dollars  USD --> BRL - ### 
    elif user_choice1 == "USD" and user_choice2 == "BRL":
        # - redirect - #
        conversion.usd_to_brl() 
    ### - elif statement - U.S Dollars  USD --> EUR - ### 
    elif user_choice1 == "USD" and user_choice2 == "EUR":
        # - redirect - #
        conversion.usd_to_eur() 
    ### - elif statement - U.S Dollars  USD --> GBP - ###
    elif user_choice1 == "USD" and user_choice2 == "GBP":
        # - redirect - #
        conversion.usd_to_gbp() 
    ### - elif statement - U.S Dollars  USD --> INR - ### 
    elif user_choice1 == "USD" and user_choice2 == "INR":
        # - redirect - #
        conversion.usd_to_inr() 
    ### - elif statement - U.S Dollars  USD --> JPY - ### 
    elif user_choice1 == "USD" and user_choice2 == "JPY":
        # - redirect - #
        conversion.usd_to_jpy() 
    ### - elif statement - U.S Dollars  USD --> CHF - ###
    elif user_choice1 == "USD" and user_choice2 == "CHF":
        # - redirect - #
        conversion.usd_to_chf() 
    ### - elif statement - U.S Dollars  USD --> CAD - ###    
    elif user_choice1 == "USD" and user_choice2 == "CAD":
        # - redirect - #
        conversion.usd_to_cad() 
    ### - elif statement - U.S Dollars  USD --> ETH - ### 
    elif user_choice1 == "USD" and user_choice2 == "ETH":
        # - redirect - #
        conversion.usd_to_eth() 
    ### - elif statement - U.S Dollars  USD --> XBT - ### 
    elif user_choice1 == "USD" and user_choice2 == "XBT":
        # - redirect - #
        conversion.usd_to_xbt() 

    #### - European Euros - #### 
    ### - elif statement - European Euros EUR --> BRL - ### 
    elif user_choice1 == "EUR" and user_choice2 == "BRL":
        # - redirect - #
        conversion.eur_to_brl() 
    ### - elif statement - European Euros EUR --> USD - ###
    elif user_choice1 == "EUR" and user_choice2 == "USD":
        # - redirect - #
        conversion.euro_to_usd() 
    ### - elif statement - European Euros EUR --> GBP - ### 
    elif user_choice1 == "EUR" and user_choice2 == "GBP":
        # - redirect - #
        conversion.euro_to_gbp() 
    ### - elif statement - European Euros EUR --> INR - ###
    elif user_choice1 == "EUR" and user_choice2 == "INR":
        # - redirect - #
        conversion.euro_to_inr() 
    ### - elif statement - European Euros EUR --> JPY - ### 
    elif user_choice1 == "EUR" and user_choice2 == "JPY":
        # - redirect - #
        conversion.euro_to_jpy() 
    ### - elif statement - European Euros EUR --> CHF - ###
    elif user_choice1 == "EUR" and user_choice2 == "CHF":
        # - redirect - #
        conversion.euro_to_chf() 
    ### - elif statement - European Euros EUR --> CAD - ### 
    elif user_choice1 == "EUR" and user_choice2 == "CAD":
        # - redirect - #
        conversion.euro_to_cad() 
    ### - elif statement - European Euros EUR --> ETH - ### 
    elif user_choice1 == "EUR" and user_choice2 == "ETH":
        # - redirect - #
        conversion.euro_to_eth() 
    ### - elif statement - European Euros EUR --> XBT - ### 
    elif user_choice1 == "EUR" and user_choice2 == "XBT":
        # - redirect - #
        conversion.euro_to_xbt() 

    #### - Great British Pounds - #### 
    ### - elif statement - Great British Pounds GBP --> BRL - ### 
    elif user_choice1 == "GBP" and user_choice2 == "BRL":
        # - redirect - #
        conversion.gbp_to_brl() 
    ### - elif statement - Great British Pounds GBP --> USD - ###
    elif user_choice1 == "GBP" and user_choice2 == "USD":
        # - redirect - #
        conversion.gbp_to_usd() 
    ### - elif statement - Great British Pounds GBP --> EUR - ###
    elif user_choice1 == "GBP" and user_choice2 == "EUR": 
        # - redirect - #
        conversion.gbp_to_eur()
    ### - elif statement - Great British Pounds GBP --> INR - ### 
    elif user_choice1 == "GBP" and user_choice2 == "INR": 
        # - redirect - #
        conversion.gbp_to_inr() 
    ### - elif statement - Great British Pounds GBP --> JPY - ### 
    elif user_choice1 == "GBP" and user_choice2 == "JPY": 
        # - redirect - #
        conversion.gbp_to_jpy() 
    ### - elif statement - Great British Pounds GBP --> CHF - ###
    elif user_choice1 == "GBP" and user_choice2 == "CHF": 
        # - redirect - #
        conversion.gbp_to_chf() 
    ### - elif statement - Great British Pounds GBP --> CAD - ### 
    elif user_choice1 == "GBP" and user_choice2 == "CAD": 
        # - redirect - #
        conversion.gbp_to_cad() 
    ### - elif statement - Great British Pounds GBP --> ETH - ### 
    elif user_choice1 == "GBP" and user_choice2 == "ETH": 
        # - redirect - #
        conversion.gbp_to_eth() 
    ### - elif statement - Great British Pounds GBP --> XBT - ### 
    elif user_choice1 == "GBP" and user_choice2 == "XBT": 
        # - redirect - #
        conversion.gbp_to_xbt() 

    #### - Indian Rupee - #### 
    ### - elif statement - Indian Rupee INR --> BRL - ###
    elif user_choice1 == "INR" and user_choice2 == "BRL": 
        # - redirect - #
        conversion.inr_to_brl() 
    ### - elif statement - Indian Rupee INR --> USD - ### 
    elif user_choice1 == "INR" and user_choice2 == "USD": 
        # - redirect - #
        conversion.inr_to_usd() 
    ### - elif statement - Indian Rupee INR --> EUR - ### 
    elif user_choice1 == "INR" and user_choice2 == "EUR": 
        # - redirect - #
        conversion.inr_to_eur() 
    ### - elif statement - Indian Rupee INR --> GBP - ### 
    elif user_choice1 == "INR" and user_choice2 == "GBP": 
        # - redirect - #
        conversion.inr_to_gbp() 
    ### - elif statement - Indian Rupee INR --> JPY - ### 
    elif user_choice1 == "INR" and user_choice2 == "JPY":
        # - redirect - #
        conversion.inr_to_jpy() 
    ### - elif statement - Indian Rupee INR --> CHF - ###
    elif user_choice1 == "INR" and user_choice2 == "CHF": 
        # - redirect - #
        conversion.inr_to_chf()  
    ### - elif statement - Indian Rupee INR --> CAD - ### 
    elif user_choice1 == "INR" and user_choice2 == "CAD": 
        # - redirect - #
        conversion.inr_to_cad() 
    ### - elif statement - Indian Rupee INR --> ETH - ### 
    elif user_choice1 == "INR" and user_choice2 == "ETH": 
        # - redirect - #
        conversion.inr_to_eth() 
    ### - elif statement - Indian Rupee INR --> XBT - ###
    elif user_choice1 == "INR" and user_choice2 == "XBT": 
        # - redirect - #
        conversion.inr_to_xbt() 

    #### - Japanese Yen - #### 
    ### - elif statement - Japanese Yen JPY --> BRL - ### 
    elif user_choice1 == "JPY" and user_choice2 == "BRL": 
        # - redirect - #
        conversion.jpy_to_brl() 
    ### - elif statement - Japanese Yen JPY --> USD - ###
    elif user_choice1 == "JPY" and user_choice2 == "USD": 
        # - redirect - #
        conversion.jpy_to_usd() 
    ### - elif statement - Japanese Yen JPY --> EUR - ### 
    elif user_choice1 == "JPY" and user_choice2 == "EUR":
        # - redirect - #
        conversion.jpy_to_eur() 
    ### - elif statement - Japanese Yen JPY --> GBP - ### 
    elif user_choice1 == "JPY" and user_choice2 == "GBP":  
        # - redirect - #
        conversion.jpy_to_gbp() 
    ### - elif statement - Japanese Yen JPY --> INR - ###
    elif user_choice1 == "JPY" and user_choice2 == "INR":
        # - redirect - #
        conversion.jpy_to_inr() 
    ### - elif statement - Japanese Yen JPY --> CHF - ###
    elif user_choice1 == "JPY" and user_choice2 == "CHF":
        # - redirect - #
        conversion.jpy_to_chf() 
    ### - elif statement - Japanese Yen JPY --> CAD - ###
    elif user_choice1 == "JPY" and user_choice2 == "CAD":
        # - redirect - #
        conversion.jpy_to_cad() 
    ### - elif statement - Japanese Yen JPY --> ETH - ###
    elif user_choice1 == "JPY" and user_choice2 == "ETH":    
        # - redirect - #
        conversion.jpy_to_eth() 
    ### - elif statement - Japanese Yen JPY --> XBT - ###
    elif user_choice1 == "JPY" and user_choice2 == "XBT": 
        # - redirect - #
        conversion.jpy_to_xbt() 

    #### - Swiss Franc - #### 
    ### - elif statement - Swiss Franc CHF --> BRL - ### 
    elif user_choice1 == "CHF" and user_choice2 == "BRL":
        # - redirect - #
        conversion.chf_to_brl() 
    ### - elif statement - Swiss Franc CHF --> USD - ###
    elif user_choice1 == "CHF" and user_choice2 == "USD":
        # - redirect - #
        conversion.chf_to_usd() 
    ### - elif statement - Swiss Franc CHF --> EUR - ### 
    elif user_choice1 == "CHF" and user_choice2 == "EUR":  
        # - redirect - #
        conversion.chf_to_eur() 
    ### - elif statement - Swiss Franc CHF --> GBP - ###
    elif user_choice1 == "CHF" and user_choice2 == "GBP":
        # - redirect - #
        conversion.chf_to_gbp() 
    ### - elif statement - Swiss Franc CHF --> INR - ###
    elif user_choice1 == "CHF" and user_choice2 == "INR":
        # - redirect - #
        conversion.chf_to_inr() 
    ### - elif statement - Swiss Franc CHF --> JPY - ###
    elif user_choice1 == "CHF" and user_choice2 == "JPY":
        # - redirect - #
        conversion.chf_to_jpy() 
    ### - elif statement - Swiss Franc CHF --> CAD - ###
    elif user_choice1 == "CHF" and user_choice2 == "CAD":    
        # - redirect - #
        conversion.chf_to_cad() 
    ### - elif statement - Swiss Franc CHF --> ETH - ###
    elif user_choice1 == "CHF" and user_choice2 == "ETH": 
        # - redirect - #
        conversion.chf_to_eth() 
    ### - elif statement - Swiss Franc CHF --> XBT - ### 
    elif user_choice1 == "CHF" and user_choice2 == "XBT": 
        # - redirect - #
        conversion.chf_to_xbt() 

    #### - Canadian Dollars - #### 
    ### - elif statement - Canadian Dollars CAD --> BRL - ### 
    elif user_choice1 == "CAD" and user_choice2 == "BRL": 
        # - redirect - #
        conversion.cad_to_brl() 
    ### - elif statement - Canadian Dollars CAD --> USD - ### 
    elif user_choice1 == "CAD" and user_choice2 == "USD":
        # - redirect - #
        conversion.cad_to_usd() 
    ### - elif statement - Canadian Dollars CAD --> EUR - ### 
    elif user_choice1 == "CAD" and user_choice2 == "EUR":
        # - redirect - #
        conversion.cad_to_eur()
    ### - elif statement - Canadian Dollars CAD --> GBP - ###
    elif user_choice1 == "CAD" and user_choice2 == "GBP":
        # - redirect - #
        conversion.cad_to_gbp() 
    ### - elif statement - Canadian Dollars CAD --> INR - ###
    elif user_choice1 == "CAD" and user_choice2 == "INR":
        # - redirect - #
        conversion.cad_to_inr() 
    ### - elif statement - Canadian Dollars CAD --> JPY - ###
    elif user_choice1 == "CAD" and user_choice2 == "JPY":
        # - redirect - #
        conversion.cad_to_jpy() 
    ### - elif statement - Canadian Dollars CAD --> CHF - ###
    elif user_choice1 == "CAD" and user_choice2 == "CHF":
        # - redirect - #
        conversion.cad_to_chf() 
    ### - elif statement - Canadian Dollars CAD --> ETH - ###
    elif user_choice1 == "CAD" and user_choice2 == "ETH":
        # - redirect - #
        conversion.cad_to_eth() 
    ### - elif statement - Canadian Dollars CAD --> XBT - ###
    elif user_choice1 == "CAD" and user_choice2 == "XBT":
        # - redirect - #
        conversion.cad_to_xbt() 

    #### - Etherum (Crypto) - #### 
    ### - elif statement - Etherums ETH --> BRL - ### 
    elif user_choice1 == "ETH" and user_choice2 == "BRL":
        # - redirect - #
        conversion.eth_to_brl() 
    ### - elif statement - Etherums ETH --> USD - ### 
    elif user_choice1 == "ETH" and user_choice2 == "USD":
        # - redirect - #
        conversion.eth_to_usd() 
    ### - elif statement - Etherums ETH --> EUR - ###  
    elif user_choice1 == "ETH" and user_choice2 == "EUR":
        # - redirect - #
        conversion.eth_to_eur() 
    ### - elif statement - Etherums ETH --> GBP - ### 
    elif user_choice1 == "ETH" and user_choice2 == "GBP":
        # - redirect - #
        conversion.eth_to_gbp() 
    ### - elif statement - Etherums ETH --> INR - ###
    elif user_choice1 == "ETH" and user_choice2 == "INR":
        # - redirect - #
        conversion.eth_to_inr() 
    ### - elif statement - Etherums ETH --> JPY - ###
    elif user_choice1 == "ETH" and user_choice2 == "JPY":
        # - redirect - #
        conversion.eth_to_jpy() 
    ### - elif statement - Etherums ETH --> CHF - ###
    elif user_choice1 == "ETH" and user_choice2 == "CHF":
        # - redirect - #
        conversion.eth_to_chf() 
    ### - elif statement - Etherums ETH --> CAD - ###
    elif user_choice1 == "ETH" and user_choice2 == "CAD":
        # - redirect - #
        conversion.eth_to_cad() 
    ### - elif statement - Etherums ETH --> XBT - ###
    elif user_choice1 == "ETH" and user_choice2 == "XBT":
        # - redirect - #
        conversion.eth_to_xbt() 

    ### - Bitcoin (Crypto) - ### 
    ### - elif statement - Bitcoin XBT --> BRL - ### 
    elif user_choice1 == "XBT" and user_choice2 == "BRL":
        # - redirect - #
        conversion.xbt_to_brl() 
    ### - elif statement - Bitcoin XBT --> USD - ###
    elif user_choice1 == "XBT" and user_choice2 == "USD": 
        # - redirect - #
        conversion.xbt_to_usd() 
    ### - elif statement - Bitcoin XBT --> EUR - ###
    elif user_choice1 == "XBT" and user_choice2 == "EUR":
        # - redirect - #
        conversion.xbt_to_eur() 
    ### - elif statement - Bitcoin XBT --> GBP - ###
    elif user_choice1 == "XBT" and user_choice2 == "GBP":
        # - redirect - #
        conversion.xbt_to_gbp() 
    ### - elif statement - Bitcoin XBT --> INR - ###
    elif user_choice1 == "XBT" and user_choice2 == "INR":
        # - redirect - #
        conversion.xbt_to_inr() 
    ### - elif statement - Bitcoin XBT --> JPY - ###
    elif user_choice1 == "XBT" and user_choice2 == "JPY":
        # - redirect - #
        conversion.xbt_to_jpy() 
    ### - elif statement - Bitcoin XBT --> CHF - ###
    elif user_choice1 == "XBT" and user_choice2 == "CHF":
        # - redirect - #
        conversion.xbt_to_chf() 
    ### - elif statement - Bitcoin XBT --> CAD - ###
    elif user_choice1 == "XBT" and user_choice2 == "CAD":
        # - redirect - #
        conversion.xbt_to_cad() 
    ### - elif statement - Bitcoin XBT --> ETH - ###
    elif user_choice1 == "XBT" and user_choice2 == "ETH":
        # - redirect - #
        conversion.xbt_to_eth() 

    #### - Special Status Codes - ####
    ### - Exit Code Convert and Exit Code To - ###  
    elif user_choice1 in ["Exit", "exit"] and user_choice2 in ["Exit", "exit"]: 
        sys.exit(1)
    ### - If the user inputs the special status code wrong or ISO code input is invalid - ###
    else: 
        print("Sorry, try again!")
        currency_matcher()