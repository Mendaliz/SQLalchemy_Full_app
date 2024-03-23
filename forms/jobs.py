from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):

    team_leader = StringField('Team Leader', validators=[DataRequired()])
    job = StringField('Job', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    end_date = DateField('End Date', format='%m/%d/%Y')
    is_finished = BooleanField("Is finished")
    submit = SubmitField('Submit')
