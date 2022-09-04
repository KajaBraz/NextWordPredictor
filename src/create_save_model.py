import pickle

from nltk.corpus import brown
from src import helper_functions, n_grams, constants


def create_model():
    corpus = brown.sents(categories=['news', 'editorial', 'hobbies'])
    # corpus = brown.sents()

    lexicon = helper_functions.get_counts(corpus, constants.MAX_N_GRAMS_SIZE)

    n_grams_dictionaries = {n: n_grams.create_n_grams(corpus, n) for n in range(2, constants.MAX_N_GRAMS_SIZE + 1)}
    normalized_bigrams = {n: n_grams.normalize_n_grams_counts(n_grams_dict, lexicon) for (n, n_grams_dict) in
                          n_grams_dictionaries.items()}

    pickle.dump(lexicon, open(constants.MODEL_LEXICON, 'wb'))
    pickle.dump(normalized_bigrams, open(constants.MODEL_N_GRAMS, 'wb'))

# TODO consider what to do if the number of suggestions is lower than the expected number (return additional most common
#  words (now) or just the words return from ngrams)
