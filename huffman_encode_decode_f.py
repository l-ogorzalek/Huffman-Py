# ----------------------------------------------------------------------------------------------------------- #
#---# Kodowanie i dekodowanie pliku #---#
# ----------------------------------------------------------------------------------------------------------- #

from huffman_core_cf import construct_priority_queue, build_huffman_tree, rebuild_huffman_tree, generate_huffman_codes, encode, decode
from huffman_read_write_f import read_text_file, write_text_file, write_encoded_with_codes, read_encoded_with_codes

def encode_text_file(filename):
    input_text = read_text_file(filename)

    min_heap = construct_priority_queue(input_text)
    huffman_tree = build_huffman_tree(min_heap)

    huffman_codes = generate_huffman_codes(huffman_tree)

    encoded_text = encode(input_text, huffman_codes)

    write_encoded_with_codes(filename, encoded_text, huffman_codes)

def decode_text_file(filename):
    huffman_codes, encoded_bits = read_encoded_with_codes(filename)

    huffman_tree = rebuild_huffman_tree(huffman_codes)

    decoded_text = decode(encoded_bits, huffman_tree)

    write_text_file(filename, decoded_text)
