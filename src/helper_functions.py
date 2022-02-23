import itertools
from collections import Counter

from src import data_preparation


def get_lexicon(corpus: [[str]], n_grams: int):
    normalized = data_preparation.adjust_and_normalize_nltk_brawn(corpus, n_grams)
    flattened = list(itertools.chain(*normalized))
    counts = Counter(flattened)
    # counts.pop(data_preparation.START_TAG)
    # counts.pop(data_preparation.END_TAG)
    return counts
