import codecs

hex1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
hex2 = bytes.fromhex('686974207468652062756c6c277320657965')

def fixed_xor(h1: bytes, h2: bytes) -> str:
  if len(h1) != len(h2):
    print('Oops the lengths are not the same')
    return h1
  # bh1 = bytes.fromhex(h1)
  # bh2 = bytes.fromhex(h2)
  res = [d1 ^ d2 for d1, d2 in zip(h1, h2)]

  return codecs.encode(bytes(res), 'hex').decode()

if __name__ == "__main__":
  print(fixed_xor(hex1, hex2))
