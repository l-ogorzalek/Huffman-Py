# ----------------------------------------------------------------------------------------------------------- #
#---# Odczyt i zapis #---#
# ----------------------------------------------------------------------------------------------------------- #

def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_text_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def write_encoded_with_codes(filename, encoded_data, huffman_codes):
    with open(filename, 'wb') as file:

        for char, code in huffman_codes.items():
            if char == ' ':
                char_representation = '<space>'
            elif char == '\n':
                char_representation = '<newline>'
            else:
                char_representation = char

            line = f"{char_representation}:{code}\n"
            file.write(line.encode('utf-8'))

        file.write(b"---\n")
        
        encoded_binary = int(encoded_data, 2).to_bytes((len(encoded_data) + 7) // 8, byteorder='big')
        file.write(encoded_binary)

def read_encoded_with_codes(filename):
    with open(filename, 'rb') as file:
        huffman_codes = {}

        while True:
            line = file.readline().decode('utf-8').strip()
            if line == "---":
                break

            char_representation, code = line.split(':')
            if char_representation == '<space>':
                char = ' '
            elif char_representation == '<newline>':
                char = '\n'
            else:
                char = char_representation

            huffman_codes[char] = code

        encoded_bytes = file.read()
        encoded_bits = bin(int.from_bytes(encoded_bytes, byteorder='big'))[2:]

        padding_length = len(encoded_bits) % 8
        if padding_length != 0:
            encoded_bits = '0' * (8 - padding_length) + encoded_bits

        return huffman_codes, encoded_bits
