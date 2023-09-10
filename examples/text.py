from khmerphonemizer import phonemize
from pprint import pprint

if __name__ == "__main__":
    print(phonemize("Hello, world មនុស្សខ្មែរ 😀"))
    print(phonemize("Hello, world មនុស្សខ្មែរ 😀", use_lexicon=False))
    text = "នៅលើលោកនេះមិនមានមនុស្សណាម្នាក់ចេះអស់ទេ"
    pprint(phonemize(text))
