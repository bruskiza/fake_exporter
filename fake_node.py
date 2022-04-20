from flask import Flask, Response
from config_metrics import *

app = Flask(__name__)

def generate_metrics():
    return_metric = ""
    for metric in metrics_go:
         return_metric = return_metric + f"""
# HELP {metric} help
# TYPE {metric} gauge
{metric} 1"""
    return return_metric

@app.route("/")
def hello_world():
    return "<p>fake exporter!</p>"

@app.route("/metrics")
def metrics():
    resp = Response(generate_metrics())
    resp.headers['Content-Type'] = 'text/plain'
    return resp

