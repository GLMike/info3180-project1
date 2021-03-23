from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField,  DecimalField, SubmitField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', 
                                validators=[DataRequired()])

    numBed = StringField('Number of Bedrooms', 
                                validators=[DataRequired()])

    numBath = StringField('Number of Bathrooms', 
                                validators=[DataRequired()])
    
    location = StringField('Location', 
                                validators=[DataRequired()])
    
    price = StringField('Price', 
                                validators=[DataRequired()])

    pType = SelectField('Type', 
                                choices=[('house', 'House'), ('apartment', 'Apartment')])

    desc = TextAreaField('Description', 
                                validators=[DataRequired()])

    pic = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])

    submit = SubmitField("Add Property")