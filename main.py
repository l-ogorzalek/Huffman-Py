from huffman_encode_decode_f import encode_text_file, decode_text_file

def main():
    action = input("Choose the operation (encode/decode): ").strip().lower()

    if action not in {'encode', 'decode'}:
        print("Invalid action. Please enter either 'encode' or 'decode'.")
        return

    filename = input("Enter the name of the text file: ").strip()
    if not filename:
        print("Filename cannot be empty.")
        return

    if action == 'encode':
        encode_text_file(filename)
        print(f"Encoding successful! Encoded data has been saved to '{filename}'.")

    elif action == 'decode':
        decode_text_file(filename)
        print(f"Decoding successful! Decoded text has been saved to '{filename}'.")

if __name__ == "__main__":
    main()
