# XOR cipher - decryption

message_1 = '391813c092a2d5ac9acb705dfe41be3df08de67d1145cbcc3f'  # encrypted by key A
message_2 = '03adeae2c8c2f2336c8a8d312733c2456e76e0b2d9068adc3f'  # encrypted by key A and then key B
message_3 = '72d0954e354045f09461dc4c911d0b58ff8963efb12c34303f'  # encrypted by key B

decrypt_text = ''

def separating_hex_string_for_future_convertion(string = 'str'):
	result = []
	for i in range(0, len(string), 2):
		result.append(string[i:i + 2])

	return result

def convert_hex_str_to_binary_string(hex_elements = ['aa']):
	result = []
	for elem in hex_elements:
		hex_int = int(elem, 16)
		bin_str = bin(hex_int)[2:]
		equal_length_binary_format = ('0' * (8 - len(bin_str))) + bin_str
		result.append(equal_length_binary_format)

	return result

def XOR_operation(bin_elems_1 = [], bin_elems_2 = []):
	result = []
	temp_bin_elem = ''
	for i in range(len(bin_elems_1)):
		for j in range(len(bin_elems_1[i])):
			if bin_elems_1[i][j] == bin_elems_2[i][j]:
				temp_bin_elem += '0'
			else:
				temp_bin_elem += '1'

		result.append(temp_bin_elem)
		temp_bin_elem = ''

	return result

def convert_bin_str_to_decimal_format(bin_elems = ['0101']):
	result = []
	for bin_elem in bin_elems:
		result.append(int(bin_elem, 2))

	return result

def converting_int_elems_to_char_elems(int_elems = [32]):
	result = ''
	for number in int_elems:
		result += chr(number)

	return result

def XOR_cipher_decryption(encrypted_text_by_A = 'a', encrypted_text_by_AB = 'ab', encrypted_text_by_B = 'b'):
	bin_elems_of_text_A = convert_hex_str_to_binary_string(separating_hex_string_for_future_convertion(encrypted_text_by_A))
	print(bin_elems_of_text_A)
	bin_elems_of_text_AB = convert_hex_str_to_binary_string(separating_hex_string_for_future_convertion(encrypted_text_by_AB))
	key_B = XOR_operation(bin_elems_of_text_A, bin_elems_of_text_AB)
	print('Key B:', key_B)
	bin_elems_of_text_B = convert_hex_str_to_binary_string(separating_hex_string_for_future_convertion(encrypted_text_by_B))
	bin_elems_of_clear_text = XOR_operation(bin_elems_of_text_B, key_B)
	decimal_elems_of_clear_text = convert_bin_str_to_decimal_format(bin_elems_of_clear_text)
	decoded_text = converting_int_elems_to_char_elems(decimal_elems_of_clear_text)

	return decoded_text


clear_text = XOR_cipher_decryption(message_1, message_2, message_3)
print(f"clear message: {clear_text}")



