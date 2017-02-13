#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program retrieves a CSV from a URL, processes it, logs invalid lines to
a file, and prints corresponding data for ID numbers.
"""

import urllib2, csv, datetime, logging, argparse

log = 'error.log'
logging.basicConfig(filename=log, level=logging.ERROR)
logger1 = logging.getLogger('IS211_Assignment2')


def downloadData(url):
    """
    Args:
        url (str): URL for fetching of data.

    Returns:
        data (str): Contents of string from URL response data.

    Example:
        >> downloadData(url)
        >>
    """
    # Generates HTTP request for the passed 'url'; returns/stores HTTP response.
    response = urllib2.urlopen(url)
    # Sets 'data' to the contents of 'response'.
    data = response.read()
    return data


def processData(response_data):
    """
    Args:
        response_data (str): Contents of data from downloadData function.

    Returns:
        myresult_dict (dict): Dictionary file containing formatted records.

    Example:
        >> processData(csvdata)
        >>
    """
    # Creates dict 'myresult_dict'.
    myresult_dict = {}
    # Splits the string on each '\n' delimiter and stores each in 'response_list'.
    response_list = response_data.split("\n")
    # Open the 'log' file in read/write mode.
    f = open(log, 'rt')
    # For each line in 'response_list' within specified range...
    for rec_line in response_list[1:-1]:
        # Split each line on ',' delimiter
        rec = rec_line.split(",")
        try:
            # Add formatted and indexed values from 'rec' into the dictionary.
            myresult_dict[rec[0]] = (rec[1], datetime.datetime.strptime(rec[2], "%d/%m/%Y"))
        except (ValueError):
            # Write formatted error message to log file.
            msg = 'Error processing line {} for ID {}'.format(rec_line[0], rec[0])
            # Use custome logger and write the formatted custom error message.
            logger1.error(msg)
            pass
        else:
            pass

    return myresult_dict


def displayPerson(id, personData):
    """
    Args:
        id (str):
        personData (dict): Dictionary containing user data.

    Returns:
        record (str): Formatted and concatenated record values.

    Example:
        >> displayPerson(10, result)
        >> Person #10 is Una James with a birthday of 1981-09-05 00:00:00
    """
    # Prompt user for id number and store it.
    while id > 0:
        try:
            id = raw_input('Enter user id: ')
            pid = 'Person #{} '.format(id)
            name = 'is {} '.format(personData[id][0])
            bday = 'with a birthday of {}'.format(personData[id][1])
            record = pid + name + bday
            print record
        except:
            print 'No user found with that id'
            continue
        if id <= 0:
            print "Exiting program..."
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Enter the data url')
    args = parser.parse_args()
    if args.url:
        url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
        csvdata = downloadData(url)
        result = processData(csvdata)
        records = displayPerson(id, result)
    else:
        print 'error'