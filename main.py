import tkinter as tk
from coinmarketcap import Market
import pandas as pd

root = tk.Tk()
topFrame = tk.Frame(root)
topFrame.pack()
botFrame = tk.Frame(root)
botFrame.pack(side="bottom")

def calculate(filename):
    frame = pd.read_csv(filename, names=['Coin','Amount'])
    m = Market()
    print "Portfolio Worth"
    print "================================"
    total = 0
    for n in range(len(frame['Coin'])):
        result = m.ticker(frame['Coin'][n],convert="USD")
        symbol = result[0]['symbol']
        value  = float(result[0]['price_usd'])*frame['Amount'][n]
        print symbol + ':   ' + str(value)
        label = tk.Label(topFrame,text=symbol + ':  $'+str(value))
        label.pack()
        total += value

    print "================================"
    print "Total = " + str(total)
    label = tk.Label(topFrame,text="==================")
    label.pack()
    label = tk.Label(topFrame,text="Total:  $"+str(total))
    label.pack()

def callback():
    from tkFileDialog import askopenfilename
    filename = askopenfilename(filetypes=(("CSV",'*.csv'),("All Files","*.*")))
    calculate(filename)
    
button = tk.Button(botFrame,text="Load CSV", command = callback)
button.pack()
root.mainloop()
