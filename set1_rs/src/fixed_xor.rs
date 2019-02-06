pub fn fixed_xor(h1: &str, h2: &str) -> String {
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

    return hex::encode(res);
}
