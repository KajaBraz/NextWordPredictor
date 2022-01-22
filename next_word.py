from src import n_grams, data_preparation

SUGGESTED_WORDS_NUMBER = 3


def get_next_word(last_word: str, n_grams_dict: {}) -> [str]:
    possible_next_n_grams = [(n_gram, count) for (n_gram, count) in n_grams_dict.items() if n_gram[0] == last_word]
    if len(possible_next_n_grams) == 0:
        return ''
    most_common = sorted(possible_next_n_grams, key=lambda x: x[1], reverse=True)[:SUGGESTED_WORDS_NUMBER]
    most_common = [bigram[1] for bigram, count in most_common]
    return most_common


def predict_next_word(training_corpus) -> None:
    bigrams_dict = n_grams.create_bigrams(training_corpus)
    current_word = data_preparation.START_TAG.strip()
    whole_text = ''
    while current_word != '.':
        possible_next_words = get_next_word(current_word, bigrams_dict)
        print(possible_next_words)
        
        input_text = input('PASTE 1, 2, OR 3, TO CHOOSE ONE OF THE WORDS OR PASTE YOUR OWN WORD AND PRESS ENTER\n')
        input_words = input_text.split(' ')
        current_word = input_words[-1]
        
        if current_word.isnumeric() and 1 <= int(current_word) <= SUGGESTED_WORDS_NUMBER:
            current_word = possible_next_words[int(current_word) - 1]
        whole_text = whole_text + ' ' + current_word
        
        print(whole_text)
