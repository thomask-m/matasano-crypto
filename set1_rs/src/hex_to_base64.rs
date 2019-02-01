pub fn hex_to_base64(hexstr: &str) -> String {
	let hex_bytes = hex::decode(hexstr);
	let b64 = match hex_bytes {
		Ok(h) => base64::encode(&h),
		Err(_) => String::from("Error"),
	};
	return b64;
}
