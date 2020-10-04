# Tom Rietjens
# stack Data Structure


class Stack:
    def __init__(self, maxSize=10):
        self.__maxSize = maxSize
        self.__headPointer = -1
        self.__stack = [None for i in range(self.__maxSize)]

    def push(self, value):
        """pushes a user entered value to the top of the stack

        Args:
            value (string): the value the user wants to put to the stack
        """
        if not self.isFull():
            self.__headPointer += 1
            self.__stack[self.__headPointer] = value

        else:
            print("stack is full")

    def pop(self):
        """Removes and returns the top element of the stack

        Returns:
            string: The item on the top of the stack
        """
        if not self.isEmpty():
            value = self.__stack[self.__headPointer]
            self.__headPointer -= 1
            return value
        else:
            print("stack is empty")

    def peek(self):
        """prints the item at the top of the stack
        """
        if not self.isEmpty():
            print(self.__stack[self.__headPointer])
        else:
            print("the list is empty")

    def isFull(self):
        """Checks if the stack is full

        Returns:
            Bool: True for full
        """
        if self.__headPointer+1 == self.__maxSize: # +1 because headpointer includes index 0, whereas maxsize doesn't
            return True
        else:
            return False

    def isEmpty(self):
        """checks if the stack is empty

        Returns:
            Bool: True for empty
        """
        if self.__headPointer < 0:
            return True
        else:
            return False
    
    def printStack(self):
        print(self.__stack)

def menu():
    """Displays the menu to the user

    Returns:
        int: the option the user picks
    """
    print("1: Push")
    print("2: Pop")
    print("3: Peek")
    print("4: Full?")
    print("5: Empty?")
    print("6: Print stack")
    print("7: Quit")

    valid = False
    while not valid:
        option = input("What do you choose: ")
        try:
            option = int(option)
            if option in range(1,8):
                return option
            else:
                print("invalid")
        except:
            print("not valid entry")
    

def main():
    """Main procedure,  everything runs through here
    """
    valid = False
    while not valid:
        size = input("what size do you want your stack to be: ")
        try:
            size = int(size)
            valid = True
        except:
            print("not a valid size: int\n")

    mystack = Stack(size)
    
    go = True
    while go:
        option = menu()
        if option == 1:
            val = input("What do you want to push? ")
            mystack.push(val)
        elif option == 2:
            val = mystack.pop()
            print("popped", val)
        elif option == 3:
            mystack.peek()
        elif option == 4:
            print(mystack.isFull())
        elif option == 5:
            print(mystack.isEmpty())
        elif option == 6:
            mystack.printStack()
        elif option == 7:
            go = False
        
    

    
    
        



if __name__ == "__main__":
    main()