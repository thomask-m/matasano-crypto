pub fn hex_to_base64(hexstr: &str) -> String {
	match hex::decode(hexstr) {
		Ok(h) => base64::encode(&h),
		Err(_) => String::from("Error"),
	}
}
