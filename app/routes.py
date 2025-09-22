from flask import Blueprint, render_template, redirect, request, url_for, session
from datetime import date
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

@main.route('/track', methods=['GET', 'POST'])
def track():
    user=session.get('user')
    if not user:
        return redirect(url_for('main.home'))

    # Step 1: Get today
    today=str(date.today())

    # Step 2: Get log dict from session
    logs=session.get('logs',{})

    # Step 3: If today's not in logs, initialize it
    if today not in logs:
        logs[today]=0

    # Step 4: Handle water intake POST
    if request.method=='POST':
        try:
            water=int(request.form.get('water',0))
            logs[today]+=water
            session['logs']=logs  # Save back to session
        except:
            pass

    # Step 5: Calculate progress
    daily_goal=round(user['weight']*35)
    progress=min(100,int((logs[today]/daily_goal)*100))

    return render_template('track.html',user=user,goal=daily_goal,intake=logs[today],progress=progress)