from collections import defaultdict

from src import data_preparation


def create_bigrams(corpus: [str]) -> {(str, str): int}:
    bigram_counts = defaultdict(int)
    normalized_tokenized = data_preparation.adjust_and_normalize_nltk_brawn(corpus)
    for sent in normalized_tokenized:
        words = sent
        for i in range(len(words) - 2):
            bigram = (words[i], words[i + 1])
            bigram_counts[bigram] += 1
    return bigram_counts
