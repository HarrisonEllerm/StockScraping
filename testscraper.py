from scraper import get_stats

search_terms = ["Valuation measures", "Fiscal year", "Profitability", "Management effectiveness", "Income statement",
                "Balance sheet", "Cash flow statement", "Stock price history", "Share statistics", "Dividends & splits"]

result = get_stats('https://nz.finance.yahoo.com/quote/FBU.NZ/key-statistics?p=FBU.NZ', search_terms)

for item in result:
    print 'key: ' + item[0] + ', value: ' + item[1]





