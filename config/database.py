from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql+psycopg2://sadewawicak:postgres@localhost:5432/fast_api_template",
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base = declarative_base()
def get_db():
    """
    Create a database session.
    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()