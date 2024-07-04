from flask import Flask, render_template, request, redirect, url_for
from graph import Graph

app = Flask(__name__)
graph = Graph()
i = 0

#default/ home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', graph = graph.graph)

@app.route("/add_member")
def add_member():
    #add functionality
    i = 0
@app.route("/log_transaction")
def log_transaction():
    #add functionality
    i = 0
@app.route("/simplify")
def simplify():
    #add functionality
    i = 0

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")