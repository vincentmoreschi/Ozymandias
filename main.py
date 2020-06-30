import places_handler

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html', time=places_handler.test())


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App

    app.run(host='127.0.0.1', port=8080, debug=True)
