"""CNA Handler module."""

import pandas as pd


def read(filename):
    """Read data from file."""
    data = pd.read_csv(filename, sep="\t")
    return data


class CNAHandler:
    """CNA Handler class."""

    def __init__(self, filename_cna, filename_variants):
        """Init CNA Handler."""
        self.cna = read(filename_cna)
        self.variants = read(filename_variants)

    def _filter_variants_by_cna(self, variants, cna):
        """Filter variants by CNA."""
        filtered_variants = []
        for _, variant_row in variants.iterrows():
            chr_var = variant_row["chr"]
            pos_var = variant_row["pos"]
            for _, cna_row in cna.iterrows():
                if chr_var == cna_row["chr"] and cna_row["start"] <= pos_var <= cna_row["end"]:
                    filtered_variants.append(variant_row)
                    break

        return pd.DataFrame(filtered_variants)

    def get_filtered_variants_by_chromosome(self, chr):
        """Get filtered variants by chromosome."""
        filtered_variants = self._filter_variants_by_cna(self.variants, self.cna)
        variants_by_chromosome = filtered_variants[filtered_variants["chr"] == chr]
        return variants_by_chromosome


if __name__ == "__main__":
    cna_handler = CNAHandler("data/cna.tsv", "data/variants.tsv")
    variants = cna_handler._filter_variants_by_cna(cna_handler.variants, cna_handler.cna)
    print(variants)
