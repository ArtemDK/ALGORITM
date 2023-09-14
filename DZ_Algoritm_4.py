# реализация полноценного левостороннего красно-черного дерева на Python с методом добавления новых элементов и балансировкой:
class RedBlackTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.color = 'RED'  # Новая нода всегда красная

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.root.color = 'BLACK'  # Корень дерева всегда черный

    def _insert(self, node, value):
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # Элемент уже существует, пропускаем его вставку

        # Балансировка после вставки
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def is_red(self, node):
        if node is None:
            return False
        return node.color == 'RED'

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = 'RED'
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = 'RED'
        return x

    def flip_colors(self, node):
        node.color = 'RED'
        node.left.color = 'BLACK'
        node.right.color = 'BLACK'

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

# Можно использовать этот класс, чтобы создать экземпляр дерева и вызывать его методы insert и find.

tree = RedBlackTree()
tree.insert(5)
tree.insert(3)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(7)
tree.insert(8)
tree.insert(6)

print(tree.find(7))  # True
print(tree.find(9))  # False
