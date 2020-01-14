#!/usr/bin/python
from flask import Flask, request, abort
import pprint as pp

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    if request.method == 'POST':
        pp.pprint(request.json)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)