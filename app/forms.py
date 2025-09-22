from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class UserInfoForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    age=IntegerField('Age',validators=[DataRequired(),NumberRange(min=1,max=120)])
    gender=RadioField('Gender',choices=[('male','Male'),('female','Female')],validators=[DataRequired()])
    height=FloatField('Height (cm)',validators=[DataRequired()])
    weight=FloatField('Weight (kg)',validators=[DataRequired()])
    activity_level=RadioField('Activity Level',choices=[('low','Low'),('medium','Medium'),('high','High')],validators=[DataRequired()])
    submit=SubmitField('Calculate Water Need')
