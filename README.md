# NextWordPredictor
A program, the aim of which is to give suggestions of possible next words guessed on the basis of the user's input.

With the use of the nltk's brown corpus as training data, once adequately preprocessed, the program creates n_grams as the base for the prediction of possible next words which are most probable to be chosen by the user. The size of n_grams is given in advance. To choose the best matches, the program follows the n_grams hierarchy, which means that it calculates the probabilities of the highest n_grams and in case of missing data, the same is repeated on the 'lower level', i.e. using the smaller n_grams.

The users are given suggestions of possible next words and in case their needs are not met, they may type their own word.
