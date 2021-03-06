from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import input_required


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[input_required()])
    category = SelectField('Category', choices=[('products','products'),('economy','economy'),('business','bisiness'),('personal','personal')],validators=[input_required()])
    post = TextAreaField('Your Pitch', validators=[input_required()])
    submit = SubmitField('Pitch')
    
class CommentForm(FlaskForm):

    comment = TextAreaField('Your Comments...',validators=[input_required()])
    submit = SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Give us your profile info.',validators = [input_required()])
    submit = SubmitField('Update')