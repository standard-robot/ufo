from flask import Flask, render_template
import sqlite3
import flask
from . import database, scrape, routes
app = Flask(__name__)
app.config.from_object('app.config')

def runnnn():
    scrape.scrapeit()
    database.create_tables()
    routes.create_routes(app)
    app.run(port=3000)
