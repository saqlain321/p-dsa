class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next_leaf = None

class BPlusTree:
    def __init__(self, degree):
        self.root = BPlusTreeNode(leaf=True)
        self.degree = degree

    def insert(self, key):
        if len(self.root.keys) == (2 * self.degree) - 1:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.degree) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        degree = self.degree
        child = parent.children[index]
        new_child = BPlusTreeNode(leaf=child.leaf)

        parent.keys.insert(index, child.keys[degree - 1])
        parent.children.insert(index + 1, new_child)

        new_child.keys = child.keys[degree: (2 * degree) - 1]
        child.keys = child.keys[0:degree - 1]

        if not child.leaf:
            new_child.children = child.children[degree: (2 * degree)]
            child.children = child.children[0:degree - 1]

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.leaf:
            return False
        return self._search(node.children[i], key)


# Example usage:
if __name__ == "__main__":
    bplus_tree = BPlusTree(3)
    keys = [10, 20, 5, 6, 12, 30, 7, 17]

    for key in keys:
        bplus_tree.insert(key)

    print("Search for key 6:", bplus_tree.search(6))
    print("Search for key 21:", bplus_tree.search(21))
