from flask import Flask, render_template
from gumball import generate_list
import json
import time

app = Flask(__name__)

cacheData = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    now = int(time.time())
    timestamp = cacheData.get('timestamp', None)
    expired = False
    s = ''
    if not timestamp or now - timestamp > 3600:
        expired = True
    else:
        cached = cacheData.get('data', None)
        if cached:
            s = json.dumps(cached, ensure_ascii=False)
        else:
            expired = True
    if expired:
        data_list = []
        for url, name, score, contains in generate_list():
            data_list.append({'url': url, 'name': name, 'score': score, 'contains': contains})
        cacheData['data'] = data_list
        cacheData['timestamp'] = now
        s = json.dumps(data_list, ensure_ascii=False)

    return render_template('./home.html', data=s)


def run():
    app.run(host='0.0.0.0', port='8999')
