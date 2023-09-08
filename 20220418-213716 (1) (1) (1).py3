odd=set([x^2+1 for x in range(0,5)])
prime=set()
for i in range(2,10):
    j=2
    f=0
whilej<=i/2
if i%j==0:
        f=1
        j+=1
if f==0:
    primes.add(i) 
print("odd numbers:",odd)
print("prime numbers:",prime)
print("union:",odd.union(primes))
print("intersection:",odd.intersection(primes))
print("difference:",odd.difference(primes)) 
print("symmetric difference:",odd.symmetric difference(primes))         
