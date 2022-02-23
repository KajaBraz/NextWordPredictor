from src import next_word, database

lexicon = database.lexicon
n_grams = database.normalized_bigrams

if __name__ == '__main__':
    print(n_grams)
    next_word.predict_next_word(n_grams, lexicon, database.N_GRAMS)
