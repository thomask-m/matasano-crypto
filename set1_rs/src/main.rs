extern crate base64;
extern crate hex;
mod fixed_xor;
use fixed_xor::fixed_xor;
mod hex_to_base64;
use hex_to_base64::hex_to_base64;
mod single_xor_cipher;
use single_xor_cipher::single_xor_cipher;

fn main() {
    let h1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    let b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";
    assert_eq!(hex_to_base64(h1), b64);

    let h2 = "1c0111001f010100061a024b53535009181c";
    let h3 = "686974207468652062756c6c277320657965";
    let expected_fxor = "746865206b696420646f6e277420706c6179";
    assert_eq!(fixed_xor(h2, h3), expected_fxor);

    let h4 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
    let message = single_xor_cipher(h4);
    println!(
        "Plaintext: {}\nScore: {}\nKey: {}",
        message.plaintext, message.score, message.key
    );
}
