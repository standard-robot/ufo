# App init file to scrape the data, create the db, and create the routes.
from flask import Flask
from . import database, scrape, routes
app = Flask(__name__)
app.config.from_object('app.config')

def runnnn():
    scrape.scrapeit()
    database.create_tables()
    routes.create_routes(app)
    app.run(port=3000)
