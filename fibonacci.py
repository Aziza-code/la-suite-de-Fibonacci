def fib(n):
    U0=0
    U1=1
    if n==0:
        U=U0
    elif n==1:
        U=U1
    else:
        i=2
        while(i<=n):
            U=U1+U0
            U0 = U1
            U1=U
            i+=1
    return U
n=6
print(fib(n))
