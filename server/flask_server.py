from flask import Flask, render_template
from gumball import generate_list
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    _data_list = []
    for _url, _name, _score, _contains in generate_list():
        _data_list.append({'url': _url, 'name': _name, 'score': _score, 'contains': _contains})
    _s = json.dumps(_data_list, ensure_ascii=False)
    return render_template('./home.html', data=_s)


def run():
    app.run(host='0.0.0.0', port='8999')
