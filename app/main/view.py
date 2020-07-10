from datetime import datettime
from flask import render_template, sesssion, redirect, url_for
from . import main
from . form import NameForm
from .. import db
from ..models import user

@main.route('/',methods=['GET,'POST'])
def index():
    form = NAME()
