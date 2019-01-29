import codecs

input_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64 = codecs.encode(codecs.decode(input_hex, 'hex'), 'base64').decode()

def hex_to_b64(h):
  return codecs.encode(codecs.decode(h, 'hex'), 'base64').decode()

print(hex_to_b64(input_hex))

