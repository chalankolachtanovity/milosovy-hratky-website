from flask import Flask
import requests
from flask import Flask, request
from threading import Thread
from masko import *
from stano import *
from tajmoti import *
from teetou import *
from aligator import *
from allFunctions import *

app = Flask(__name__)


@app.route("/")
def home():
    with open("1_housing.html", "r") as f:
        html = f.read()
    return html


@app.route("/kmaso")
def kmaso():
    return (f'{kmasko_stat()}')


@app.route("/stano")
def stano():
    return (f'{stano_stat()}')


@app.route("/aligator")
def aligator():
    return (f'{aligator_stat()}')


@app.route("/teetou")
def teetou():
    return (f'{teetou_stat()}')


@app.route("/tajmoti")
def tajmoti():
    return (f'{tajmoti_stat()}')


@app.route("/kdratio")
def kd_ratio():
    return (f'{best_kd_ratio()}')


@app.route("/headshot_ratio")
def hs_ratio():
    return (f'{h_percentage()}')


@app.route("/other_stats")
def all_stats():
    return (f'{other_stats()}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
