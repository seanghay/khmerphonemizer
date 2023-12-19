from khmerphonemizer import phonemize_single

if __name__ == "__main__":
  assert phonemize_single("មាន់") == ['m', 'ŏ', 'ə', 'n']
  assert phonemize_single("មិនទាន់ទៅទេ") == ['m', 'ɨ', 'n', 't', 'ŏ', 'ə', 'n', 't', 'ɨ', 'w', 't', 'eː']
  