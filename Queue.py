#Queue Data Structure
class EmptyQueueError(Exception):
    pass


class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            return
        self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return EmptyQueueError("Queue is Empty.")
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)


if __name__=="__main__":
    qu = Queue()

    while True:
        print("Queue Operations : ")
        print("1. Enqueue\n2. Dequeue\n3. Length\n4. Peek\n5. Traverse\n6. Exit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            data = int(input("Enter element : "))
            qu.enqueue(data)

        elif choice == 2:
            qu.dequeue()

        elif choice == 3:
            value =qu.size()
            print("The length : %d"%value)

        elif choice == 4:
            value = qu.peek()
            print("Peek element : %d"%value)

        elif choice == 5:
            print("Queue : ",qu.display())

        else:
            break

    print("Thankyou")
    print("Programmed by Adarsh Choudhary.")
