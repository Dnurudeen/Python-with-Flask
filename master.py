from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)


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


# Add this block to create tables when the script is run
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
        # Check if data already exists
        if not Item.query.first():
            # Add sample items
            item1 = Item(name="Laptop", price=800, barcode="123456789012", description="A high-performance laptop.")
            item2 = Item(name="Phone", price=500, barcode="987654321098", description="A smartphone with a sleek design.")
            item3 = Item(name="Headphones", price=100, barcode="111222333444", description="Noise-canceling headphones.")
            
            db.session.add_all([item1, item2, item3])
            db.session.commit()
            print("Sample data added successfully!")
        else:
            print("Sample data already exists!")
    app.run(debug=True)