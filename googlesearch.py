from google import google
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECURE_KEY')

@app.route('/')
def home():
    return "black man question.jpg"

@app.errorhandler(404)
def page_not_found(error):
    return "404"

@app.route('/fetch/<word>')
def send_text_file(word):
    result = search(word)
    return result

if __name__ == '__main__':
    app.run(debug=True)

def search(keyword):
    num_page = 1
    search_results = google.search(keyword, num_page)
    return search_results