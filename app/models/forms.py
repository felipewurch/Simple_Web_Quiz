from wtforms import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    email = StringField("email",validators=[DataRequired()])
    name = StringField("name",validators=[DataRequired()])
