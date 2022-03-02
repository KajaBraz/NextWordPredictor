from collections import defaultdict, Counter

from src import data_preparation, helper_functions


def create_n_grams(corpus: [str], n_grams_param: int, lexicon: Counter) -> Counter:
    if n_grams_param < 2:
        return
    n_gram_counts = defaultdict(int)
    normalized_tokenized = data_preparation.adjust_and_normalize_nltk_brawn(corpus, n_grams_param)
    marked_unknown = helper_functions.mark_unknown(lexicon, normalized_tokenized)
    for sent in marked_unknown:
        words = sent
        for i in range(len(words) - n_grams_param):
            n_grams = tuple([words[n] for n in range(i, i + n_grams_param)])
            n_gram_counts[n_grams] += 1
    return Counter(n_gram_counts)


# TODO check if normalisation works fine for n_grams other than bigrams

def normalize_n_grams_counts(n_grams_counts: {(str, str): int}, lexicon_counts: Counter) -> Counter:
    normalized_n_grams_counts = Counter()
    for n_gram, count in n_grams_counts.items():
        total_counts_first_word = lexicon_counts[n_gram[0]]
        normalized_n_grams_counts[n_gram] = count / total_counts_first_word
    return normalized_n_grams_counts
