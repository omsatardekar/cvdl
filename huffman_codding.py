import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    
    def __lt__(self, other):
        return self.freq < other.freq


def printNodes(node, val=''):
    
    newVal = val + str(node.huff)

    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")


def main():
    
    chars = input("Enter the characters (comma-separated): ").split(",")
    chars = [char.strip() for char in chars]

   
    freq = input("Enter the frequencies (comma-separated, corresponding to the characters): ").split(",")
    freq = list(map(int, freq))

    if len(chars) != len(freq):
        print("Error: The number of characters and frequencies must match!")
        return

   
    nodes = []
    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x]))

   
    while len(nodes) > 1:
       
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

       
        left.huff = 0
        right.huff = 1

        
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)

  
    print("\nHuffman Codes:")
    printNodes(nodes[0])



if __name__ == "__main__":
    main()
