from marketplace import app, db
from marketplace.models import Item


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