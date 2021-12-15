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

class removeInventory(FlaskForm):
    id = StringField('Item ID', validators=[DataRequired()])
    submit = SubmitField()

class updateListingForm(FlaskForm):
    image= StringField('Image URL')
    vin_num= StringField('Vin Number')
    year = StringField('Year')
    make = StringField('Make')
    model = StringField('Model')
    description = StringField('Description')
    submit = SubmitField()