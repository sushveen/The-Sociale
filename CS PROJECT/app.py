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
    age_rating = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    activity = db.Column(db.String(200), nullable=False)  
    rating = db.Column(db.Float, nullable=False)  
    num_people_min = db.Column(db.Integer, nullable=True)  
    num_people_max = db.Column(db.Integer, nullable=True) 
    image = db.Column(db.String(200), nullable=True)  

    def __repr__(self):
        return f'<Place {self.name}>'

# Route to create tables in the database
def create_tables():
    db.create_all()

# Home page route to render places based on filters
@app.route('/', methods=['GET', 'POST'])
def home():
    # Get filter criteria from the form
    age_category = request.form.get('age_category')
    budget_min = request.form.get('budget_min')
    budget_max = request.form.get('budget_max')
    location = request.form.get('location')
    activity = request.form.get('activity')
    rating_min = request.form.get('rating_min')
    num_people_min = request.form.get('num_people_min')
    num_people_max = request.form.get('num_people_max')

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
    
    if activity:
        query = query.filter(Place.activity.like(f'%{activity}%'))
    
    if rating_min:
        query = query.filter(Place.rating >= float(rating_min))
    
    if num_people_min:
        query = query.filter(Place.num_people_min >= int(num_people_min))
    
    if num_people_max:
        query = query.filter(Place.num_people_max <= int(num_people_max))

    # Fetch the filtered places
    places = query.all()

    # Render the template with the places list
    return render_template('index.html', places=places)

if __name__ == '__main__':
    app.run(debug=True)
