# def printinfo(name,age=30):
#     print("Name:",name)
#     print("age:",age)
#     return
#
# printinfo("Aman",20)
# printinfo("",21)

# def printme(mylist, *var):
#     print(mylist)
#     for v in var:
#         print(v)
#     return
#
# printme(10)
# print(2323,565,6545,54545,45454,54545)

#Wap which prints fibbonacci series of the given number
def fibo(n):
    a=0
    b=1
    print(a,end=' ')
    print(b,end=' ')
    for i in range(2,n):
        c = a+b;
        a = b
        b = c
        print(c,end=' ')


fibo(10)
