from collections import defaultdict, Counter

from src import data_preparation


def create_n_grams(corpus: [str], n_grams_size: int) -> {(str): Counter}:
    if n_grams_size < 2:
        return Counter()
    n_gram_occurrences = defaultdict(list)
    normalized_tokenized = data_preparation.adjust_and_normalize_nltk_brawn(corpus, n_grams_size)
    for sent in normalized_tokenized:
        words = sent
        for i in range(len(words) - n_grams_size):
            # cur_key =
            n_gram_occurrences[tuple([words[n] for n in range(i, i + n_grams_size - 1)])] += [
                words[i + n_grams_size - 1]]
            # n_grams = tuple([words[n] for n in range(i, i + n_grams_size)])
            # n_gram_counts[n_grams] += 1
    n_grams_counts = {}
    for preceeding_words, next_words in n_gram_occurrences.items():
        n_grams_counts[preceeding_words] = Counter(next_words)
    return n_grams_counts


# TODO check if normalisation works fine for n_grams other than bigrams

def normalize_n_grams_counts(n_grams_counts: {(str): Counter}, lexicon_counts: {int: Counter}) -> {(str): Counter}:
    normalized_n_grams_counts = {}

    for n_gram_base, next_words in n_grams_counts.items():
        normalized_n_grams_counts[n_gram_base] = Counter()
        for next_word, count in next_words.items():
            normalized_n_grams_counts[n_gram_base][next_word] = count
        # normalized_n_grams_counts[preceding_words] =

    # for n_gram, count in n_grams_counts.items():
    #     total_counts_first_word = lexicon_counts[n_gram[0]]
    #     normalized_n_grams_counts[n_gram] = count / total_counts_first_word
    return normalized_n_grams_counts
