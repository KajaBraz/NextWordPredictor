from collections import Counter

from src import data_preparation, constants


def get_counts(corpus: [[str]], max_n_grams_size: int) -> {int: Counter}:
    counts = {}
    for n in range(1, max_n_grams_size + 1):
        grams = []
        normalized = data_preparation.adjust_and_normalize_nltk_brawn(corpus, n)
        for sent in normalized:
            grams += [tuple(sent[i:i + n]) for i in range(len(sent) - n)]
        counts[n] = Counter(grams)
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
