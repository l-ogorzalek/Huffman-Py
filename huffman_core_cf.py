# ----------------------------------------------------------------------------------------------------------- #
#---# Główne funkcje i klasa Node #---#
# ----------------------------------------------------------------------------------------------------------- #

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

## Usuwanie najmniejszych elementów z kopca

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

def rebuild_huffman_tree(huffman_codes):
    root = Node(None, 0)

    for char, code in huffman_codes.items():
        current_node = root
        for bit in code:
            if bit == '0':
                if not current_node.left:
                    current_node.left = Node(None, 0)
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = Node(None, 0)
                current_node = current_node.right

        current_node.char = char

    return root

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

## Kodowanie i dekodowanie

def encode(data, huffman_codes):
    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data

def decode(encoded_data, huffman_tree):
    current_node = huffman_tree
    decoded_output = ''

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_output += current_node.char
            current_node = huffman_tree
    return decoded_output
