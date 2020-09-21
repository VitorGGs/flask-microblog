from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User


class EditProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
	submit = SubmitField('Submit')

	def __init__(self, originial_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.originial_username = originial_username

	def validate_username(self, username):
		if username.data != self.originial_username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Please use a different username.')


class EmptyForm(FlaskForm):
	submit = SubmitField('Submit')


class PostForm(FlaskForm):
	post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
	submit = SubmitField('Submit')
