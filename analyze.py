import argparse
import requests
from requests_html import HTMLSession
import json
import csv
from etf_analyzer.functions import extract_symphId, gather_etfs, etf_data_iterator
from etf_analyzer.css_selectors import CSS_SELECTORS

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', action='store', required=True, help='Specifies the URL to a symphony from which the user wishes the program to scrape and analyze its ETFs.')
    parser.add_argument('-o', '--outfile', dest='outfile', action='store', required=True, help='Specifies a file that the program will write the CSV output to.')
    #parser.add_argument('-t', '--threading', dest='threading', action='store_true', required=False, help='Tells the program to utilize mulitithreading.')
    args = parser.parse_args()

    composerConfig = {
                "projectId" : "leverheads-278521",
                "databaseName" : "(default)"
            }

    print('Collecting ETFs used in the symphony...')
    symphId = extract_symphId(args.url)
    symphReq= requests.get(f'https://firestore.googleapis.com/v1/projects/{composerConfig["projectId"]}/databases/{composerConfig["databaseName"]}/documents/symphony/{symphId}')
    response = json.loads(symphReq.text)
    etfs = gather_etfs(response['fields']['latest_version_edn']['stringValue'])
    
    # Initialize list for storing ETF Data
    etf_data = list()

    session = HTMLSession()

    print('Scraping ETF data...')
    
    for etf in etfs:
        # Initialize dictionary for ETF data scraped from Composer
        data_dict = dict()
        
        data_dict['ETF'] = etf
        s = session.get(f'https://composer.trade/etf/{etf}/')
        s.html.render()
        for k, v in CSS_SELECTORS.items():
            if not type(v) == list:
                data_dict[k] = s.html.find(v, first=True).text
            else:
                try:
                    data_dict[k] = s.html.find(v[0], first=True).text + f' ({s.html.find(v[-1], first=True).text})'
                except AttributeError:
                    pass
        etf_data.append(data_dict)

    print('Writing ETF data to file...')
    with open(args.outfile, 'w') as csvfile:
        headers = ['ETF'] + list(CSS_SELECTORS.keys())
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(etf_data)

    print('Finished!')
    return
if __name__ == "__main__":
    main()