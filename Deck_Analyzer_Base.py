from argparse import ArgumentError

import requests
import json
import csv

# Calls API using HTTP request - Evan
def get_card_data(query):
    url = f"https://api.scryfall.com/cards/search?q={query}"
    response = requests.get(url)
# Error handling if the status of the request equals 200 - Evan
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

#This will print card names - Evan
def print_card_name(data):
    if data and 'data' in data:
        for card in data['data']:
            print(card['name'])


# Maki
# Input: Data recieved from API call.
# Behavior: Asks user to select a card.
# Returns: Selected card
def select_card_from_data(data):
    user_choice = 0
    if data and 'data' in data:
        data_count = len(data['data'])
        current_card = 0
        for card in data['data']:
            print(f"[{current_card}] {card['name']}")
            current_card += 1
        user_choice = int(input("Select a number.\n"))
        if user_choice < 0 or user_choice > len(data):
            raise ArgumentError("Invalid user choice!")
    else:
        raise ArgumentError("Invalid data passed to select_card_from_data!")
    return data['data'][user_choice]



#This will define the query type for card
def select_query_type(argument):
    switcher = {
        1: "Name",
        2: "Keywords",
        3: "Colors",
        4: "Multi-Request: Multiple fields"
    }
    return switcher.get(argument, "nothing")

if __name__ == "__main__":
    # argument = input("How would you like to search for your card?")
    # print (select_query_type(argument))

    search_query = "name:Tiamat"
    card_data = get_card_data(search_query)
    selected_card = select_card_from_data(card_data)

    print(f"Selected card mana cost: {selected_card['mana_cost']}")
    print(f"Selected card name: {selected_card['name']}")
    print(f"Selected card CMC: {selected_card['cmc']}")
    print(f"Selected card Orcle Text: {selected_card['oracle_text']}")



# def card_query(user_query):


# My dick is small




# if card_data and 'data' in card_data:
#     first_card = card_data['data'][0]
#     print(f"First card name: {first_card['name']}")
#     print(f"First card mana cost: {first_card['mana_cost']}")
#     print(f"First card CMC: {first_card['cmc']}")
#     print(f"First card Orcle Text: {first_card['oracle_text']}")