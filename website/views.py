# Used to render front-end or the html templates for the website
from flask import Blueprint, render_template, request, json
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
    print(request.json)
    return request.json
    '''
    country_name = request
    quick_stats = country_data.calc(country_name)
    return render_template('information.html', quick_stats = quick_stats)
    '''

# Defining hover action on map
@views.route('/hover_information', methods = ['POST'])
def hover_information():
    country_name = request.json['country']
    rtn = {
        'CO2' : country_data.CO2[country_name],
        'Ranking' : str(country_data.rank[country_name])
    }
    print(rtn)
    return json.dumps(rtn)

# Rendering AI html page
@views.route('/ai')
def ai_render():
    ml = ai('co2_trend.csv')
    img1 = ml.train()
    img2 = ml.predict()

    return render_template('ai.html', img1 = img1, img2 = img2)
