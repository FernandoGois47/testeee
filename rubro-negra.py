RED = True
BLACK = False

class Node:
    def __init__(self, key, color=RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        self.root = self._bst_insert(self.root, new_node)
        self.fix(new_node)

    def _bst_insert(self, root, node):
        if root is None:
            return node
        if node.key < root.key:
            root.left = self._bst_insert(root.left, node)
            root.left.parent = root
        else:
            root.right = self._bst_insert(root.right, node)
            root.right.parent = root
        return root

    def fix(self, node):
        while node != self.root and node.parent.color == RED:
            grand = node.parent.parent
            if node.parent == grand.left:
                uncle = grand.right
                if uncle and uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    grand.color = RED
                    node = grand
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = BLACK
                    grand.color = RED
                    self.rotate_right(grand)
            else:
                uncle = grand.left
                if uncle and uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    grand.color = RED
                    node = grand
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = BLACK
                    grand.color = RED
                    self.rotate_left(grand)
        self.root.color = BLACK

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def print_inorder(self, node):
        if node:
            self.print_inorder(node.left)
            print(f'{node.key} {"R" if node.color else "B"}', end=' ')
            self.print_inorder(node.right)

# Exemplo de uso
if __name__ == "__main__":
    tree = RedBlackTree()
    for val in [10, 20, 30, 15, 5, 25]:
        tree.insert(val)
    print("Árvore em ordem (valor cor):")
    tree.print_inorder(tree.root)
