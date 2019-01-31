from single_byte_xor import decode_cipher, PlaintextScore

def detect_single_xor(file_path: str) -> PlaintextScore:
  # Takes in a file delimited by new lines
  # of hex strings.
  # This will detect which one has most likely been encrypted by a single XOR byte
  with open(file_path, 'r') as enc:
    res = [decode_cipher(enc_string.strip()) for enc_string in enc]
    return min(res, key=lambda pts: pts.score)

if __name__ == "__main__":
  pts = detect_single_xor('./encrypted.txt')
  print('Message: {}'.format(pts.plaintext))
  print('Key: {}'.format(pts.key))
