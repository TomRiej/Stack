# Tom Rietjens
# stack Data Structure


class Stack:
    def __init__(self, maxSize=10):
        self.__maxSize = maxSize
        self.__headPointer = -1
        self.__stack = [None for i in range(self.__maxSize)]

    def push(self, value):
        if not self.isFull():
            self.__headPointer += 1
            self.__stack[self.__headPointer] = value

        else:
            print("stack is full")

    def pop(self):
        if not self.isEmpty():
            value = self.__stack[self.__headPointer]
            self.__headPointer -= 1
            return value
        else:
            print("stack is empty")

    def peek(self):
        if not self.isEmpty():
            print(self.__stack[self.__headPointer])
        else:
            print("the list is empty")

    def isFull(self):
        if self.__headPointer+1 == self.__maxSize: # +1 because headpointer includes index 0, whereas maxsize doesn't
            return True
        else:
            return False

    def isEmpty(self):
        if self.__headPointer < 0:
            return True
        else:
            return False
    
    def printStack(self):
        print(self.__stack)


def main():
    mystack = Stack(5)
    for i in range(1,8):
        mystack.push(i)
    
    
        



if __name__ == "__main__":
    main()