# RegEx
import re
# Requests
import requests

r = requests.get('https://public-interactive-chart.vercel.app/static/js/main.7f302d46.chunk.js')
data = r.text

url_val = [i.start() for i in re.finditer('url:', data)]

output = []

for item in url_val:
	# Make a list of all url instances
    _out = (''.join(data[item:item+data[item:].index(',')].split('url:')[1].split('/')[0:3]))
    if _out not in output:
        output.append(_out)

for item in list(set(output)):
    print(item)

