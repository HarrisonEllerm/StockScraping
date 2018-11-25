from scraper import get_stats
from scraper import get_summary

stats_search_terms = ["Valuation measures",
                "Fiscal year",
                "Profitability",
                "Management effectiveness",
                "Income statement",
                "Balance sheet",
                "Cash flow statement",
                "Stock price history",
                "Share statistics",
                "Dividends & splits"]

while True:

    symbol = raw_input("Please enter ticker symbol and option, or help to find out more information.\n")

    if symbol.upper().__contains__("QUIT"):
        break

    elif symbol.upper().__contains__("HELP"):
        print("Possible options:")
        print(" -sum, usage: [FBU.NZ --sum], finds summary information associated with the ticker.")
        print(" -stats, usage: [FBU.NZ --stats], finds statistics associated with the ticker.")
        print(" help, usage: [help], prints this menu.")
        print(" quit, usage: [quit], quits the program.\n")

    # handle the summary report case
    elif "sum" in symbol:
        try:

            summary_items = get_summary('https://nz.finance.yahoo.com/quote/' + symbol.upper().replace(' -SUM', '') +
                                        '?p=' + symbol.upper().replace(' -SUM', ''))
            print "****** SUMMARY INFO ******"
            for item in summary_items:
                print item[0] + ' = ' + item[1]
            print("**************************\n")

        except Exception as error:
            print error

    # handle the statistics case
    elif "stats" in symbol:
        try:

            stats = get_stats('https://nz.finance.yahoo.com/quote/' + symbol.upper().replace(' -STATS', '') +
                              '/key-statistics?p=' + symbol.upper().replace(' -STATS', ''), stats_search_terms)
            print "******  STATISTICS  ******"
            for item in stats:
                print item[0] + ' = ' + item[1]
            print("**************************\n")

        except Exception as error:
            print error

    else:
        print("Command unknown, use 'help' to display a list of possible commands.\n")
