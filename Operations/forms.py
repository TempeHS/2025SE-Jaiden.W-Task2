from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FloatField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Regexp, NumberRange

class MovieForm(FlaskForm):
    budget = FloatField(
        "Budget (in millions)",
        validators=[
            DataRequired(),
            NumberRange(min=0, message="Budget must be a positive number"),
        ],
        render_kw={"type": "number", "step": "any"},  # Allow decimal values
    )
    release_date = StringField(
        "Release Date (YYYY-MM-DD)",
        validators=[
            DataRequired(),
            Regexp(
                r"^\d{4}-\d{2}-\d{2}$",
                message="Date must be in the format YYYY-MM-DD",
            ),
        ],
    )
    rating = SelectField(
        "Rating",
        choices=[
            ("R", "R"),
            ("PG", "PG"),
            ("G", "G"),
            ("Not Rated", "Not Rated"),
            ("NC-17", "NC-17"),
            ("Approved", "Approved"),
            ("TV-PG", "TV-PG"),
            ("PG-13", "PG-13"),
            ("Unrated", "Unrated"),
            ("X", "X"),
            ("TV-MA", "TV-MA"),
            ("TV-14", "TV-14"),
        ],
        validators=[DataRequired()],
    )
    is_sequel = BooleanField("Is it a Sequel?")
    runtime = IntegerField("Runtime (in minutes)", validators=[DataRequired()])
    genre = SelectField(
        "Genre",
        choices=[
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Animation", "Animation"),
            ("Biography", "Biography"),
            ("Comedy", "Comedy"),
            ("Crime", "Crime"),
            ("Drama", "Drama"),
            ("Family", "Family"),
            ("Fantasy", "Fantasy"),
            ("Horror", "Horror"),
            ("Music", "Music"),
            ("Musical", "Musical"),
            ("Mystery", "Mystery"),
            ("Romance", "Romance"),
            ("Sci-Fi", "Sci-Fi"),
            ("Sport", "Sport"),
            ("Thriller", "Thriller"),
            ("Western", "Western"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")

    @property
    def is_sequel_data(self):
        """Return 1 if True, otherwise 0."""
        return 1 if self.is_sequel.data else 0