"""Init the database and the models."""

from models import Base, engine


def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
