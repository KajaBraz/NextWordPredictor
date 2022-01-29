import re
from collections import Counter

from NextWordPredictor.src import data_preparation


def get_lexicon(corpus):
    normalized = data_preparation.normalize_text(corpus)
    lexicon = re.split(r'\s+', normalized)
    counts = Counter(lexicon)
    return counts
