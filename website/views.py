# Used to render front-end or the html templates for the website
from flask import Blueprint, render_template, request, json, redirect, url_for, flash
from .calculations import stats
from .calculations import ai
import os
import pandas
import sys

views = Blueprint('views', __name__, template_folder='templates')

# Calculations and statistics for each country
country_data = stats('data.csv')

# Rendering home page
@views.route('/')
def home():
    return render_template("home.html")

# Rendering interactive map
@views.route('/map')
def map():
    return render_template('map.html')

# Rendering data statistics output templates
@views.route('/click_information', methods = ['POST'])
def click_information():
    country_name = request.json['country']
    if country_name not in country_data.CO2:
        return 'No data found'
    rtn = country_data.calc(country_name)
    return json.dumps(rtn)

# Defining hover action on map
@views.route('/hover_information', methods = ['POST'])
def hover_information():
    country_name = request.json['country']
    if country_name not in country_data.CO2:
        rtn = {
            'CO2': 'No data' 
        }
    else:rtn = {
            'CO2' : country_data.CO2[country_name],
            'Ranking' : str(country_data.rank[country_name])
        }
    return json.dumps(rtn)

@views.route('/detailed_information')
def detailed_information():
    return render_template('information.html')

# Rendering AI html page
# Rendering AI html page
@views.route('/ai', methods=['GET', 'POST'])
def ai_render():
    if request.method == 'POST':
        years_to_predict = int(request.form.get('numericValue', 0))
        if years_to_predict < 2025:
            flash('Please enter a year greater than 2025!', category="error")
            return redirect(url_for('views.ai_render'))

        ml = ai('co2_trend.csv')
        img1 = ml.train()
        img2 = ml.predict(years_to_predict)
        return render_template('ai.html', img1=img1, img2=img2)

    elif request.method == 'GET':
        ml = ai('co2_trend.csv')
        img1 = ml.train()
        img2 = ml.predict(2050)
        return render_template('ai.html', img1=img1, img2=img2)