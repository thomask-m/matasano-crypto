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

fn main() {
	let h: &str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	let b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";
	assert_eq!(hex_to_base64(h), b64);
}
