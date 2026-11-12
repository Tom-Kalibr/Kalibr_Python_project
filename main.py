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


# This function requests the data from the API (https://pokeapi.co/api/v2/type/16), The data we request are all pokemon with the Dragon typing
def data_get():
    print("Placeholder")


# This functions filters the data so only pokemon with more then 8 letters in their name remain in the list
def filter_name_length():
    print("Placeholder")


# This function adds an extra datafield with the length of the name
def name_length():
    print("Placeholder")


# This function writes the data to a CSV file
def csv_writer():
    print("Placeholder")


# This function writes the data to a JSON file
def json_writer():
    print("Placeholder")


# This is the main function that executes the entire program
def main():
    print("Placeholder")
