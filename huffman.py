import heapq
from collections import Counter

class hf:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
def build_tree(text):
    freq = Counter(text)
    heap = [hf(c, f) for c, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        a = hf(None, left.freq + right.freq)
        a.left = left
        a.right = right
        heapq.heappush(heap, a)
    return heap[0]

def make_code(node, code="", mapping = {}):
    if node is None:
        return
    if node.char is not None:
        mapping[node.char] = code
    make_code(node.left, code + "0", mapping)
    make_code(node.right, code + "1", mapping)
    return mapping

def nc(text, codes):
    return "".join(codes[c] for c in text)

def decode(nc, root):
    result = ""
    current = root
    for bit in nc:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            result += current.char
            current = root
    return result

text = "Yash"
root = build_tree(text)
code = make_code(root)
ncode = nc(text, code)
print(text)
print(ncode)
print(decode(ncode, root))
print(code)