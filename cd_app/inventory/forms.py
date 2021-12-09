from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired

class addToInventory():
    image = StringField('Image URL', validators=[DataRequired()])
    vin_num = StringField('Vin Number', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField()