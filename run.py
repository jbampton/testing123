import json
import re
import urllib.request
from datetime import datetime


p = re.compile(r"(<!-- lichess -->)(.*?)(<!-- lichess -->)", re.MULTILINE | re.DOTALL)
with urllib.request.urlopen('https://lichess.org/api/user/SexyMate/perf/blitz') as url:
    data = json.load(url)
    results = ''
    for row in data['stat']['bestWins']['results']:
        title = row['opId']['title']
        if title == None:
            title = ''
        else:
            title += ' '
        name = row['opId']['name']
        rating = row['opRating']
        date = row['at']
        results += f'- {title}{name} ({rating}) {date}\n'
    with open("README.md", 'r') as my_file:
        readme = my_file.read()
        readme = re.sub(p, r"\1\n"+results+r"\3", readme)
    with open("README.md", 'w') as my_file:
        my_file.write(readme)
