def recu_fib(n):
    if n<=1:
        return n
    else:
        return recu_fib(n-1)+recu_fib(n-2)
nterms=10
print("fibonacci series")
for i in range(nterms):
 print(recu_fib(i))
