def create_stack():
    stack = []
    return stack


def push(stack, item):
    stack.append(item)
    print("Pushed item: " + item)


def check_empty(stack):
    return len(stack) == 0


def pop(stack):
    if check_empty(stack):
        return ("Stack is empty")
    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))

print("Stack before popping: ", str(stack))
print("Poped item: " + pop(stack))
print("Stack after popping the element: " + str(stack))
