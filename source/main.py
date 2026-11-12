# These are the libraries needed for the code
import requests
import logging
import json
import csv

# This is the logging configuration
logging.basicConfig(
    level=logging.INFO,
    filename="logfile.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# This logs when the file was last written
logging.info("File written")


# This function requests the data from the API (https://pokeapi.co/api/v2/type/16), The data we request are all pokemon with the Dragon typing, the function returns only the names of the pokemon.
def data_get(timeout=10):
    try:  # This try and except block gets the data from the API and turns it into JSON data, it also checks for any possible error
        data = requests.get(url="https://pokeapi.co/api/v2/type/16", timeout=timeout)
        data_json = data.json()
        data.raise_for_status()
    except requests.exceptions.Timeout:
        logging.error("requests.exceptions.Timeout", exc_info=True)
        raise
    except requests.exceptions.ConnectionError:
        logging.error("requests.exceptions.ConnectionError", exc_info=True)
        raise
    except requests.exceptions.HTTPError:
        logging.error("requests.exceptions.HTTPError", exc_info=True)
        raise
    except requests.exceptions.JSONDecodeError:
        logging.error("requests.exceptions.JSONDecodeError", exc_info=True)
        raise
    except requests.exceptions.RequestException:
        logging.error("requests.exception.RequestException", exc_info=True)
        raise

    # The code bellow filters away all the unnecessary info so we only keep the names of the pokemon.
    pokemon_list = data_json["pokemon"]

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
    name_and_length = []
    for i in filtered_list:
        name = i
        length = len(name)
        name_and_length.append({"Name": name, "Length": length})

    return name_and_length


# This function writes the data to a CSV file
def csv_writer(name_and_length):
    fieldnames = ["Name", "Length"]

    with open("results.csv", "w", newline="", encoding="UTF-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(name_and_length)


# This function writes the data to a JSON file
def json_writer(name_and_length):
    writer = json.dumps(name_and_length, indent=4)
    with open("results.json", "w") as jsonfile:
        jsonfile.write(writer)


# This is the main function that executes the entire program
def main():
    pokemon_name_list = data_get()
    filtered_list = filter_name_length(pokemon_name_list)
    name_and_length = name_length(filtered_list)
    csv_writer(name_and_length)
    json_writer(name_and_length)


# Executing main() executes the entire program
main()
