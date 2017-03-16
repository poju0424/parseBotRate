from google import google
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Vultr!'

def search(keyWord):
    num_page = 1
    search_results = google.search(keyword, num_page)

def app1(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])