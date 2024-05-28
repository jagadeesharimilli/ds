def push(stack,ele):
    stack.append(ele)
    print(ele,'inserted into stack')
def pop(stack):
    if len(stack)==0:
        print('stack is empty')
        return
    print(stack[-1],'deleted successfully')
    stack.pop()
stack=[]
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
print(stack)

pop(stack)
print(stack)
