"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa3qu7avj5o488pj0g-a.oregon-postgres.render.com",
        database="todo_kdrp",
        user="todo_kdrp_user",
        password="XJdSwc39WRSDnh6e0OGYJrxQGTDKaXku")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
