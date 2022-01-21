from src import n_grams


def get_next_word(last_word: str, n_grams_dict: {}) -> str:
    possible_next_n_grams = [(n_gram, count) for (n_gram, count) in n_grams_dict.items() if n_gram[0] == last_word]
    if len(possible_next_n_grams) == 0:
        return ''
    most_common = max(possible_next_n_grams, key=lambda x: x[1])[0]
    return most_common


def predict_next_word(training_corpus) -> None:
    bigrams_dict = n_grams.create_bigrams(training_corpus)

    whole_text = ''
    while True:
        input_text = input('PASTE YOUR WORD AND PRESS ENTER\n')
        input_words = input_text.split(' ')

        if input_words[-1] == '.':
            return

        current_word = input_words[-1]
        next_word = get_next_word(current_word, bigrams_dict)
        whole_text = whole_text + ' ' + input_text + ' ' + next_word[1]
        print(whole_text)
