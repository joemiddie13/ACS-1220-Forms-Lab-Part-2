from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be between 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')


class AuthorForm(FlaskForm):
    """Form to create an author."""
    name = StringField('Name', validators=[DataRequired()])
    biography = TextAreaField('Biography')
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[], render_kw={"placeholder": "YYYY-MM-DD"})
    country = StringField('Country')
    submit = SubmitField('Submit')


class GenreForm(FlaskForm):
    """Form to create a genre."""
    name = StringField('Genre Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    pass

class UserForm(FlaskForm):
    """Create new user form."""
    username = StringField('Username', validators=[DataRequired()])
    favorite_books = QuerySelectMultipleField('Favorite Books', query_factory=lambda: Book.query, get_label='title')
    submit = SubmitField('Submit')
