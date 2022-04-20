from re import M
from flask import Flask, Response
from config_metrics import *
from structlog import get_logger
import random
import time

log = get_logger()

app = Flask(__name__)

def get_fake_load():
    return random.randint(0, 100)

def get_fake_measure():
    return random.randint(1500, 1500000)


def generate_metrics():
    return_metric = ""
    for metric in metrics_go:
         return_metric = return_metric + f"""
# HELP {metric} help
# TYPE {metric} gauge
{metric} 1"""
    return return_metric

all_metrics = enrich()

minimal = {}

@app.route('/<job>/minimal')
def minimal_metrics(job):
    am = ""
    minimal = ["go_gc_duration_seconds",
    "go_goroutines",
    "go_info", "node_uname_info", "node_time_seconds"]
    
    for metric in minimal:
        am = am + get_metric(metric, job)
    resp = Response(am)
    resp.headers['Content-Type'] = 'text/plain'
    return resp
    

def get_metric(metric, job=None):
    m = ""
    log.info(metric)
    help = all_metrics[metric].get('help', "")
    type = all_metrics[metric].get('type', "")
    if "node_load" in metric:
        measure = get_fake_load()
    elif "node_time_seconds" in metric:
        measure = int(time.time())
    elif "node_uname_info" in metric:
        metric = f"{metric}" + "{\"fake_exporter\"}"
        if job is not None:
            metric = metric.replace("fake_exporter", job)
        measure = 1
    elif "go_info" in metric:
        metric = metric + "{version=\"notgo\"}"
        measure = 1
    elif "go_goroutines" in metric:
        measure = random.randint(2, 8)
    else:
        measure = get_fake_measure()

    if "1 if there was an error opening or reading a file, 0 otherwise" in help:
        measure = random.choice([0, 1])
    
    m = m + f"{help}\n{type}\n{metric} {measure}\n"
    if "summary" in type:
        m = m + f"{metric}_sum {measure}\n"
        m = m + f"{metric}_count {measure}\n"
    return m
    

@app.route("/all_metrics", methods=["GET"])
def generate_all_metrics():
    am = ""
    for metric in all_metrics.keys():
        am = am + get_metric(metric)
    resp = Response(am)
    resp.headers['Content-Type'] = 'text/plain'
    return resp


@app.route("/")
def hello_world():
    return "<p>fake exporter!</p>"

@app.route("/metrics")
def metrics():
    resp = Response(generate_metrics())
    resp.headers['Content-Type'] = 'text/plain'
    return resp


if __name__ == "__main__":
    log.info(all_metrics)
    app.run(debug=True)
