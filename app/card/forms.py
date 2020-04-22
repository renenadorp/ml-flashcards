from flask import url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length, DataRequired


from app.models import Card


class SearchForm(FlaskForm):
    """Search Form."""

    q = StringField("Search", validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(SearchForm, self).__init__(*args, **kwargs)
        self.search = None

    def validate(self):
        return True
