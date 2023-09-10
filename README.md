## Khmer Phonemizer

A Free, Standalone and Open-Source Khmer Grapheme-to-Phonemes.

### Installation

```shell
pip install khmerphonemizer
```

### Usage

```python
from khmerphonemizer import phonemize

text = "នៅលើលោកនេះមិនមានមនុស្សណាម្នាក់ចេះអស់ទេ"
result = phonemize(text)

print(result)
```

Output

```python
(['នៅលើ',
  'លោក',
  'នេះ',
  'មិន',
  'មាន',
  'មនុស្ស',
  'ណា',
  'ម្នាក់',
  'ចេះ',
  'អស់',
  'ទេ'],
 [['n', 'ɨ', 'w', 'l', 'əː'],
  ['l', 'oː', 'k'],
  ['n', 'i', 'h'],
  ['m', 'ɨ', 'n'],
  ['m', 'i', 'ə', 'n'],
  ['m', 'ɔ', 'n', 'u', 'h'],
  ['n', 'aː'],
  ['m', 'n', 'ĕ', 'ə', 'ʔ'],
  ['c', 'e', 'h'],
  ['ʔ', 'ɑ', 'h'],
  ['t', 'eː']])
```

Check out the [examples/](./examples/) for more examples.

### API

- `phonemize` Tokenize input text into words and phonemize each word and returns a tuple with tokens and phonemes.
  - `input_str: str` Text with multiple words.
  - `beam: int = 500` number of beam search.
  - `min_beam: int = 100`: minimum number of beam search.
  - `beam_score: float = 0.6` beam search score.
  - `use_lexicon: bool = True` Use lexicon dictionary for known words.

- `phonemize_single` Phonemize a single word.
  - `word: str` Text with single Khmer or English word only.
  - `beam: int = 500` number of beam search.
  - `min_beam: int = 100`: minimum number of beam search.
  - `beam_score: float = 0.6` beam search score.
  - `use_lexicon: bool = True` Use lexicon dictionary for known words.

### License

MIT

---

### References

Without these awesome projects from awesome people, this wouldn't be possible.

- [Khmer Word Search: Challenges, Solutions, and Semantic-Aware Search](https://arxiv.org/abs/2112.08918) (Rina Buoy and Nguonly Taing and Sovisal Chenda)
- [CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron/) (Kyle Gorman, Jackson Lee, and contributors, 2019)
- [rhasspy/gruut](https://github.com/rhasspy/gruut) (Michael Hansen et al., 2020)
- [OpenFst](https://www.openfst.org/) (Kyle Gorman et al.)
- [AdolfVonKleist/Phonetisaurus](https://github.com/AdolfVonKleist/Phonetisaurus) (Josef Novak et al., 2017)
