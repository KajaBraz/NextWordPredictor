import re

from src import constants


def adjust_and_normalize_nltk_brawn(corpus: [[str]], n_grams_size: int) -> [[str]]:
    if n_grams_size < 1:
        return
    processed_corpus = []
    pattern_special_chars_beginning = re.compile(r'^\W+$')  # match special chars at the beginning of strings ("''")
    pattern_special_chars_end = re.compile(r'\W+$')  # match special chars at the end of strings ("nations'")
    for sent in corpus:
        lower = map(lambda w: w.lower(), sent)
        filtered = map(lambda w: pattern_special_chars_beginning.sub('', w), lower)
        filtered = map(lambda w: pattern_special_chars_end.sub('', w), filtered)
        filtered = filter(lambda w: len(w) != 0, filtered)
        updated_sent = [constants.START_TAG] * n_grams_size + list(filtered) + [constants.END_TAG]
        processed_corpus.append(updated_sent)
    return processed_corpus
