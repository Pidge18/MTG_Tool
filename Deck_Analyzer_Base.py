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
        raise RuntimeError(f"API Error: {response.status_code}")

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
            print(f"[{current_card + 1}] {card['name']}")
            current_card += 1
        user_choice = int(input("Select a number.\n")) - 1
        if user_choice < 0 or user_choice > len(data):
            raise ArgumentError("Invalid user choice!")
    else:
        raise ArgumentError("Invalid data passed to select_card_from_data!")
    return data['data'][user_choice]


#Evan's notes: Prof please correct me if I am wrong =>
# This class defines an argument with user input
# Argument is used as defining items for the query like 'name','keywords','colors' or a multi-request
class ScryfallQuery:
    def __init__(self, argument, user_input):
        self.argument = argument
        self.user_input = user_input
    def get(self):
        return f"{self.argument}:{self.user_input}"

def get_query_from_user() -> ScryfallQuery:
    return ScryfallQuery("bla","bla")


class InputableArgument:
    def input(self):
        raise NotImplementedError("Calling function on abstract base!")
    def get_query(self):
        raise NotImplementedError("Calling function on abstract base!")

class StringArgument(InputableArgument):
    arg_name = ""
    value = ""
    def __init__(self, argument_name: str):
        self.arg_name = argument_name
        value = ""
    def input(self):
        self.value = input(f"Provide value for {self.arg_name}: ")
    def get_query(self):
        return ScryfallQuery(argument=self.arg_name,user_input=self.value)






#This will define the query type for card
def select_query_type(argument):
    switcher = {
        1: "Name", # -> name
        2: "Keywords", # -> keywords
        3: "Colors", # -> colors: R(ed),W(hite),G(reen),B(lack),(Bl)U(e)
        4: "Multi-Request: Multiple fields" # -> selecting multiples -> EX: name,keywords
    }
    return switcher.get(argument, "nothing")

if __name__ == "__main__":
    # argument = input("How would you like to search for your card?")
    # print (select_query_type(argument))

    base_argument = InputableArgument()

    base_argument = StringArgument("name")
    base_argument.input()

    search_query = base_argument.get_query().get()
    card_data = get_card_data(search_query)
    selected_card = select_card_from_data(card_data)

    print(f"Selected card mana cost: {selected_card['mana_cost']}")
    print(f"Selected card name: {selected_card['name']}")
    print(f"Selected card CMC: {selected_card['cmc']}")
    print(f"Selected card Orcle Text: {selected_card['oracle_text']}")



# def card_query(user_query):







# if card_data and 'data' in card_data:
#     first_card = card_data['data'][0]
#     print(f"First card name: {first_card['name']}")
#     print(f"First card mana cost: {first_card['mana_cost']}")
#     print(f"First card CMC: {first_card['cmc']}")
#     print(f"First card Orcle Text: {first_card['oracle_text']}")