#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program retrieves a CSV from a URL, processes it, logs invalid lines to
a file, and prints corresponding data for ID numbers.
"""

import urllib2, csv, datetime, logging


def downloadData(url):
    """
    Args:
        url (str): URL for fetching of data.

    Returns:
        data (): Contents of string.

    Example:
        >>> downloadData(url)
        >>>
    """
    response = urllib2.urlopen(url)
    data = response.read()
    return data

def processData(response_data):
    """
    Args:
        url (str): URL for fetching of data.

    Returns:
        Contents of file.

    Example:
        >>> downloadData(url)
        >>>
    """
    myresult_dict = {}
    response_list = response_data.split("\n")

    for rec_line in response_list:
        rec = rec_line.split(",")
        try:
            myresult_dict[rec[0]] = (rec[1], datetime.datetime.strptime(rec[2], "%d/%m/%Y"))
        except (ValueError, IndexError):
            print ("Whoops")
                                     
    return myresult_dict

if __name__ == "__main__":
    url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"

    birthdays_csv = downloadData(url)

    results = processData(birthdays_csv)

    print results
