'''
Contains functions used to execute the program effectively.
'''
import re
from .exceptions import InvalidSymphonyUrl

def extract_symphId(url: str) -> str:
    '''
    Function returns the twenty character alphanumeric
    string representing the unique ID of the provided symphony `url`.

    :param url: URL of the symphony provided by the user.
    '''
    regex = '\/symphony\/([^\/]+)'
    match = re.search(regex, url)
    if not match:
        raise InvalidSymphonyUrl('{url} does not have a valid symphony url structure.'.format(url=url))
    return match.groups(1)[0]

def gather_etfs(text: str) -> set:
    '''
    Parses the provided param `text` for ETFs and returns them as an
    iterable object. The return type is a set to ensure no duplicate ETFs
    are returned in the iterable.
    '''
    etfs = set()
    regex = '(?<=:ticker \\")[A-Z]+'
    etfs.update(set(re.findall(regex, text)))
    regex = '(?<=:lhs-val \\")[A-Z]+'
    etfs.update(set(re.findall(regex, text)))
    return etfs

def gather_etf_data(etf: str) -> dict:
    return




