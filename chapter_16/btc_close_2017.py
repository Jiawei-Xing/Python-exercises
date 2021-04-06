from __future__ import (absolute_import, division, print_function, 
                                                unicode_literals)
                                                
# ~ try:
    # ~ from urllib2 import urlopen
# ~ except ImportError:
    # ~ from urllib.request import urlopen
# ~ import json

# ~ json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# ~ response = urlopen(json_url)
# ~ req = response.read()
# ~ with open('btc_close_2017_urllib,json', 'wb') as f:
    # ~ f.write(req)
# ~ file_urllib = json.loads(req)
# ~ print(file_urllib)

# ~ import requests

# ~ json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# ~ req = requests.get(json_url)
# ~ with open('btc_close_2017_request.json', 'w') as f:
    # ~ f.write(req.text)
# ~ file_requests = req.json()

# ~ print(file_urllib == file_requests)

import json

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
# ~ for btc_dict in btc_data:
    # ~ date = btc_dict['date']
    # ~ month = int(btc_dict['month'])
    # ~ week = int(btc_dict['week'])
    # ~ weekday = btc_dict['weekday']
    # ~ close = int(float(btc_dict['close']))
    # ~ print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    
import pygal
import math

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = 'close/$'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('close', close_log)
line_chart.render_to_file('close log line chart.svg')

from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart
    
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], 
        'Close average per month', 'average per month')
line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], 
        'close average per week', 'average per week')
line_chart_week

idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
    'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1: idx_week], 
    'close weekly average', 'weekly average')
line_chart_weekday.x_labels = ['M','T', 'W', 'R', 'F', 'S', 'U']
line_chart_weekday.render_to_file('close weekly average.svg')

with open('close dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('<html><head><title>close dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
        'close line chart.svg', 'close log line chart.svg', 'close average per month.svg',
        'close average per week.svg', 'close weekly average.svg'
    ]:
        html_file.write('   <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')
