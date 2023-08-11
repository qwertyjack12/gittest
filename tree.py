class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if node.data == value:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, node):
        if self.root is None:
            self.root = node
            return

        n, p, fl_find = self.__find(self.root, None, node.data)

        if not fl_find and n:
            if node.data < n.data:
                n.left = node
            else:
                n.right = node

        return

    def __del_list_node(self, node, parent):
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None

    def __del_one_child_node(self, node, parent):
        if parent.left == node:
            if node.left is None:
                parent.left = node.right
            elif node.right is None:
                parent.left = node.left
        elif parent.right == node:
            if node.left is None:
                parent.right = node.right
            elif node.right is None:
                parent.right = node.left

    def del_node(self, value):
        n, p, fl_find = self.__find(self.root, None, value)

        if not fl_find:
            return None

        if n.left is None and n.right is None:
            self.__del_list_node(n, p)
        elif n.left is None or n.right is None:
            self.__del_one_child_node(n, p)
        else:
            nr, pr = self.__find_min(n.right, n)
            n.data = nr.data
            self.__del_one_child_node(nr, pr)

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def show_tree_deep_lnr(self, node):
        if node is None:
            return None

        self.show_tree_deep_lnr(node.left)
        print(node.data)
        self.show_tree_deep_lnr(node.right)

    def show_tree_deep_rnl(self, node):
        if node is None:
            return None

        self.show_tree_deep_rnl(node.right)
        print(node.data)
        self.show_tree_deep_rnl(node.left)

    def show_tree_width(self):
        if self.root is None:
            return None

        p = self.root
        nodes_array = [p]

        while nodes_array:
            new_nodes_array = []
            for i in nodes_array:
                print(i.data, end=' ')
                if i.left:
                    new_nodes_array += [i.left]
                if i.right:
                    new_nodes_array += [i.right]
            print()
            nodes_array = new_nodes_array
