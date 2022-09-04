import pickle

from src import next_word, create_save_model, constants

if not constants.MODEL_EXISTS:
    create_save_model.create_model()

model_n_grams = pickle.load(open(constants.MODEL_N_GRAMS, 'rb'))
model_lexicon = pickle.load(open(constants.MODEL_LEXICON, 'rb'))

if __name__ == '__main__':
    whole_text = ''
    current_n_gram = [constants.START_TAG] * (constants.MAX_N_GRAMS_SIZE - 1)
    current_word = current_n_gram[-1]

    while current_word != '.':
        possible_next_words = next_word.predict_next_word(current_n_gram, model_n_grams, model_lexicon,
                                                          constants.MAX_N_GRAMS_SIZE)

        print(f'\nSUGGESTED WORDS:\n{possible_next_words}')
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
