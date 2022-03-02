import re

from src import constants


def adjust_and_normalize_nltk_brawn(corpus: [[str]], n_grams: int) -> [[str]]:
    if n_grams < 2:
        return
    processed_corpus = []
    pattern_special_chars_beginning = re.compile(r'^\W+$')  # match special chars at the beginning of strings ("''")
    pattern_special_chars_end = re.compile(r'\W+$')  # match special chars at the end of strings ("nations'")
    for sent in corpus:
        lower = map(lambda w: w.lower(), sent)
        filtered = map(lambda w: pattern_special_chars_beginning.sub('', w), lower)
        filtered = map(lambda w: pattern_special_chars_end.sub('', w), filtered)
        filtered = filter(lambda w: len(w) != 0, filtered)
        processed_corpus.append([constants.START_TAG] * (n_grams - 1) + list(filtered) + [constants.END_TAG])
    return processed_corpus
