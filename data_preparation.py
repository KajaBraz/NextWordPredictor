import re

START_TAG = '<START> '
END_TAG = ' <END>'


# TODO handle not replacing the apostrophes in words (ex. don't)
# TODO handle e-mail addresses and special symbols appearing between letters, i.e. in the following context: \w_\w


def normalize_text(text: str, full=True) -> str:
    lower = text.lower()
    if full:
        normalized = re.sub(r'^\w\s', '', lower)
    else:
        normalized = re.sub(r'[^-%\.\w\s]', '', lower)
    return normalized


def adjust_and_tokenize(text: str) -> [str]:
    text = normalize_text(text, False)
    sentences = [START_TAG + sent + END_TAG for sent in re.split(r'\.\s', text)]
    sentences = [sent.replace('.', '') for sent in sentences]
    return sentences
