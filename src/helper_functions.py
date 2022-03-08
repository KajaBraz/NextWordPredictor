import itertools
from collections import Counter

from src import data_preparation, constants


def get_lexicon(corpus: [[str]], n_grams: int):
    normalized = data_preparation.adjust_and_normalize_nltk_brawn(corpus, n_grams)
    flattened = list(itertools.chain(*normalized))
    counts = Counter(flattened)
    # counts.pop(data_preparation.START_TAG)
    # counts.pop(data_preparation.END_TAG)
    return counts


# def remove_rare_items(n_occurrences: int, dict_obj: Counter[str:int]) -> Counter:
def remove_rare_items(n_occurrences: int, dict_obj: {str: int}) -> Counter:
    obj_no_rare_items = Counter()
    obj_no_rare_items[constants.UNKNOWN_WORD_MARKER] = 0

    for k, v in dict_obj.items():
        if v > n_occurrences:
            obj_no_rare_items[k] = v
        else:
            obj_no_rare_items[constants.UNKNOWN_WORD_MARKER] += v
    return obj_no_rare_items


def mark_unknown(lexicon: Counter, corpus: [[str]]) -> [[str]]:
    updated = []
    for sent in corpus:
        updated.append([word if word in lexicon else constants.UNKNOWN_WORD_MARKER for word in sent])
    return updated
