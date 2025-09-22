from flask import Blueprint, render_template, redirect, url_for, session
from app.forms import UserInfoForm

main=Blueprint('main',__name__)

@main.route('/',methods=['GET','POST'])
def home():
    form=UserInfoForm()
    if form.validate_on_submit():
        session['user']={
            'name':form.name.data,
            'age':form.age.data,
            'gender':form.gender.data,
            'height':form.height.data,
            'weight':form.weight.data,
            'activity_level':form.activity_level.data
        }
        return redirect(url_for('main.recommendation'))
    return render_template('index.html',form=form)

@main.route('/recommendation')
def recommendation():
    user=session.get('user')
    if not user:
        return redirect(url_for('main.home'))
    weight=user['weight']
    water_needed=round(weight*35)  # ml/day
    return render_template('recommendation.html',user=user,water_needed=water_needed)
