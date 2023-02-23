import argparse
from etf_analyzer.functions import extract_symphId

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', action='store', required=True, help='Specifies the URL to a symphony from which the user wishes the program to scrape and analyze its ETFs.')
    parser.add_argument('-o', '--outfile', dest='outfile', action='store', required=True, help='Specifies a file that the program will write the CSV output to.')
    parser.add_argument('-t', '--threading', dest='threading', action='store_true', required=False, help='Tells the program to utilize multi-threading in its execution.')
    args = parser.parse_args()

    composerConfig = {
                "projectId" : "leverheads-278521",
                "databaseName" : "(default)"
            }


    if args.threading:
        import threading
        pass
    else:
        pass

    return

if __file__ == "__main__":
    main()