from flask import Flask, render_template
from gumball import reward_post, detect_content
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    _data_list = []
    for _url, _name, _score in reward_post():
        _content = detect_content(_url)
        _data_list.append({'url': _url, 'name': _name, 'score': _score, 'contains': _content.count('截图')})
    _s = json.dumps(_data_list, ensure_ascii=False)
    return render_template('./home.html', data=_s)


if __name__ == '__main__':
    app.run()
