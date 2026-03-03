import json
import sys

import requests

URL_ALL = "https://restcountries.com/v3.1/all?fields=name,capital,currencies"
URL_NAME = "https://restcountries.com/v3.1/name/"


def make_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
           return response.text
    except Exception as error:
        print("Error making request to: ", url)
        
    return None


def parse_json(answer_text):
    try:
        return json.loads(answer_text)
    except: 
        print('Error parsing JSON...') 


def count_countries():
    response = make_request(URL_ALL)

    if response:
        country_list = parse_json(response)

        if country_list:
            return len(country_list)


def list_countries(country_list):
    for country in country_list:
        print(country['name']['common'])


def show_population(country_name):
    response = make_request(URL_NAME + str(country_name))
    
    if response:
        country_list = json.loads(response)

        if country_list:
            for country in country_list:
                print(f"\n\t{country['name']['common']}: {country['population']} inhabitants\n\t")
        
    else:
        print('\n\t> Country not found!\n') 


def show_currencies(country_name):
    response = make_request(URL_NAME + country_name)
    
    if response:
        country_list = json.loads(response) 

        if country_list:
            for country in country_list:
                print('\n\tCurrencies of', country['name']['common'] + ':')

                currencies = country['currencies']

                # currencies.values() maps 'currency' to the object (e.g., inside "BRL") from "currencies", now we can access ['name'] of BRL (which is currently the 'currency' variable in the for loop)
                for currency in currencies.values():
                    print('\n\t', currency['name'], '\n\t')
                      
    else:
        print('\n\t> Country not found!\n') 


def get_country_name():
    try:
        arg2 = sys.argv[2]
        return arg2
    
    except:
        print('\n\t> You need to pass the country name!\n')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('\n\t>> Welcome to the country system <<')
        print('\n\tUsage: python countries.py <action> <country name>')
        print('\n\tAvailable actions: count, currency, population\n') 
    else:
        arg1 = sys.argv[1]

        if arg1 == 'count':
            print(f'\n\t> There are {count_countries()} countries in the world\n')
        
        elif arg1 == 'currency':
            country = get_country_name()

            if country:
                show_currencies(country)
            
        elif arg1 == 'population':
            country = get_country_name()

            if country: 
                show_population(country)
            
        else:
            print('\n\t>> Invalid argument\n')