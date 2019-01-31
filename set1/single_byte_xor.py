import codecs
from fixed_xor import fixed_xor
from collections import namedtuple, Counter

character_freq = {
  ord('a'): 0.08167,
  ord('b'): 0.01492,
  ord('c'): 0.02782,
  ord('d'): 0.04253,
  ord('e'): 0.12702,
  ord('f'): 0.02228,
  ord('g'): 0.02015,
  ord('h'): 0.06094,
  ord('i'): 0.06966,
  ord('j'): 0.00153,
  ord('k'): 0.00772,
  ord('l'): 0.04025,
  ord('m'): 0.02406,
  ord('n'): 0.06749,
  ord('o'): 0.07507,
  ord('p'): 0.01929,
  ord('q'): 0.00095,
  ord('r'): 0.05987,
  ord('s'): 0.06327,
  ord('t'): 0.09056,
  ord('u'): 0.02758,
  ord('v'): 0.00978,
  ord('w'): 0.02360,
  ord('x'): 0.00150,
  ord('y'): 0.01974,
  ord('z'): 0.00074,
}

hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
PlaintextScore = namedtuple('PlaintextScore', ['score', 'plaintext', 'key'])

def _evaluate(deciphered_text: bytes) -> float:
  # deciphered_text should be bytes object
  # Evaluates using Pearson's chi-squared statistic
  decipher_text_freq = Counter(deciphered_text)
  num_letters = len(deciphered_text)
  for letter in decipher_text_freq:
    if letter not in character_freq:
      num_letters -= decipher_text_freq[letter]

  chi_squared = 0.0
  for b in character_freq:
    if b in decipher_text_freq:
      expected_freq = character_freq[b] * num_letters
      chi_squared += ( (decipher_text_freq[b] - expected_freq) ** 2 ) / expected_freq
    else:
      # we have to excessively punish characters that are weird...
      chi_squared += 100

  return chi_squared

def decode_cipher(he: str) -> PlaintextScore:
  # decodes single-byte XOR cipher against English alphabet
  # evaluates each result and returns the most likely one
  scores = {}
  h = bytes.fromhex(he)
  for i in range(0, 256):
    cipherkey = bytes([i] * len(h))
    deciphered_text = bytes.fromhex(fixed_xor(h, cipherkey))
    scores[i] = PlaintextScore(_evaluate(deciphered_text), deciphered_text, chr(i))

  return min([scores[c] for c in scores], key=lambda ps: ps.score)

if __name__ == "__main__":
  # I'm cooking ciphers like a pound of bacon!
  for choices in decode_cipher(hex):
    print(choices)
