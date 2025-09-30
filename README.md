# 💧 Hydration Tracker

A simple Flask-based web application that helps users track their daily water intake, view hydration history, and receive personalized hydration recommendations.

---

## 🚀 Features

- ✅ Log daily water intake
- 📊 Dashboard with daily/weekly hydration stats
- 🕒 View hydration history
- 🤖 Get personalized hydration recommendations
- 🎨 Clean and responsive UI (HTML templates with Bootstrap/Tailwind-ready structure)

---

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (default, can be configured)
- **Frontend**: HTML, Jinja2 templates, Bootstrap/Tailwind (customizable)

---

## 📂 Project Structure

```
hydration_tracker-main/
│── app/
│   ├── __init__.py        # Flask app setup
│   ├── forms.py           # WTForms for input handling
│   ├── models.py          # Database models (SQLAlchemy)
│   ├── routes.py          # Flask routes and logic
│   ├── templates/         # HTML templates
│       ├── base.html
│       ├── dashboard.html
│       ├── history.html
│       ├── index.html
│       ├── recommendation.html
│       ├── track.html
│── run.py                 # App entry point
│── requirements.txt       # Python dependencies
│── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/sahilkumar5h9/hydration_tracker.git
cd hydration_tracker-main
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scriptsctivate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 5. Run the application

```bash
python run.py
```

App will be available at 👉 `http://127.0.0.1:5000`

---

## 📸 Screens (Templates)

- **Home Page**: Quick overview and navigation
- **Dashboard**: Hydration stats visualization
- **Track**: Log your daily intake
- **History**: View past logs
- **Recommendation**: AI-driven suggestions

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.
