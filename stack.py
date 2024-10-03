class Stack:
    def __init__(self):
        self.items = []  

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        if self.is_empty():
            return "Stack is empty"  
        return self.items.pop()  

    def peek(self):
        if self.is_empty():
            return "Stack is empty"  
        return self.items[-1]  
    def is_empty(self):
        return len(self.items) == 0  
    def size(self):
        return len(self.items)  


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(10)
    print(stack.peek())  
    print(stack.pop())   
    print(stack.pop())   
    print(stack.pop())   
