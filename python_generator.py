def gen(n):
    for x in range(1,n+1):
        yield x*x
for i in gen(6):
    print(i)

def odd(n):
    for x in range(1,n+1):
        if x % 2 !=0:
            yield x
for b in odd(10):
    print(b)

def fib(n):
  a,b=0,1
  for _ in range(1,n+1):
    yield a
    a,b=b,a+b
for x in fib(10):
  print(x)


def infinit():
  i =1
  while True:
    yield i
    i+=1
  g= infinit()
  for _ in range(6):
    print(next(g))
def divisible(lst):
    for x in lst:
        if x % 3==0:
            yield x
for x in divisible([2,3,4,5,6,778,]):
    print(x)


def add(lst):
    prev=0
    for x in lst:
        yield prev+x
        prev=1
        
for x in add([1,2,3,4,5,67]):
  
    print(x)
    
