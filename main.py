from __future__ import print_function
from flask import Flask, render_template
import webbrowser
from thread import start_new_thread
from time import sleep
from copy import copy

PORT = 5000
DEBUG = True

app = Flask(
    __name__,
    static_folder='static'
)

BASIC_CONTEXT = {
    'DEBUG': DEBUG,
    'title': "Nice app",
    'livejs': True,
}


@app.route('/')
def index():
    '''Entry point'''
    data = {
        'DEBUG': DEBUG,
        'title': "Nice app"
    }
    return render_template('index.html', **data)


@app.route('/charts/')
def charts():
    data = copy(BASIC_CONTEXT)

    return render_template('charts.html', **data)

if __name__ == '__main__':
    def show():
        sleep(2)
        url = 'http://localhost:{port}/'.format(port=PORT)
        print("Opening browser at {url}".format(url=url))
        webbrowser.open_new(url)
    start_new_thread(show, tuple())
    app.run(
        debug=DEBUG,
        port=PORT,
    )
