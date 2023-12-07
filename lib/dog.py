from models import Dog

def create_table(base, engine):
    # Create the table for the Dog model in the specified base.
    base.metadata.create_all(engine)

def save(session, dog):
    # Add the dog instance to the session and commit the changes.
    session.add(dog)
    session.commit()

def get_all(session):
    # Return a list of all Dog instances from the database.
    return session.query(Dog).all()

def find_by_name(session, name):
    # Return the Dog instance with the given name.
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    # Return the Dog instance with the given id.
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    # Return the Dog instance with the given name and breed.
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    # Update the breed of the specified Dog instance and commit the changes.
    dog.breed = breed
    session.commit()