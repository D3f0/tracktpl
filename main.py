from __future__ import print_function
from flask import Flask, render_template
import webbrowser
from thread import start_new_thread
from time import sleep


PORT = 5000

app = Flask(__name__)


@app.route('/')
def index():
    '''Entry point'''
    data = {}
    return render_template('base.html', **data)

if __name__ == '__main__':
    def show():
        sleep(2)
        url = 'http://localhost:{port}/'.format(port=PORT)
        print("Opening browser at {url}".format(url=url))
        webbrowser.open_new(url)
    start_new_thread(show, tuple())
    app.run(debug=True, port=PORT)
