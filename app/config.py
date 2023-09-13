# Basic config which implements a DATABASE_URI
import os
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'db/search_sightings.db')}"