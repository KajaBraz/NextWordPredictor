from typing import Tuple, Counter

from src import constants


def get_next_words(last_words: Tuple[str], all_n_grams_dict: {int: Counter}, max_n_grams_size: int) -> [str]:
    print('***')
    print(last_words)
    print('***')
    possible_next_n_grams = []
    for n in range(max_n_grams_size, 1, -1):
        if len(possible_next_n_grams) < constants.SUGGESTED_WORDS_NUMBER:
            new_grams = [(n_gram, count) for (n_gram, count) in all_n_grams_dict[n].items() if
                         (n_gram[:n - 1] == last_words[-(n - 1):] and n_gram[-1] not in possible_next_n_grams)]
            new_grams = sorted(new_grams, key=lambda x: x[1], reverse=True)[:constants.SUGGESTED_WORDS_NUMBER]
            possible_next_n_grams += [n_gram[-1] for n_gram, count in new_grams]

            print('---', n, '---', len(new_grams), len(possible_next_n_grams))
            print([n_gram[-1] for n_gram, count in new_grams])
    return possible_next_n_grams


def predict_next_word(n_grams_dict: Counter, lexicon: Counter, max_n_grams_size: int) -> None:
    print('PREDICT', n_grams_dict.keys())
    lexicon.pop(constants.START_TAG)
    lexicon.pop(constants.END_TAG)
    current_word = constants.START_TAG
    whole_text = ''
    current_n_gram = [constants.START_TAG] * (max_n_grams_size - 1)
    while current_word != '.':
        # print('***')
        # print(current_n_gram)
        # print('***').
        possible_next_words = get_next_words(tuple(current_n_gram), n_grams_dict, max_n_grams_size)
        missing = constants.SUGGESTED_WORDS_NUMBER - len(possible_next_words)

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

        if current_word.isnumeric() and 1 <= int(current_word) <= constants.SUGGESTED_WORDS_NUMBER:
            current_word = possible_next_words[int(current_word) - 1]

        current_n_gram = current_n_gram[1:] + [current_word] if len(
            current_n_gram) >= max_n_grams_size else current_n_gram + [current_word]
        whole_text = whole_text + ' ' + current_word
        print(f'YOUR TEXT:\n{whole_text}\n')
