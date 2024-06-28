"""Load data from files to the database."""

import pandas as pd

from src.models import CNA, SessionLocal, Variant


def read(filename):
    """Read data from file."""
    data = pd.read_csv(filename, sep="\t")
    return data


def load_data_to_db(filename_cna, filename_variants):
    """Load data to the database."""
    cna_data = read(filename_cna)
    variants_data = read(filename_variants)

    with SessionLocal() as db:
        for _, row in cna_data.iterrows():
            try:
                cna_record = CNA(
                    chr=row["chr"], start=row["start"], end=row["end"], other_columns=row.get("other_columns", "")
                )
                db.add(cna_record)
            except Exception as exc:
                print(f"Error: {exc}")

        for _, row in variants_data.iterrows():
            try:
                variant_record = Variant(chr=row["chr"], pos=row["pos"], other_columns=row.get("other_columns", ""))
                db.add(variant_record)
            except Exception as exc:
                print(f"Error: {exc}")

        db.commit()


if __name__ == "__main__":
    filename_cna = "data/cna.tsv"
    filename_variants = "data/variants.tsv"
    load_data_to_db(filename_cna, filename_variants)
