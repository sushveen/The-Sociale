from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///places.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the 'places' table model
class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    age_rating = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200), nullable=True)  # Optional: Image URL

    def __repr__(self):
        return f'<Place {self.name}>'

def create_tables():
    db.create_all()


# Home page route to render places based on filters
@app.route('/', methods=['GET', 'POST'])
def home():
    age_category = request.form.get('age_category')
    budget_min = request.form.get('budget_min')
    budget_max = request.form.get('budget_max')
    location = request.form.get('location')

    # Build the base query
    query = Place.query

    # Apply filters if present
    if age_category:
        query = query.filter(Place.age_rating == age_category)
    
    if budget_min:
        query = query.filter(Place.budget >= float(budget_min))
    
    if budget_max:
        query = query.filter(Place.budget <= float(budget_max))
    
    if location:
        query = query.filter(Place.location.like(f'%{location}%'))

    # Fetch the filtered places
    places = query.all()

    return render_template('index.html', places=places)

if __name__ == '__main__':
    app.run(debug=True)
