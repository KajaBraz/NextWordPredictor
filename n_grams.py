from collections import defaultdict

from src import data_preparation


def create_bigrams(corpus: [str]) -> {(str, str): int}:
    normalized = data_preparation.adjust_text(corpus)
    tokenized = data_preparation.tokenize_sentences(normalized)
    bigram_counts = defaultdict(int)
    for sent in tokenized:
        words = sent.split(' ')
        for i in range(len(words) - 2):
            bigram = (words[i], words[i + 1])
            bigram_counts[bigram] += 1
    return bigram_counts
