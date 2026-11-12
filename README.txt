Intro:
Hello! This program gives you a list of all dragon type pokemon with names logner then 9 characters, it also shows you how many characters the name has.


About:
The program is split into 6 main files. The first file is this README, if you opened this first, good job!

The second file is the main.py file in the source map. This file contains the code that runs the script, after running the code yo will get the result as specified in the intro.
The main.py file consists of 7 parts, the logging settings, which sets up the logs for the script, the data_get function, which gets you the data and turns it into an usable list
The filter_name_length function, which filters out all the names with 9 characters or less, the name_length function, which gets the length of the names and turns the data in a dictionary
the csv_writer and json_writer, which write the data to the respective files.
And finaly the main function which executes all the code

The second, third and fourth file of the program are the logfiles, the results.csv and the results.json

The final file is the test_main.py file. This file checks in the first 3 functions output the right data.


Instalation:
To install run this program you need to do the following:
1. Download python
2. Make sure you have the following libraries installed: requests, logging, json, csv and pytest
3. Make sure the files are somewhere on your computer where your shell can acces it
4. Run the following command in the shell: python <directory>


Expectation:
The end result should be a log file that either displays an error if something went wrong, or the time the script was executed.
In addition to this there should be a CSV and JSON file with the results if everything went right


Issues:
There are 2 main issues, the first is that the tests in pytest will fail once new pokemon get added to the API, this only happens once every ~5 years,
so you should be able to update the tests whenever that happens

The second main issue is that the PYTHONPATH for the pytests was not configured correctly, thus I had to manually append the path to PYTHONPATH, this contains information
that will not be published in the GITHUB, so you would have to configure this yourself if this also is a issue for you