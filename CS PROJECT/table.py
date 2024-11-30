
from app import db, Place, app

# with app.app_context():
    # db.drop_all()

with app.app_context():
    db.create_all() 
    place1 = Place(
        name="Wonderla",
        age_rating="All ages",
        budget=1016,
        location="Mysore Road",
        activity="Amusement Park",
        rating=4.5, 
        num_people_min=1, 
        num_people_max=None,  # You can set this to None or a specific value
        image="https://i.ytimg.com/vi/yp3B7hdot_U/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDihT4YF-7qpCxy2Z_DfQbwpNmqIA"
            )

        # To add this entry to the database
    db.session.add(place1)
    db.session.commit()
