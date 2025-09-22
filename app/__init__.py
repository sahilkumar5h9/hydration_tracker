import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=os.getenv('SECRET_KEY')

    from .routes import main
    app.register_blueprint(main)

    return app
