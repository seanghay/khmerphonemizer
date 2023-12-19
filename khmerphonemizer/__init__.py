r"""
Khmer Phonemizer - A Free, Standalone and Open-Source Khmer Grapheme-to-Phonemes.
"""
import os
import csv
import re
from khmercut import tokenize
from sosap import Model


def _read_lexicon_file(file):
    lexicon = {}
    with open(file) as infile:
        for line in csv.reader(infile, delimiter="\t"):
            word, phonemes = line
            word, phonemes = word.strip(), phonemes.strip().split()
            lexicon[word] = phonemes
    return lexicon


_pattern = re.compile(r"([A-Za-z\u1780-\u17ff]+)|([^A-Za-z\u1780-\u17ff]+)")
_model_file = os.path.join(os.path.dirname(__file__), "g2p.fst")
_lexicon_file = os.path.join(os.path.dirname(__file__), "km_lexicon.tsv")
_lexicon_dict = _read_lexicon_file(_lexicon_file)
_model = Model(_model_file)


def _phoneticize(word: str):
    results = _model.phoneticize(word)
    results = list(results)
    if len(results) == 0:
        return None
    return results


def phonemize_single(word, use_lexicon: bool = True):
    r"""
    Phonemize a single word. The word must match [a-zA-Z\u1780-\u17dd]+
    """
    if word is None:
        return None
    word = word.lower()
    if use_lexicon and word in _lexicon_dict:
        return _lexicon_dict[word]
    return _phoneticize(word)


def phonemize(
    input_str: str,
    use_lexicon: bool = True,
):
    r"""
    Tokenize and Phonemize text with multiple words into list of phonemes
    """
    outputs = []
    tokens = tokenize(input_str)
    for token in tokens:
        for m in _pattern.finditer(token):
            if m[2] is not None:
                outputs.append(m[2])
                continue
            phonemes = phonemize_single(
                m[1].lower(),
                use_lexicon=use_lexicon,
            )
            outputs.append(phonemes)

    return tokens, outputs
