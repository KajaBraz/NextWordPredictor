from typing import Tuple

from src import data_preparation, constants

SUGGESTED_WORDS_NUMBER = 3


def get_next_word(last_words: Tuple[str], n_grams_dict: {}) -> [str]:
    possible_next_n_grams = [(n_gram, count) for (n_gram, count) in n_grams_dict.items() if
                             n_gram[:len(last_words)] == last_words and n_gram[-1]!=constants.UNKNOWN_WORD_MARKER]
    # print(sorted(possible_next_n_grams, key=lambda x: x[1], reverse=True))
    # print('POSS', possible_next_n_grams)
    if len(possible_next_n_grams) == 0:
        return []
    most_common = sorted(possible_next_n_grams, key=lambda x: x[1], reverse=True)[:SUGGESTED_WORDS_NUMBER]
    most_common = [n_gram[-1] for n_gram, count in most_common]
    return most_common


def predict_next_word(n_grams_dict, lexicon, n_grams) -> None:
    lexicon.pop(data_preparation.START_TAG)
    lexicon.pop(data_preparation.END_TAG)
    lexicon.pop(constants.UNKNOWN_WORD_MARKER)
    current_word = data_preparation.START_TAG
    whole_text = ''
    current_n_gram = [data_preparation.START_TAG] * (n_grams - 1)
    while current_word != '.':
        # print('***')
        # print(current_n_gram)
        # print('***')
        possible_next_words = get_next_word(tuple(current_n_gram), n_grams_dict)
        missing = SUGGESTED_WORDS_NUMBER - len(possible_next_words)

        # TODO when suggesting most common words from lexicon (in case of missing n_grams in dictionary), prevent
        #  duplications (it can happen that we have just one matching n_gram in the n_gram dict and if the suggested
        #  word is ex. "the", the rest of the suggested words will be taken from the lexicon and "the" can be the most
        #  common word; this way it will be doubled in suggestions)

        if missing > 0:
            default_words = [word for word, count in lexicon.most_common(missing)]
            possible_next_words = possible_next_words + default_words
        print(f'SUGGESTED WORDS:\n{possible_next_words}')
        input_text = input('PASTE 1, 2, OR 3, TO CHOOSE ONE OF THE WORDS OR PASTE YOUR OWN WORD AND PRESS ENTER\n')
        input_words = input_text.split(' ')
        current_word = input_words[-1]

        if current_word.isnumeric() and 1 <= int(current_word) <= SUGGESTED_WORDS_NUMBER:
            current_word = possible_next_words[int(current_word) - 1]

        current_n_gram = current_n_gram[1:] + [current_word]
        whole_text = whole_text + ' ' + current_word
        print(f'YOUR TEXT:\n{whole_text}\n')
