'''
Contains functions used to execute the program effectively.
'''

import requests
import re
from .exceptions import InvalidSymphonyUrl

def extract_symphId(url: str) -> str:
    '''
    Function returns the twenty character alphanumeric
    string representing the unique ID of the provided symphony.

    :param url: URL of the symphony provided by the user.
    '''
    regex = '\/symphony\/([^\/]+)'
    match = re.search(regex, url)
    if not match:
        raise InvalidSymphonyUrl('{url} does not have a valid symphony url structure.'.format(url=url))
    return match.groups(1)[0]
