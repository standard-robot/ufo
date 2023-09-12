from flask import Flask, render_template
import sqlite3
import flask
from . import database, scrape
app = Flask(__name__)
app.config.from_object('app.config')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/ufos', methods=['GET'])
def get_all_ufos():
    conn = sqlite3.connect('db/search_sightings.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ufo_sightings')
    ufos = cursor.fetchall()

    conn.close()

    ufos_list = []
    for ufo in ufos:
        ufos_list.append({
            'date_occurred': ufo[1],
            'date_posted': ufo[2],
            'city': ufo[3],
            'state': ufo[4],
            'country': ufo[5],
            'shape': ufo[6],
            'summary': ufo[7]
        })

    return flask.jsonify(ufos_list)


@app.route('/api/ufos/locations/<location>', methods=['GET'])
def get_ufos_by_location(location):
    conn = sqlite3.connect('db/search_sightings.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM ufo_sightings WHERE state LIKE '%' || ? || '%' OR city LIKE '%' || ? || '%' OR country LIKE '%' || ? || '%';", (location,location,location))
    ufos = cursor.fetchall()
    print(ufos)

    conn.close()

    if not ufos:
        return flask.jsonify({'message': 'No UFO sightings found for this location.'}), 404

    ufos_list = []
    for ufo in ufos:
        ufos_list.append({
            'date_occurred': ufo[1],
            'date_posted': ufo[2],
            'city': ufo[3],
            'state': ufo[4],
            'country': ufo[5],
            'shape': ufo[6],
            'summary': ufo[7],
        })
    return flask.jsonify(ufos_list)


@app.route('/api/ufos/dates/<date>', methods=['GET'])
def get_ufos_by_date(date):
    conn = sqlite3.connect('db/search_sightings.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM ufo_sightings WHERE date_occurred LIKE '%' || ? || '%';", (date,))
    ufos = cursor.fetchall()

    conn.close()

    if not ufos:
        return flask.jsonify({'message': 'No UFO sightings found for this date.'}), 404

    ufos_list = []
    for ufo in ufos:
        ufos_list.append({
            'date_occurred': ufo[1],
            'date_posted': ufo[2],
            'city': ufo[3],
            'state': ufo[4],
            'country': ufo[5],
            'shape': ufo[6],
            'summary': ufo[7],
        })

    return flask.jsonify(ufos_list)


def runnnn():
    scrape.scrapeit()
    database.create_tables()
    app.run(port=3000)
