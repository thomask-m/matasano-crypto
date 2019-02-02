mod fixed_xor;
use fixed_xor::fixed_xor;

fn evaluate(_hexstr: String) -> f32 {
  1.0
}

pub struct PlaintextScore {
  pub plaintext: String,
  pub score: f32,
  pub key: char
}

impl PlaintextScore {
  fn new(plaintext: String, score: f32, key: char) -> PlaintextScore {
    PlaintextScore {
      plaintext: plaintext,
      score: score,
      key: key,
    }
  }
}

pub fn single_xor_cipher(hexstr: &str) -> PlaintextScore {
  let size = hexstr.len() / 2;
  let mut scores = Vec::with_capacity(256);
  for k in 0..256 {
    let mut key_extended = Vec::with_capacity(size);
    for _ in 0..size {
      key_extended.push(k as u8);
    }
    let xor = fixed_xor(hex::encode(key_extended), hexstr);
    scores.push(PlaintextScore::new(xor, evaluate(xor), k));
  }

  return PlaintextScore {
    plaintext: hexstr.to_string(),
    score: scores[0],
    key: 'A',
  };
}
