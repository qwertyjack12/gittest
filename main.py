
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def binary_tree_width(root):
    p = root
    array_nodes = [p]
    result = []
    while array_nodes:
        array_next_nodes = []
        for el in array_nodes:
            result += el.data
            if el.left is not None:
                array_next_nodes += el.left
            if el.right is not None:
                array_next_nodes += el.right
        array_nodes = array_next_nodes
    return result

def binary_tree_length(root):


if __name__ == '__main__':
    print_hi('PyCharm')
    print(1234)
