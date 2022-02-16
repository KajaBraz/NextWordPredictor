import nltk
from nltk.corpus import brown
from src import helper_functions, n_grams

nltk.download('brown')

corpus = brown.sents(categories=['news', 'editorial', 'hobbies'])

lexicon = helper_functions.get_lexicon(corpus)
bigrams = n_grams.create_bigrams(corpus)
normalized_bigrams = n_grams.normalize_bigrams_counts(bigrams, lexicon)
