from huffman_core_cf import construct_priority_queue, build_huffman_tree, generate_huffman_codes, encode, decode, Node 

## Test

test_data = "this is an example for huffman encoding"
print("Original text:", test_data)

min_heap = construct_priority_queue(test_data)
huffman_tree = build_huffman_tree(min_heap)

huffman_codes = generate_huffman_codes(huffman_tree)
print("Generated Huffman Codes:", huffman_codes)

encoded_text = encode(test_data, huffman_codes)
print("Encoded Text:", encoded_text)

decoded_text = decode(encoded_text, huffman_tree)
print("Decoded Text:", decoded_text)

print("Decoded text matches original:", decoded_text == test_data) 

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

#---# OUTPUT #---#

# Original text: this is an example for huffman encoding
# Generated Huffman Codes: {'m': '0000', 'o': '0001', 'n': '001', 'h': '0100', 'c': '01010', 'x': '01011', 't': '01100', 'g': '01101', 'd': '01110', 'u': '01111', 'p': '10000', 'l': '10001', 'a': '1001', 'f': '1010', 'i': '1011', 'r': '11000', 's': '11001', 'e': '1101', ' ': '111'}
# Encoded Text: 0110001001011110011111011110011111001001111110101011100100001000010001110111110100001110001110100011111010101000001001001111110100101010000101110101100101101
# Decoded Text: this is an example for huffman encoding
# Decoded text matches original: True
