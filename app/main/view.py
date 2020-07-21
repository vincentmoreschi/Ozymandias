from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from . forms import SearchForm
from .. import db
from . import places_handler

#from ..models import user

query = ''


@main.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        query = form.name.data
        print("yter")

        places_handler.get_place_location(query)
        return redirect(url_for('.map'))
    return render_template('index.html', form=form)


@main.route('/map')
def map():
    return render_template('map.html')
