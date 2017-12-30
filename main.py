
from coinmarketcap import Market
import pandas as pd



frame = pd.read_csv("../../Downloads/coins.csv", names=['Coin','Amount'])
m = Market()
print "Portfolio Worth"
print "================================"
total = 0
for n in range(len(frame['Coin'])):
    result = m.ticker(frame['Coin'][n],convert="USD")
    symbol = result[0]['symbol']
    value  = float(result[0]['price_usd'])*frame['Amount'][n]
    print symbol + ':   ' + str(value)
    total += value

print "================================"
print "Total = " + str(total)
