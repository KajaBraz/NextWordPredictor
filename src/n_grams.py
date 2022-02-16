from collections import defaultdict, Counter

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

def normalize_bigrams_counts(bigrams_counts:{(str,str):int}, lexicon_counts:Counter)->{(str,str):float}:
    normalized_bigrams_counts = {}
    for bigram, count in bigrams_counts.items():
        total_counts_first_word = lexicon_counts[bigram[0]]
        normalized_bigrams_counts[bigram] = count/total_counts_first_word
    return normalized_bigrams_counts