from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

"""
    Defines a set of functions used to
    scrape the Yahoo Finance Web Page for
    Stock information.
    
    Author: Harry Ellerm
"""


def get_page(url):
    """
    Accepts a single url argument and makes a GET
    request to that url.
    """
    try:
        # closing function makes sure that any network
        # resources are freed when they go out of scope
        # of the with block
        with closing(get(url, stream=True)) as resp:
            if is_good(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_exception('Error thrown when requesting to {0} : {1}'.format(url, str(e)))
        return None


def get_stats(url, search_terms):
    """
    Gets the statistics for a particular stock by parsing the
    corresponding Yahoo Finance web page.
    :param url: the url
    :param search_terms: the terms corresponding to the statistics
    the user is interested in, i.e. Valuation measures, Fiscal year,
    Profitability etc.
    :return: an array of key value pairs representing the stats found,
    or None if no stats could be found.
    """
    response = get_page(url)
    if response is not None:
        soup = BeautifulSoup(response, 'html.parser')
        stats = []
        for item in search_terms:
            table = get_table_corresponding_to_search_term(soup, item)
            table_data = table.findAll('tr')
            for row in table_data:
                cells = row.findAll('td')
                statistic = cells[0].find(text=True), cells[1].find(text=True)
                stats.append(statistic)

        if len(stats) != 0:
            return stats
        else:
            return None


def get_table_corresponding_to_search_term(soup, search_term):
    """
    Returns a table from within the HTML, specified by
    a search term.
    :param soup: the soup object
    :param search_term: the search term
    :return: a table corresponding to the search term
    if found, or None if no table is found.
    """
    # first parent steps out to span
    # second parent steps out of span to div
    str_val = soup.find(text=search_term).parent.parent
    table = str_val.findNext("table")

    if len(table) != 0:
        return table
    else:
        return None


def is_good(resp):
    """
    Defines if a request is valid by analysing the
    content-type header of the HTML, if any is returned.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_exception(e):
    """
    Logs an exception thrown during execution.
    """
    print(e)


