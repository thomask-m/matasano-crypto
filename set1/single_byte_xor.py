import codecs
from fixed_xor import fixed_xor
from collections import namedtuple

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

def _evaluate(plaintext: str) -> float:
  # plaintext should be a regular Python string
  score = 0.0
  for letter in plaintext:
    if letter.upper() in character_freq:
      score += character_freq[letter.upper()]
  return score

ScorePlaintext = namedtuple('ScorePlaintext', ['score', 'plaintext', 'key'])

def decode_cipher(h: str, limit=5) -> [ScorePlaintext]:
  # decodes single-byte XOR cipher against English alphabet
  # evaluates each result and sorts them by character frequency score
  # YOU should decide which one is probably the key
  scores = {}
  for letter in character_freq:
    cipherkey = codecs.encode(bytes(letter, 'utf-8') * (len(h) // 2), 'hex').decode()
    plaintext = codecs.decode(fixed_xor(h, cipherkey), 'hex').decode('latin-1')
    scores[letter] = ScorePlaintext(_evaluate(plaintext), plaintext, letter)

  max_score_plaintext = 0
  res = []
  for letter in scores:
    if scores[letter].score > max_score_plaintext:
      max_score_plaintext = scores[letter].score
    res.append(scores[letter])

  return sorted(res, key=lambda s_p: s_p.score, reverse=True)[:limit]

if __name__ == "__main__":
  for choices in decode_cipher(hex, 3):
    print(choices)
