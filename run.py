from flask import Flask, jsonify, render_template
import csv
import pandas as pd
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from scrape_praw import *
import secrets
from transformer_model import *

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generates a random 32-character hex string

class SearchForm(FlaskForm):
    search_term = StringField('Search Term', validators=[DataRequired()])
    submit = SubmitField('Search')
@app.route('/', methods=["GET","POST"])
def test():

    if request.method == "POST":
        form = SearchForm()
        search_results = []
        if form.validate_on_submit():
            search_term = form.search_term.data.lower()
            print("Accessing scrape file...")
            file_name = get_search_results(search_term)

            print("File name where ", file_name)
            with open(file_name, 'r', newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                        search_results.append(row)
            #print(search_results)
    else:
        form = SearchForm()
        search_results = []
    return render_template('index.html', form=form, search_results=search_results)

@app.route('/get_user/<keyword>', methods=['GET'])
def get_user(keyword):
    # Access the 'keyword' variable, which contains the last part of the URL
    # You can use 'keyword' in your API logic

    # For demonstration, we'll return a JSON response with the keyword
    user_file_name = get_user_posts(user_id=keyword)
    print("User data is saved in ", user_file_name)
    generate_op(user_file_name)
    print("Scores for user's posts are generated!!")
    user_data = pd.read_csv(user_file_name)
    user_data['created_utc'] = pd.to_datetime(user_data['created_utc'])
    user_data_monthly = user_data[["created_utc","Score"]].groupby(pd.Grouper(key='created_utc',freq='M')).mean().reset_index()
    user_data_monthly_json = user_data_monthly.to_json(orient="records")

    print(user_data_monthly_json)
    return render_template('viz.html', data = user_data_monthly_json)

if __name__ == '__main__':
    app.run(port = 8000, debug=True)
