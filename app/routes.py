from flask import Blueprint, render_template, redirect, request, url_for, session
from datetime import date
from app.forms import UserInfoForm
import random

main = Blueprint('main', __name__)

# ✅ Helper function for water goal calculation
def calculate_water_goal(activity, steps):
    if activity == 'low':
        base = 4000
    elif activity == 'medium':
        base = 4750
    else:
        base = 5500

    if steps <= 3000:
        extra = 0
    elif steps <= 5000:
        extra = 250
    elif steps <= 7000:
        extra = 500
    else:
        extra = 1000

    return min(7000, base + extra)


# ✅ Signup/Home Route
@main.route('/', methods=['GET', 'POST'])
def home():
    form = UserInfoForm()
    if form.validate_on_submit():
        session['user'] = {
            'name': form.name.data,
            'age': form.age.data,
            'gender': form.gender.data,
            'height': form.height.data,
            'weight': form.weight.data,
            'activity_level': form.activity_level.data,
            'avg_steps': form.avg_steps.data
        }
        return redirect(url_for('main.recommendation'))
    return render_template('index.html', form=form)


# ✅ Recommendation Page
@main.route('/recommendation')
def recommendation():
    user = session.get('user')
    if not user:
        return redirect(url_for('main.home'))

    activity = user.get('activity_level')
    steps = int(user.get('avg_steps', 0))
    water_needed = calculate_water_goal(activity, steps)

    return render_template('recommendation.html', user=user, water_needed=water_needed)


# ✅ Track Water Intake
@main.route('/track', methods=['GET', 'POST'])
def track():
    user = session.get('user')
    if not user:
        return redirect(url_for('main.home'))

    today = str(date.today())
    logs = session.get('logs', {})

    if today not in logs:
        logs[today] = 0

    if request.method == 'POST':
        try:
            water = int(request.form.get('water', 0))
            logs[today] += water
            session['logs'] = logs
        except:
            pass

    activity = user.get('activity_level')
    steps = int(user.get('avg_steps', 0))
    daily_goal = calculate_water_goal(activity, steps)

    progress = min(100, int((logs[today] / daily_goal) * 100))

    return render_template('track.html',
                           user=user,
                           goal=daily_goal,
                           intake=logs[today],
                           progress=progress)


# ✅ Dashboard (Summary Page + Streak + Quote)
@main.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user:
        return redirect(url_for('main.home'))

    today = str(date.today())
    logs = session.get('logs', {})
    today_intake = logs.get(today, 0)

    activity = user.get('activity_level')
    steps = int(user.get('avg_steps', 0))
    goal = calculate_water_goal(activity, steps)

    progress = min(100, int((today_intake / goal) * 100)) if goal else 0

    # ✅ Streak logic
    streak = session.get('streak', 0)
    last_logged = session.get('last_logged')

    if last_logged != today and today_intake >= goal:
        streak += 1
        session['streak'] = streak
        session['last_logged'] = today
    elif last_logged != today and today_intake < goal:
        streak = 0
        session['streak'] = 0
        session['last_logged'] = today

    # ✅ Motivational Quotes / Facts
    quotes = [
"Your body is approximately 60% water by weight.",
"75% of Americans are chronically dehydrated according to research.",
"US adults drink an average of 44 ounces of plain water daily.",
"Your brain is about 73% water content.",
"Muscle tissue contains approximately 80% water.",
"Cartilage in joints is roughly 80% water.",
"You lose water through breath, sweat, urine and bowel movements daily.",
"Dehydration of just 2% can significantly impair physical performance.",
"All the water that will ever exist is already here right now.",
"About 20% of daily fluid intake comes from food sources.",
"Pure water is the world's first and foremost medicine. - Slovakian Proverb",
"If there is magic on this planet, it is contained in water. - Loren Eiseley",
"Water is the driving force of all nature. - Leonardo da Vinci",
"Thousands have lived without love, not one without water. - W.H. Auden",
"Water is life, and clean water means health. - Audrey Hepburn",
"When the well is dry, we know the worth of water. - Benjamin Franklin",
"Nothing is softer than water, yet nothing can resist it. - Lao Tzu",
"Water is life's matter and matrix, mother and medium. - Albert Szent-Gyorgyi",
"We forget that water and life cycles are one. - Jacques Cousteau",
"Water links us to our neighbor in profound ways. - John Thorson",
"Men need about 13 cups of fluids daily, women need 9 cups.",
"Pregnant women should aim for 10 cups of water per day.",
"Breastfeeding women need approximately 13 cups daily for optimal hydration.",
"Children ages 4-8 need about 5 cups of water daily.",
"Teenagers require 8-11 cups of fluids per day depending on gender.",
"Water helps transport oxygen and nutrients throughout your body efficiently.",
"Proper hydration aids in removing waste through urination and perspiration.",
"Water helps maintain normal body temperature through natural cooling mechanisms.",
"Staying hydrated supports your body's natural detoxification systems effectively.",
"Dehydration can trigger headaches and migraines in susceptible individuals.",
"Carry a reusable water bottle with you everywhere for easy access.",
"Freeze water bottles overnight for ice-cold hydration all day long.",
"Choose water over sugary drinks to reduce calories and improve health.",
"Add lemon or lime wedges to make plain water more appealing.",
"Drink water before, during, and after exercise for optimal performance.",
"Serve water during meals to aid digestion and nutrient absorption.",
"Opt for water when eating out instead of caloric beverages.",
"Set hourly reminders to drink water throughout your busy day.",
"Eat water-rich foods like fruits and vegetables for additional hydration.",
"Monitor urine color - pale yellow indicates good hydration levels.",
"Proper hydration can help prevent kidney stones from forming.",
"Water helps lubricate joints and reduce arthritis-related joint pain.",
"Staying hydrated may improve concentration and mental clarity significantly.",
"Dehydration can make your blood thicker, straining your heart.",
"Water consumption before meals can reduce caloric intake naturally.",
"Proper hydration helps prevent constipation and promotes regular bowel movements.",
"Your skin stays more moisturized and youthful with adequate water intake.",
"Drinking water can boost metabolism and support weight management efforts.",
"Hot climates and physical activity increase your daily water requirements.",
"Thirst is your body's late signal - drink before feeling thirsty."
]

    quote = random.choice(quotes)

    return render_template('dashboard.html',
                           goal=goal,
                           intake=today_intake,
                           progress=progress,
                           streak=streak,
                           quote=quote)
