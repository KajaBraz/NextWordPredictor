from typing import Tuple, Counter

from src import constants


def get_next_words(last_words: Tuple[str], all_n_grams_dict: {int: {(str): Counter}}, max_n_grams_size: int) -> [str]:
    not_considered = {constants.START_TAG, constants.END_TAG}
    possible_next_n_grams = []
    for n in range(max_n_grams_size, 1, -1):
        if len(possible_next_n_grams) < constants.SUGGESTED_WORDS_NUMBER:
            if last_words[-(n - 1):] in all_n_grams_dict[n]:
                new_grams_words, new_grams_counts = zip(*all_n_grams_dict[n][last_words[-(n - 1):]].most_common())
                new_grams_words = [word for word in new_grams_words if word not in not_considered]
                possible_next_n_grams += new_grams_words[:constants.SUGGESTED_WORDS_NUMBER]
    return possible_next_n_grams


def predict_next_word(current_n_gram: str, n_grams_dict: {int: {(str): Counter}}, lexicon: {int: Counter},
                      max_n_grams_size: int) -> [str]:
    possible_next_words = get_next_words(tuple(current_n_gram), n_grams_dict, max_n_grams_size)[
                          :constants.SUGGESTED_WORDS_NUMBER]
    missing = constants.SUGGESTED_WORDS_NUMBER - len(possible_next_words)

    while missing > 0:
        not_considered = {constants.START_TAG, constants.END_TAG}
        not_considered.update(possible_next_words)
        default_words, default_words_counts = zip(*lexicon[1].most_common(len(not_considered) + missing))
        possible_next_words = possible_next_words + [word[0] for word in default_words if word[0] not in not_considered]
        missing = constants.SUGGESTED_WORDS_NUMBER - len(possible_next_words)
    return possible_next_words
