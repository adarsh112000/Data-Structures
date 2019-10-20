#Simple Stack.

class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return(len(self.items))

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        if self.is_empty():
            return EmptyStackError("Stack is Empty.")
        return self.items[-1]

    def display(self):
        print(self.items)


if __name__=="__main__":
    st = Stack()

    while True:
        print("Stack Operations : ")
        print("1. Push\n2. Pop\n3. peek\n4. Traverse\n5. Length\n 6. Exit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            data = int(input("Enter element : "))
            st.push(data)

        elif choice == 2:
            st.pop()

        elif choice == 3:
            value = st.peek()
            print("Peek element : %d"%value)
            
        elif choice == 4:
            st.display()

        elif choice == 5:
            value = st.size()
            print("The size of Stack : %d"%value)

        else:
            break

    print("Thankyou")
    print("Programmed by Adarsh Choudhary")
