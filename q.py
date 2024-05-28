def enQ(Q,ele):
    Q.append(ele)
    print(ele,'inserted into Q')
def deQ(Q):
    if len(Q)==0:
        print('Q is empty')
        return
    print(Q[0],'deleted successfully')
    Q.pop(0)
Q=[]
enQ(Q,10)
enQ(Q,20)
enQ(Q,30)
enQ(Q,40)

print(Q)

deQ(Q)

print(Q)
