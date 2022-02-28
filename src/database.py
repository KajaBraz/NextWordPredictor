from nltk.corpus import brown
from src import helper_functions, n_grams

N_GRAMS = 2

corpus = brown.sents(categories=['news', 'editorial', 'hobbies'])

lexicon = helper_functions.get_lexicon(corpus, N_GRAMS)
n_grams_dictionary = n_grams.create_n_grams(corpus, N_GRAMS)
normalized_bigrams = n_grams.normalize_n_grams_counts(n_grams_dictionary, lexicon)
