import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def member():
    pass

if __name__ == '__main__':
    app.run()
    