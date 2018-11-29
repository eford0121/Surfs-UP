#libraries
import sqlalchemy
import datetime as dt
import time
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

####################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Base.classes.keys()

# Save references to the tables
Station = Base.classes.station
Measurement = Base.classes.measurement

#create session
session = Session(engine)

#################################################
#Flask setup
#################################################

app = Flask(__name__)

#################################################

@app.route("/")
def welcome():
    """List all available api routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"- Precipitation <br/>"
        f"/api/v1.0/stations"
        f"-Stations<br/>"
        f"/api/v1.0/tobs<"
        f"-Tobs <br/>"
        f"/api/v1.0/<start>"
        f"-Temp statistics for a given start day</br>"
        f"/api/v1.0/<start>/<end>"
        f"-Temp Statistics for a given range"
    )



if __name__ == '__main__':
    app.run(debug=True)
