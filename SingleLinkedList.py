#Linked List

class Node:

    def __init__(self, value):
        self.info = value
        self.link = None

class SingleLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("The List is Empty.")
            return
        else:
            print("The List : ")
            p = self.start
            while p is not None:
                print(p.info, " ", end=" ")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        count = 0
        while p is not None:
            count += 1
            p = p.link
        print("The Total Nodes : %d"%count)

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info==x:
                print("The position of %d in List : %d"%(x, position))
                return True
            position +=1
            p = p.link
        else:
            print("%d not found."%x)
            return False

    def insert_in_beg(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def insert_at_position(self, data, k):
        if k==1:
            self.insert_in_beg(data)
            return
        p = self.start
        i = 1
        while i<k-1 and p is not None:
            p = p.link
            i += 1

        if p is None:
            print("You can only insert upto position %d"%i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, x):
        if self.start is None:
            print("The List is empty.")
            return

        if self.start.info == x:
            self.start = self.start.link
            return

        p = self.start
        while p.link is not None:
            if p.link.info ==x:
                break
            p = p.link
        if p.link is None:
            print("Element %d is not in list."%x)
        else:
            p.link = p.link.link

    def delete_first_node(self):
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return

        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def create_list(self):
        n = int(input("Enter number of elements : "))
        if n==0:
            return
        
        for i in range(n):
            data = int(input("Enter an element : "))
            self.insert_at_end(data)


if __name__=="__main__":

    list = SingleLinkedList()
    list.create_list()
    
    while True:
        print("Linked List")
        print("1. Traverse\n2. Count Nodes\n3. Search\n4. Insert\n5. Delete\n6.Exit")
        choice = int(input("Enter selection : "))
        if choice == 1:
            list.display_list()
        elif choice == 2:
            list.count_nodes()
        elif choice == 3:
            element = int(input("Enter element to be searched : "))
            list.search(element)
        elif choice == 4:
            print("1. Insert at beginning.")
            print("2. Insert at ending.")
            print("3. Insert at index.")
            choice = int(input("Enter your choice : "))
            element = int(input("Enter element : "))
            if choice == 1:
                list.insert_in_beg(element)
            elif choice == 2:
                list.insert_at_end(element)
            else:
                index = int(input("Enter index : "))
                list.insert_at_position(element, index)
        elif choice == 5:
            print("1. Delete 1st node")
            print("2. Delete last node")
            print("3. Delete node")
            choice = int(input("Enter choice : "))
            if choice == 1:
                list.delete_first_node()
            elif choice == 2:
                list.delete_last_node()
            else:
                element = int(input("Enter element : "))
                list.delete_node(element)
        else:
            break
    print("Thankyou")
    print("Programmed By Adarsh Choudhary.")
