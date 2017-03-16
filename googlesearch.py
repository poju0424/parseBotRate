from google import google
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECURE_KEY')

@app.route('/')
def home():
    """Render website's home page."""
    return "index"

@app.route('/about/')
def about():
    """Render the website's about page."""
    return "about"

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return "404"

@app.route('/fetch/<name>')
def send_text_file(name):
    """Send your static text file."""
    return name

if __name__ == '__main__':
    app.run(debug=True)

def search(keyWord):
    num_page = 1
    search_results = google.search(keyword, num_page)