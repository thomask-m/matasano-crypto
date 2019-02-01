extern crate base64;
extern crate hex;

fn hex_to_base64(hexstr: &str) -> String {
	let hex_bytes = hex::decode(hexstr);
	let b64 = match hex_bytes {
		Ok(h) => base64::encode(&h),
		Err(_) => String::from("Error"),
	};
	return b64;
}

fn fixed_xor(h1: &str, h2: &str) -> String {
	let h1_bytes = hex::decode(h1);
	let h2_bytes = hex::decode(h2);

	if h1.len() != h2.len() {
		return "Error".to_string();
	}

	let h1_bytes = match hex::decode(h1) {
		Ok(bytes) => bytes,
		Err(_) => return "Error".to_string(),
	};

	let h2_bytes = match hex::decode(h2) {
		Ok(bytes) => bytes,
		Err(_) => return "Error".to_string(),
	};

	let mut res = Vec::new();
	let mut i = 0;
	while i < h1_bytes.len() {
		res.push(&h1_bytes[i] ^ &h2_bytes[i]);
		i += 1;
	}

	return hex::encode(res)
}

fn main() {
	let h1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	let b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";
	assert_eq!(hex_to_base64(h1), b64);

	let h2 = "1c0111001f010100061a024b53535009181c";
	let h3 = "686974207468652062756c6c277320657965";
	let expected_fxor = "746865206b696420646f6e277420706c6179";
	assert_eq!(fixed_xor(h2, h3), expected_fxor);
}
