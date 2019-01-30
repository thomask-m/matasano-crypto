from single_byte_xor import decode_cipher

with open('./encrypted.txt', 'r') as enc:
  res = []

  for i, enc_string in enumerate(enc):
    res.append(decode_cipher(enc_string.strip()))
  print(min(res, key=lambda ps: ps.score))
