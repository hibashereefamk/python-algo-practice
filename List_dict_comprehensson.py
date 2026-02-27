lists=[1,2,3,4,]

square=[ x for x in lists if x % 2 == 0]
print(square)
Inputs= ["python", "java", "c"]
Output=[x.upper() for x in Inputs]
print(Output)
num=[x*10 if x %2 == 0 else x for x in lists ]
print(num)
g=[3,-1,5,-7,2]
replace=[0 if x<0 else x for x in g ]
print(replace)

count={x:x**2 for  x in lists }
print(count)
result={x:x**3 for x in lists}
print(result)

double={x:x*2 for x in lists}
print(double)
even_square={x:x*2 for x in lists if x%2==0}
print(even_square)
grthan3={x:x for x in lists if x>3}
print(grthan3)
nums = [3,-1,5,-7,2]
replacea_as={x:0 if x<0 else x for x in nums}
print(replacea_as)

text='programming'
result={char:text.count(char) for char in text}
print(result)
words = ["apple","banana","kiwi"]
result={word:len(word) for word in words}
print(result)
d = {'a':1, 'b':2, 'c':3}
swap={v:k for k,v in d.items() }
print(swap)

keys = ['name','age','city']
values = ['Hiba',22,'Malappuram']
result={k:v for k,v in zip(keys,values)}
print(result)
Nested={x:{x:x**2} for x in lists}
print(Nested)
result={x:'odd' if x%2 ==0 else 'even' for x in lists}
print(result)
