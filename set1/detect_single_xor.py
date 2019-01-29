from single_byte_xor import decode_cipher

with open('./encrypted.txt', 'r') as enc:
  res = []

  for i, enc_string in enumerate(enc):
    for r in decode_cipher(enc_string.strip('\n'), 15):
      if r.score > 70:
        res.append(r)
  
  for candidates in sorted(res, key=lambda s_p: s_p.score):
    print(candidates)
