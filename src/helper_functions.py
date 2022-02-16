import itertools
from collections import Counter

from src import data_preparation


def get_lexicon(corpus: [[str]]):
    normalized = data_preparation.adjust_and_normalize_nltk_brawn(corpus)
    flattened = list(itertools.chain(*normalized))
    counts = Counter(flattened)
    # counts.pop(data_preparation.START_TAG)
    # counts.pop(data_preparation.END_TAG)
    return counts
