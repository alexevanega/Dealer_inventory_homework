from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,validators
from wtforms.validators import DataRequired

class addToInventory(FlaskForm):
    image = StringField('Image URL', validators=[DataRequired()])
    vin_num = StringField('Vin Number', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField()

