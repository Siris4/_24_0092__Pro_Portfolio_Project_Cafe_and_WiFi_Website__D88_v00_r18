from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Base(DeclarativeBase):
    pass

# Cafe Table Configuration
class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(250), nullable=False)
    map_url = mapped_column(String(500), nullable=False)
    img_url = mapped_column(String(500), nullable=False)
    location = mapped_column(String(250), nullable=False)
    seats = mapped_column(String(250), nullable=False)
    has_toilet = mapped_column(Boolean, nullable=False)
    has_wifi = mapped_column(Boolean, nullable=False)
    has_sockets = mapped_column(Boolean, nullable=False)
    can_take_calls = mapped_column(Boolean, nullable=False)
    coffee_price = mapped_column(String(250), nullable=True)

    # Convert the Cafe object into a dictionary for JSON serialization
    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
            "img_url": self.img_url,
            "map_url": self.map_url
        }

# Route to render the cafes dynamically in the template
@app.route('/')
def index():
    # Fetch all cafes from the database
    cafes = Cafe.query.all()
    # Convert Cafe objects to dictionaries for JSON serialization
    cafes_dict = [cafe.to_dict() for cafe in cafes]
    # Pass the cafes list to the HTML template
    return render_template('index.html', cafes=cafes_dict)

if __name__ == '__main__':
    app.run(debug=True)
