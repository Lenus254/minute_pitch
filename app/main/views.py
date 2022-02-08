# from .import main

# @main.route('/')
# def index():
   
#     return "Flask"

from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment, User, Pitch
from .forms import PitchForm ,CommentForm,UpdateProfile
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
    products = Pitch.query.filter_by(category = 'products').all()
    economy= Pitch.query.filter_by(category = 'economy').all()
    business= Pitch.query.filter_by(category = 'business').all()
    personal = Pitch.query.filter_by(category = 'personal').all()

    return render_template('index.html',title = title, pitches = pitches, products= products, economy=economy, business=business, personal=personal  )


@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    pform = PitchForm()
    if pform.validate_on_submit():
        title = pform.title.data
        post = pform.post.data
        category = pform.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('create_pitch.html', form = pform)

#comments view function

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)
