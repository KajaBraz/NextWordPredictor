from nltk.corpus import brown
from src import helper_functions, n_grams

N_GRAMS = 2
OCCURRENCES_TO_DISCARD = 1
corpus = brown.sents(categories=['news', 'editorial', 'hobbies'])
# corpus = brown.sents()

lexicon = helper_functions.get_lexicon(corpus, N_GRAMS, OCCURRENCES_TO_DISCARD)
n_grams_dictionary = n_grams.create_n_grams(corpus, N_GRAMS, lexicon)
normalized_bigrams = n_grams.normalize_n_grams_counts(n_grams_dictionary, lexicon)
