"""Main module for the application."""

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from src.models import CNA, SessionLocal, Variant

app = FastAPI()

filename_cna = "../data/cna.tsv"
filename_variants = "../data/variants.tsv"


def get_db():
    """Get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def health_check():
    """Return {"Hello": "World"}."""
    return {"Hello": "World"}


@app.get("/variants")
def get_variants(chromosome: int, db: Session = Depends(get_db)):
    """Get variants by chromosome."""
    variants = db.query(Variant).filter(Variant.chr == chromosome).all()
    cna_records = db.query(CNA).filter(CNA.chr == chromosome).all()
    filtered_variants = []

    for variant in variants:
        if not variant.pos:
            continue
        for cna in cna_records:
            if cna.start <= variant.pos <= cna.end:
                filtered_variants.append(variant)
                break

    return filtered_variants
