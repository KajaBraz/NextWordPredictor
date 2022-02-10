from src import next_word, database

bigrams = database.bigrams
lexicon = database.lexicon

if __name__ == '__main__':
    next_word.predict_next_word(bigrams, lexicon)
