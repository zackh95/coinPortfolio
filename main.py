import tkinter as tk
from coinmarketcap import Market
import pandas as pd

class Portfolio:

    def calculate(self, filename):
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
            label = tk.Label(self.topFrame,text=symbol + ':  $'+str(value))
            label.pack()
            self.labels.append(label)
            total += value

        print "================================"
        print "Total = " + str(total)
        label = tk.Label(self.topFrame,text="==================")
        label.pack()
        self.labels.append(label)
        label = tk.Label(self.topFrame,text="Total:  $"+str(total))
        label.pack()
        self.labels.append(label)

    def callback(self):
        for x in self.labels:
            x.destroy()
        from tkFileDialog import askopenfilename
        self.filename = askopenfilename(filetypes=(("CSV",'*.csv'),("All Files","*.*")))
        self.calculate(self.filename)

    def refresh(self):
        for x in self.labels:
            x.destroy()
        self.calculate(self.filename)

    def __init__(self):
        self.filename = ""
        self.root = tk.Tk()
        self.topFrame = tk.Frame(self.root)
        self.topFrame.pack()
        self.botFrame = tk.Frame(self.root)
        self.botFrame.pack(side="bottom")
        self.labels = []
        button = tk.Button(self.botFrame,text="Load CSV", command = self.callback)
        button.pack()
        button2 = tk.Button(self.botFrame,text="Refresh", command = self.refresh)
        button2.pack(side="right")
        self.root.mainloop()

Portfolio()
