from flask import Flask, render_template, request, redirect
import pandas as pd
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

filepath = '/Users/samsoik/Documents/TDI/12-day-program/day-10/\
price-volume-data-for-all-us-stocks-etfs/Data/Stocks/'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tickerinfo.html')

@app.route('/plotStocks', methods = ['POST'])
def plotStocks():
    ticker = request.form['ticker']
    month = request.form['month']
    start = pd.to_datetime('2016-' + month + '-01')
    if month == '12':
        stop = pd.to_datetime('2017-01-01')
    else:
        stop = pd.to_datetime('2016-' + str(int(month) + 1) + '-01')

    stocks = pd.read_csv(filepath + ticker.lower() + '.us.txt', usecols = ['Date', 'Close'])
    return str(stocks['Close'][0])
    """
    stocks['Date'] = pd.to_datetime(stocks['Date'])
    stocks = stocks[stocks['Date'] >= start]
    stocks = stocks[stocks['Date'] < stop]
#    return ', '.join([str(x) for x in stocks['Close']])
    
    p = figure(title = 'Kaggle Huge Stock Market Dataset (2016)', x_axis_type = 'datetime', x_axis_label = 'Date',
               y_axis_label = 'Price (USD)')
    p.line(stocks['Date'], stocks['Close'], legend_label = ticker.upper() + ': Close')
    p.legend.location = 'top_left'

    html = file_html(p, CDN, 'plotStocks')
    f = open('templates/plot.html', 'w')
    f.write(html)
    f.close()
    return render_template('plot.html')
    """
if __name__ == '__main__':
  app.run(port=33507)
