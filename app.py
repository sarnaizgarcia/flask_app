from flask import Flask

app = Flask(__name__)


@app.route('/')  # creates route to home page
def home():
    return 'Hello, world!'


app.run(port=5000)
