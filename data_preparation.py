import re

START_TAG = '<START> '
END_TAG = ' <END>'


def adjust_text(text: str) -> str:
    text = ''.join([ch for ch in text if ch.isalnum() or ch in ['.', ',', ' ']])
    text_separated_commas = text.replace(', ', ' , ')
    return text_separated_commas


def tokenize_sentences(text: str) -> [str]:
    return [START_TAG + sent + END_TAG for sent in re.split(r'\.\s', text)]
