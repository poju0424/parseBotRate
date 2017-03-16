from google import google
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

def search(keyWord):
    num_page = 1
    search_results = google.search(keyword, num_page)