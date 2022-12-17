from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, url_for, flash, redirect
#from scrape import *

app = Flask(__name__)

comments = pd.read_csv("comments.csv")
posts = pd.read_csv("posts.csv")

messages = [{'search term': 'Message One',
             'content': 'Message One Content'},
            {'author': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('home.html',messages=messages)

@app.route('/test', methods=("GET","POST"))
def test():
    if request.method == "POST":
        #print(request)
        search = request.form['search_term']
        stDate = request.form['stDate']
        endDate = request.form['endDate']
        print(search, stDate, endDate)
        #generate_csv(search, stDate, endDate)

    return render_template('test.html')

@app.route('/viz')
def viz():
    return render_template('viz.html')

@app.route("/uploaded_data")
def upload():
    df = pd.read_csv("df_viz_2.csv")
    df = df[["datetime","author","op"]]
    df.sort_values(by='datetime')

    return df.to_csv()

if __name__ == '__main__':
        app.run(debug=True)
