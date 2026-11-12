# These are the libraries needed for the code
import requests
import schedule
import time
import logging
import json
import csv
import datetime

# This is the logging configuration
logging.basicConfig(
    level=logging.INFO,
    filename="logfile.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Placeholder")


# This function requests the data from the API (https://pokeapi.co/api/v2/type/16), The data we request are all pokemon with the Dragon typing, the function returns only the names of the pokemon.
def data_get(timeout=10):
    data = requests.get(url="https://pokeapi.co/api/v2/type/16", timeout=timeout).json()
    pokemon_list = data["pokemon"]

    pokemon_name_list = []

    for i in pokemon_list:
        name = i["pokemon"]["name"]
        pokemon_name_list.append(name)

    return pokemon_name_list


# This functions filters the data so only pokemon with more then 8 letters in their name remain in the list
def filter_name_length(pokemon_name_list):
    filtered_list = []
    for i in pokemon_name_list:
        name = i
        if len(name) > 8:
            filtered_list.append(name)

    return filtered_list


# This function adds an extra datafield with the length of the name
def name_length(filtered_list):
    name_and_length = {"Name": [], "Length": []}
    for i in filtered_list:
        name = i
        name_and_length["Name"].append(name)
        name_and_length["Length"].append(len(name))

    return name_and_length


# This function writes the data to a CSV file
def csv_writer():
    print("Placeholder")


# This function writes the data to a JSON file
def json_writer():
    print("Placeholder")


# This is the main function that executes the entire program
def main():
    print("Placeholder")


pokemon_name_list = data_get()
filtered_list = filter_name_length(pokemon_name_list)
name_and_length = name_length(filtered_list)
