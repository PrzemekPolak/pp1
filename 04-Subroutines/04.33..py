wys = 20

def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a

for n in range(1,wys+1):
    print(f'{fib(n)}',end=' ')
