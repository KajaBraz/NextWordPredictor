from collections import Counter

from src import next_word, database, constants

lexicon = database.lexicon
n_grams = Counter(database.normalized_bigrams)

if __name__ == '__main__':
    # print(n_grams)
    next_word.predict_next_word(n_grams, lexicon, constants.N_GRAMS)

    # print(len(lexicon))

    # print(type(lexicon))
    # print(lexicon.most_common(10))
    # print(lexicon.most_common()[-10:])
    # print(sorted(lexicon.values()))

    # print(len(n_grams))
    # print(type(n_grams))
    # print(n_grams.most_common(10))
    # print(n_grams.most_common()[-10:])

    # print(len([(word, count) for word, count in lexicon.items() if count>10]))
