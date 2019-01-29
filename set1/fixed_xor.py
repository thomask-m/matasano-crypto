import codecs

hex1 = '1c0111001f010100061a024b53535009181c'
hex2 = '686974207468652062756c6c277320657965'

def fixed_xor(h1, h2):
  # len(h1) == len(h2)
  if len(h1) != len(h2):
    print('here we are')
    return h1
  dec1 = codecs.decode(h1, 'hex')
  dec2 = codecs.decode(h2, 'hex')

  res = []

  for d1, d2 in zip(dec1, dec2):
    res.append(d1 ^ d2)

  return codecs.encode(bytes(res), 'hex').decode()

# print(fixed_xor(hex1, hex2))

