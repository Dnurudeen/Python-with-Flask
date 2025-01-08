from marketplace import app
from flask import render_template
from marketplace.models import Item

@app.route("/")
def home_page():
    return render_template('home.html')

# @app.route("/about/<username>")
# def about_page(username):
#     return f"<h1>Welcome to About Page {username}</h1>"
 
@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
