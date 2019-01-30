import codecs
from fixed_xor import fixed_xor
from collections import namedtuple, Counter

character_freq = {
  'A': 8.167,
  'B': 1.492,
  'C': 2.782,
  'D': 4.253,
  'E': 12.702,
  'F': 2.228,
  'G': 2.015,
  'H': 6.094,
  'I': 6.966,
  'J': 0.153,
  'K': 0.772,
  'L': 4.025,
  'M': 2.406,
  'N': 6.749,
  'O': 7.507,
  'P': 1.929,
  'Q': 0.095,
  'R': 5.987,
  'S': 6.327,
  'T': 9.056,
  'U': 2.758,
  'V': 0.978,
  'W': 2.360,
  'X': 0.150,
  'Y': 1.974,
  'Z': 0.074,
}

hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# hex = '0e3647e8592d35514a081243582536ed3de6734059001e3f535ce6271032'

PlaintextScore = namedtuple('PlaintextScore', ['score', 'plaintext', 'key'])

def _evaluate(deciphered_text: str) -> float:
  # deciphered_text should be a regular Python string
  # Evaluates using a Pearson chi-squared test
  decipher_text_freq = Counter(deciphered_text.upper())
  num_letters = len(deciphered_text)
  for letter in decipher_text_freq:
    decipher_text_freq[letter] /= num_letters

  chi_squared = 0.0
  for c in character_freq:
    expected_freq = character_freq[c] / 100
    chi_squared += ( (decipher_text_freq[c] - expected_freq) ** 2 ) / expected_freq

  return chi_squared

def decode_cipher(h: str) -> PlaintextScore:
  # decodes single-byte XOR cipher against English alphabet
  # evaluates each result and sorts them by score
  scores = {}
  for letter in character_freq:
    cipherkey = codecs.encode(bytes(letter, 'utf-8') * (len(h) // 2), 'hex').decode()
    deciphered_text = codecs.decode(fixed_xor(h, cipherkey), 'hex').decode('latin-1')
    scores[letter] = PlaintextScore(_evaluate(deciphered_text), deciphered_text, letter)

  return min([scores[c] for c in scores], key=lambda ps: ps.score)

if __name__ == "__main__":
  # I'm cooking ciphers like a pound of bacon!
  for choices in decode_cipher(hex):
    print(choices)
