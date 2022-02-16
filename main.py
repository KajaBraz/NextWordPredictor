from src import next_word, database

lexicon = database.lexicon
bigrams = database.normalized_bigrams

if __name__ == '__main__':
    next_word.predict_next_word(bigrams, lexicon)
