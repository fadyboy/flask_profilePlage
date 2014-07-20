# main file to run personal profile flask website

from flask import Flask, render_template
from datetime import datetime


# create instance of Flask class and assign to variable app
app = Flask(__name__)

# create url routing for the default/home page
@app.route('/')
def home():

    return render_template('index.html')

# create url routing for the about page
@app.route('/about')
def about():

    return render_template('about.html')

# create url routing for the news page
@app.route('/news')
def news():
    # create dictionary to hold links to news sites
    new_sites = {}
    new_sites['cnn'] = ("http://www.cnn.com")
    new_sites['bbc'] = ("http://www.bbc.co.uk")

    return render_template('news.html', cnn=new_sites['cnn'], bbc=new_sites['bbc'])

# create filter for current year
@app.template_filter()
def get_current_year(date):
    # get the current date
    date = datetime.now()
    current_year = date.year

    return current_year

if __name__ == "__main__":
    app.run(debug=True)