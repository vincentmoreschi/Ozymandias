from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from . forms import SearchForm
from . import places_handler

from .. models import MapData

query = ''


@main.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.location.data
        form.location.data = ''
        session['query'] = query
        session['place'] = places_handler.get_place_location(query)
        return redirect(url_for('.map'))
    return render_template('index.html', form=form)


@main.route('/map',  methods=['GET', 'POST'])
def map():
    print(session.get('place'))
    return render_template('map.html',image_file = session.get('place'),query = session.get('query'))
