"""Models for the API."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./db.sqlite3"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()


class CNA(Base):
    """CNA model."""

    __tablename__ = "cna"

    id = Column(Integer, primary_key=True, index=True)
    chr = Column(Integer, index=True)
    start = Column(Integer)
    end = Column(Integer)
    other_columns = Column(String)


class Variant(Base):
    """Variant model."""

    __tablename__ = "variants"

    id = Column(Integer, primary_key=True, index=True)
    chr = Column(Integer, index=True)
    pos = Column(Integer)
    other_columns = Column(String)
