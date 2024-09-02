from config.database import Base, engine
from models.users import Users


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    Users.metadata.create_all(bind=engine)