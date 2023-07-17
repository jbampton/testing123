import json
import re
import urllib.request
from datetime import datetime

p = re.compile(r"(<!-- lichess -->)(.*?)(<!-- lichess -->)", re.MULTILINE | re.DOTALL)
with urllib.request.urlopen('https://lichess.org/api/user/SexyMate/perf/blitz') as url:
    data = json.load(url)
    results = ''
    for win in data['stat']['bestWins']['results']:
        #print(win)
        title = win['opId']['title']
        if title == None:
            title = ''
        else:
            title += ' '
        name = win['opId']['name']
        rating = win['opRating']
        date = win['at']
        # print(f'{title}{name} ({rating}) {date}')
        result = f'- {title}{name} ({rating}) {date}'
        results += result + "\n"
    with open("README.md", 'r') as my_file:
        readme = my_file.read()
        new_readme = re.sub(p, r"\1\n"+results+r"\3", readme)
        #print(new_readme)
    with open("README.md", 'w') as my_file:
        my_file.write(new_readme)
