import re

START_TAG = '<s>'
END_TAG = '</s>'


# TODO handle not replacing the apostrophes in words (ex. don't)
# TODO handle e-mail addresses and special symbols appearing between letters, i.e. in the following context: \w_\w

def adjust_and_normalize_nltk_brawn(corpus: [[str]]) -> [[str]]:
    processed_corpus = []
    pattern_special_chars_beginning = re.compile(r'^\W+$')  # match special chars at the beginning of strings ("''")
    pattern_special_chars_end = re.compile(r'\W+$')  # match special chars at the end of strings ("nations'")
    for sent in corpus:
        lower = map(lambda w: w.lower(), sent)
        filtered = map(lambda w: pattern_special_chars_beginning.sub('', w), lower)
        filtered = map(lambda w: pattern_special_chars_end.sub('', w), filtered)
        filtered = filter(lambda w: len(w) != 0, filtered)
        processed_corpus.append([START_TAG] + list(filtered) + [END_TAG])
    return processed_corpus
