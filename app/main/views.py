# from .import main

# @main.route('/')
# def index():
   
#     return "Flask"

from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment, User, Pitch
from .forms import PitchForm #,CommentForm,UpdateProfile
from flask_login import login_required, current_user
from .. import db,photos


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Created pitches'
    pitches = Pitch.query.all()
    items = Pitch.query.filter_by(category = 'items').all()
    economy= Pitch.query.filter_by(category = 'economy').all()
    business= Pitch.query.filter_by(category = 'business').all()
    personal = Pitch.query.filter_by(category = 'personal').all()

    return render_template('index.html',title = title, pitches = pitches, items= items, economy=economy, business=business, personal=personal  )
