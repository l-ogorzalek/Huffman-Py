## Węzeł drzewa

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

## heapify i sift_up do przywracania własności kopca

def heapify(arr, size, root_index):
    root = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    if left_child < size and arr[left_child].freq < arr[root].freq:
        root = left_child

    if right_child < size and arr[right_child].freq < arr[root].freq:
        root = right_child

    if root != root_index:
        arr[root_index], arr[root] = arr[root], arr[root_index]
        heapify(arr, size, root)

        
def sift_up(heap, index):
    parent_index = (index - 1) // 2

    if index > 0 and heap[index].freq < heap[parent_index].freq:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        sift_up(heap, parent_index)

## usuwanie najmniejszych elementów z kopca

def extract_min(heap):
    if len(heap) == 0:
        return None
    
    heap[0], heap[-1] = heap[-1], heap[0]
    min_element = heap.pop()

    heapify(heap, len(heap), 0)

    return min_element

## Budowanie kopca

def build_min_heap(arr):
    size = len(arr)

    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    return arr

## Budowanie kolejki priorytetowej

def construct_priority_queue(data):
    frequency = {}

    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    frequency_list = [Node(char, freq) for char, freq in frequency.items()]

    min_heap = build_min_heap(frequency_list)

    return min_heap

## Budowanie drzewa Huffmana

def build_huffman_tree(min_heap):
    while len(min_heap) > 1:
        node_x = extract_min(min_heap)  

        node_y = extract_min(min_heap)

        merged_node_z = Node(None, node_x.freq + node_y.freq)
        merged_node_z.left = node_x
        merged_node_z.right = node_y

        min_heap.append(merged_node_z)
        sift_up(min_heap, len(min_heap) - 1)

    return min_heap[0]

## Generowanie kodów

def generate_huffman_codes(node, code="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if node is not None:
        if node.left is None and node.right is None:
            code_dict[node.char] = code
        else:
            generate_huffman_codes(node.left, code + "0", code_dict)
            generate_huffman_codes(node.right, code + "1", code_dict)

    return code_dict

## Test

test_data = "this is an example for huffman encoding"

print("Original text:", test_data)

min_heap = construct_priority_queue(test_data)
huffman_tree = build_huffman_tree(min_heap)

huffman_codes = generate_huffman_codes(huffman_tree)
print("Generated Huffman Codes:", huffman_codes)

def encode(data, huffman_codes):
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data

encoded_text = encode(test_data, huffman_codes)
print("Encoded Text:", encoded_text)

def decode(encoded_data, huffman_tree):
    current_node = huffman_tree
    decoded_output = ''
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.left is None and current_node.right is None:
            decoded_output += current_node.char
            current_node = huffman_tree
    return decoded_output

decoded_text = decode(encoded_text, huffman_tree)
print("Decoded Text:", decoded_text)

print("Decoded text matches original:", decoded_text == test_data) 

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

#---# OUTPUT #---#

# Original text: this is an example for huffman encoding
# Generated Huffman Codes: {'n': '000', 't': '00100', 'u': '00101', 'm': '0011', 'o': '0100', 's': '0101', 'g': '0110', 'i': '0111', 'p': '10000', 'r': '10001', 'e': '1001', ' ': '101', 'x': '11000', 'h': '11001', 'a': '1101', 'f': '1110', 'l': '111100', 'c': '111101', 'd': '11111'}
# Encoded Text: 00100110010111010110101110101101110100010110011100011010011100001111001001101111001001000110111001001011110111000111101000101100100011110101001111101110000110
# Decoded Text: this is an example for huffman encoding
# Decoded text matches original: True