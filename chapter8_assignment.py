def analyze_text(text):
	"""Receives a string as input, counts the number of alpha characters,
	and tracks the number of letter "E's" (upper or lowercase)."""
	new_text = ""
	for char in (text):
		o_char = ord(char)
		if o_char >= 65 and o_char <= 90:
			new_text = new_text + char
		if o_char >= 97 and o_char <= 122:
			new_text = new_text + char

	text_len = len(new_text)
	num_e = text.count("e")
	num_E = text.count("E")
	all_e = num_e + num_E
	percent = (all_e / text_len) * 100
	percent = str(percent)
	all_e = str(all_e)
	text_len = str(text_len)

	return "The text contains " + text_len + " alphabetic characters, of which " + all_e + " (" + percent + "%) are 'e'."
