from flask import Flask

# This is all setup for the web application
app = Flask(__name__)

@app.route("/")
def html_based():
    return " ".join(open("index.html","r").readlines())

@app.route("/hello")
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')