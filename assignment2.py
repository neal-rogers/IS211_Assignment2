#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program retrieves a CSV from a URL, processes it, logs invalid lines to
a file, and prints corresponding data for ID numbers.
"""

import urllib2, csv, datetime


url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'

def downloadData(url):
    """
    Args:
        url (str): URL for fetching of data.

    Returns:
        data (): Contents of file.

    Example:
        >>> downloadData(url)
        >>>
    """
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()

# def processData(data):
#    """
#    Args:
#        url (str): URL for fetching of data.
#
#    Returns:
#        Contents of file.
#
#    Example:
#        >>> downloadData(url)
#        >>>
#    """
