from flask import Flask, g
import sqlite3

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'
    app.config['DATABASE'] = 'bird.db'
    app.config['DEBUG'] = True

    
    return app