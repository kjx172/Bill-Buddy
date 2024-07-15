from flask import Flask, render_template, request, redirect, url_for
from graph import Graph

app = Flask(__name__)
graph = Graph()

#sample graph
graph.add_member("Alice")
graph.add_member("Bob")
graph.add_member("Charlie")
graph.add_member("David")
graph.add_member("Ema")
graph.add_member("Fred")
graph.add_member("Gabe")
graph.add_transaction("Gabe", "Bob", 30, "Lunch")
graph.add_transaction("Gabe", "David", 10, "Drinks")
graph.add_transaction("Fred", "Bob", 10, "Sushi")
graph.add_transaction("Fred", "Charlie", 30, "Uber")
graph.add_transaction("Fred", "David", 10, "shirt")
graph.add_transaction("Fred", "Ema", 10, "Coffee")
graph.add_transaction("Bob", "Charlie", 40, "couch damage")
graph.add_transaction("Charlie", "David", 20, "Pizzas")
graph.add_transaction("David", "Ema", 50, "shoes")


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

@app.route("/log_transaction", methods=["GET", "POST"])
def log_transaction():
    if request.method == "POST":
        from_member = request.form.get("from_member")
        to_member = request.form.get("to_member")
        amount = float(request.form.get("amount"))
        reason = request.form.get("reason")

        if from_member == to_member:
            return render_template('log_transaction.html', error="Members cannot be the same.", graph=graph.graph)
        
        if amount <= 0:
            return render_template('log_transaction.html', error="Amount must be a positive number.", graph=graph.graph)

        if from_member and to_member and amount and reason:
            graph.add_transaction(from_member, to_member, amount, reason)
        return redirect(url_for('home'))
    return render_template('log_transaction.html', graph=graph.graph)

@app.route("/search_transaction")
def search_transaction():
    return render_template('search_transaction.html', graph = graph.graph)

@app.route("/search_transaction", methods=["POST"])
def search():
    search_input = request.form.get('search_input')
    search_results = graph.search_transaction(search_input)
    return render_template('search_transaction.html', results=search_results)

@app.route("/simplified_transactions")
def simplify():
    simplified_graph = graph.simplify_debts()
    return render_template('simplified_transactions.html', graph = simplified_graph)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")