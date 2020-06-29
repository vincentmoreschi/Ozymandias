import googlemaps
import places_handler
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')


def root():
    places  = places_handler.test()
    return app.render_template('index.html', place = places)

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)
