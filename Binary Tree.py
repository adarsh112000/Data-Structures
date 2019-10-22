#Binary Tree
#Programmed by Adarsh Choudhary.

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
                self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

if __name__ == "__main__":

    root = int(input("Enter root node : "))

    tree = Node(root)

    n = int(input("Enter number of nodes : "))

    for i in range(n):
        node = int(input("Enter a node : "))
        tree.insert(node)

    print("Binary Tree")
    tree.PrintTree()

    print("\nThankyou.")
    print("Programmed by Adarsh Choudhary.")
