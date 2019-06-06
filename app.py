#!/usr/bin/env python

from random import randrange
from flask import Flask
from prometheus_client import start_http_server, Counter
import os

app = Flask('kayenta-tester')
c = Counter('requests', 'Number of requests served, by http code', ['http_code'])

@app.route('/')
def hello():
    if os.environ['APP_VERSION']=='v1':
        c.labels(http_code = '500').inc()
        return "<h1>Oops, service is not stable</h1>", 500
    else:
        c.labels(http_code = '200').inc()
        return "<h1>Oh ya! service is god damn good<h1>"

start_http_server(8000)
app.run(host = '0.0.0.0', port = 9080)
