from flask import Flask, render_template, request, redirect, url_for
from graph import Graph

app = Flask(__name__)
graph = Graph()
#sample graph
graph.add_member("Alice")
graph.add_member("Bob")
graph.add_transaction("Alice", "Bob", 50, "Lunch")

i = 0

#default/ home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', graph = graph.graph)

@app.route("/members")
def members():
    return render_template('members.html', graph = graph.graph)

@app.route("/add_member", methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        member_name = request.form.get("member_name")
        if member_name:
            graph.add_member(member_name)
        return redirect(url_for('members'))
    return render_template('add_member.html', graph=graph.graph)

@app.route("/remove_member", methods=["GET", "POST"])
def remove_member():
    if request.method == "POST":
        member_name = request.form.get("member_name")
        if member_name:
            graph.remove_member(member_name)
        return redirect(url_for('members'))
    return render_template('remove_member.html', graph=graph.graph)

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