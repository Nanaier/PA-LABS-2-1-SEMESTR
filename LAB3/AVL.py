import collections
import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, key, data):

        # Find the correct location and insert the node
        if not root:

            return TreeNode(key, data)
        elif key < root.key:
            root.left = self.insert_node(root.left, key, data)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, data)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.data = temp.data
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def search(self, root, val):
        if root is None:
            return False
        elif root.key == val:
            return root.data
        elif root.key < val:
            return self.search(root.right, val)
        elif root.key > val:
            return self.search(root.left, val)
        return False

    def isInTheTree(self, root, val):
        if root is None:
            return False
        elif root.key == val:
            return True
        elif root.key < val:
            return self.isInTheTree(root.right, val)
        elif root.key > val:
            return self.isInTheTree(root.left, val)
        return False

    def edit(self, root, val, data):
        # if root is None:
        if root.key == val:
            root.data = data
        elif root.key < val:
            self.edit(root.right, val, data)
        else:
            self.edit(root.left, val, data)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def serialize(self, root):
        components = []
        def incorporate(root, components):
            line = str(root.key) + ";" + str(root.data) + '\n'
            components.append(line)
            if root.left:
                components.append('L')
                incorporate(root.left, components)
            if root.right:
                components.append('R')
                incorporate(root.right, components)
            components.append('U')
            components.append('\n')
            return ''.join(components)

        incorporate(root, components)
        components.pop()
        return ''.join(components)

    def writeToFile(self, root, filename):
        serialized = self.serialize(root)
        myfile = open(filename, 'w')
        myfile.write(serialized)
        myfile.close()

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print("{0} ".format(root.key), end="")
        self.inOrder(root.right)



    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            print(indent, end="")
            if last:
                print("|----", end="")
                indent += "     "
            else:
                print("|----", end="")
                indent += "|    "
            print(currPtr.key, currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

    def display(self, root):
        lines_prnt = ''
        lines, *_ = self._display_aux(root)
        for line in lines:
            lines_prnt += line +"\n"
        return lines_prnt

    def _display_aux(self, root):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if root is None:
            return "", 0, 0, 0
        if root.right is None and root.left is None:
            line = '%s' % root.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if root.right is None:
            lines, n, p, x = self._display_aux(root.left)
            s = '%s' % root.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if root.left is None:
            lines, n, p, x = self._display_aux(root.right)
            s = '%s' % root.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(root.left)
        right, m, q, y = self._display_aux(root.right)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def levelOrderTraversal(self, root):
        ans = []

        # Return Null if the tree is empty
        if root is None:
            return ans

        # Initialize queue
        queue = collections.deque()
        queue.append(root)

        # Iterate over the queue until it's empty
        while queue:
            # Check the length of queue
            currSize = len(queue)
            currList = []

            while currSize > 0:
                # Dequeue element
                currNode = queue.popleft()
                currList.append(currNode.key)
                currSize -= 1

                # Check for left child
                if currNode.left is not None:
                    queue.append(currNode.left)
                # Check for right child
                if currNode.right is not None:
                    queue.append(currNode.right)

            # Append the currList to answer after each iteration
            ans.append(currList)

        # Return answer list
        return ans


def deserialize(filename):
    chars = ''
    nodes = []
    next_child = None
    f = open(filename, "r")
    for line in f:
        for char in line:
            if char not in ('L', 'R', 'U'):
                chars += char
                chars = chars.strip('\n')
            else:
                if not nodes:
                    if chars.find(";") != -1:
                        nodes.append(TreeNode(int(chars.split(";")[0]), chars.split(";")[1]))
                elif next_child == 'left':
                    if chars.find(";") != -1:
                        nodes[-1].left = (TreeNode(int(chars.split(";")[0]), chars.split(";")[1]))
                    nodes.append(nodes[-1].left)
                elif next_child == 'right':
                    if chars.find(";") != -1:
                        nodes[-1].right = (TreeNode(int(chars.split(";")[0]), chars.split(";")[1]))
                    nodes.append(nodes[-1].right)
                elif next_child == 'up':
                    nodes.pop()
                if char == 'L':
                    next_child = 'left'
                elif char == 'R':
                    next_child = 'right'
                elif char == 'U':
                    next_child = 'up'
                chars = ''
    return nodes[0]
