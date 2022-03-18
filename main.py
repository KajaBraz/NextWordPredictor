from collections import Counter

from src import next_word, database, constants

lexicon = database.lexicon
n_grams = Counter(database.normalized_bigrams)

if __name__ == '__main__':
    whole_text = ''
    current_n_gram = [constants.START_TAG] * (constants.MAX_N_GRAMS_SIZE - 1)
    current_word = current_n_gram[-1]

    while current_word != '.':
        possible_next_words = next_word.predict_next_word(current_n_gram, n_grams, lexicon, constants.MAX_N_GRAMS_SIZE)

        print(f'SUGGESTED WORDS:\n{possible_next_words}')
        input_text = input('PASTE THE NUMBER THAT CORRESPONDS TO THE WORD (FROM 1 TO 10),'
                           ' TO CHOOSE ONE OF THE WORDS OR PASTE YOUR OWN WORD AND PRESS ENTER\n')
        input_words = input_text.lower().split(' ')
        current_word = input_words[-1]

        if current_word.isnumeric() and 1 <= int(current_word) <= constants.SUGGESTED_WORDS_NUMBER:
            current_word = possible_next_words[int(current_word) - 1]

        current_n_gram = current_n_gram[1:] + [current_word] if len(
            current_n_gram) >= constants.MAX_N_GRAMS_SIZE - 1 else current_n_gram + [current_word]
        whole_text = whole_text + ' ' + current_word
        print('\nYOUR TEXT:\n', whole_text)
