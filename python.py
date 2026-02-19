#--------------
def my_reverse(num):
    arr = []
    i = 0
    while i < len(num):
        arr.insert(0, num[i])
        i += 1
    return arr

print(my_reverse([5, 3, 55, 33, 2]))

#--------------------duplication
def avoid_duplication(num):
    z = []
    i = 0
    while i < len(num):
        if num[i] not in z:
            z.append(num[i])
        i += 1
    return z

print(avoid_duplication([1, 2, 2, 3, 4, 4, 5]))
#-----------------------------
def avoid_dupli(num):
    i=0
    z=[]
    while i<len(num):
        if num[i] not in z:
            z.append(num[i])
        i+= 1
    return z
print(avoid_dupli([1,2,35,2,21]))
#------------------
def remove_duplicates(lst):
    seen = set()
    i = 0
    while i < len(lst):
        if lst[i] in seen:
            lst.pop(i)
        else:
            seen.add(lst[i])
        i += 1

my_list = [1, 2, 2, 3, 1]
remove_duplicates(my_list)
print(my_list)  # Output: [1, 2, 3]
#----------------------
def duplicate(num):
    z=[]
    for i in range(len(num)):
        if(num[i] not in z):
            z.append(num[i])
    return z
print(duplicate([1,2,2,2,0]))
#----------------
def Largest(num):
    if len(num) < 2:
       return None
    largest=num[0]
    for i in num:
       if i>largest:
           largest=i
    return largest


print(Largest([2,3,4,56,5]))
#-----------------------
def second_largest(num):
    second=largest=float('-inf')
    for n in num:
        if n > largest:
            second=largest
            largest=n
        elif n > second and n != largest:
            second=n
    return second
print(second_largest([1,2,3,4,516,62]))
#Create a list of all even numbers’ squares from 1 to 10, but only include squares greater than 10.
def list_items():
    squares=[num**2 for num in range(1,11) if num %2==0 and num**2>10 ]
    return squares
print(list_items())  # Output: [16, 36, 64, 100]
mytuple=(1,2,3,4,5)
print(mytuple.count(2))
print(mytuple.index(4))
#--count the value of tuple-------------------------
def tuple_count(tuple,value):
        return tuple.count(value)
arr=(2,2,2,4,5)
print(tuple_count(arr,2))
#---------------------------------
my_set = {"apple", "banana", "cherry"}
for i, item in enumerate(my_set):
    print(f"Index {i}: {item}")
# Output (order not guaranteed): Index 0: apple, Index 1: banana, Index 2: cherry
#-------------------------intersection-------------
def common_elemements(set1,set2):
    return set1.intersection(set2)
set1={2,4,5,5,5,5}
set2={1,3,4,5}
print(common_elemements(set1,set2))
#-----------
def remove_values(my_set, values):
    my_set.difference_update(values)

my_set = {1, 2, 3, 4}
remove_values(my_set, {2, 3})
print(my_set)  # Output: {1, 4}
#--------------------
def is_disjoint(set1, set2):
    return set1.isdisjoint(set2)

set1 = {1, 2}
set2 = {3, 4}
dcvb=is_disjoint(set1, set2)
print(dcvb)  # Output: true
#-----------------------------



number= 324354
reverse =0
while number > 0:
    digit =number % 10
    reverse =reverse*10 + digit
    number =number //10
print(reverse)

def second_largest(nums):
    largest=float('-inf')
    second=float('-inf')
    for x in nums:
        if x > largest:
            second =largest
            largest= x
        elif x > second and x!= largest:
            second =x
        return second
num=[1,3,4,5,3]
print(second_largest(num))

def secpnd_largest(nums):
    largest=float('-inf')
    second=float('-inf')
    for x in nums:
        if x > largest:
            second=largest
            largest =x
        elif  x > second and x != largest:
            second= x
    return second
num=[1,3,4,5,3]
print(secpnd_largest(num))

tup=(1,2,3,4,5,6)
tuple1=tuple(x**2 for x in tup)
print(tuple1)
print(id(tup))
print(id(tuple1))


tup1=(1,2,3)
for x in tup1:
    print(x**2)
list1=list(tup1)
list1[0]=10
tuple2=tuple(list1)
print(tuple2)


result =list(map(lambda x:x**2,num))
print(result)

number=[2,3,4,5,2]
square=[x**2 for x in number if x<5 and x%2 ==0]
print(square)

str='python'
reverse= str[::-1]
result=reverse[:-1]+reverse[-1].upper()
result2=str[0].upper()+str[1:]
result3= reverse[0].upper()+reverse[1:]
print(result2)
print(result3)
print(result)

str='jchbfhfvb'

revrse3 =str[::-1]
reverse=revrse3[:-1]+revrse3[-1].upper()
print(reverse)
value=''
for i in str:
    value=i+value
    value=value[:-1]+value[-1].upper()
print(value)

data = {1: "a", 2: "b", 3: "c", 4: "d"}
clean={k:v for k,v in data.items() if k %2 ==0}
print (clean)

numbere=[2,2,43,12,4,2313,4,2,3,4,5]
num=[x for x in numbere if x % 2==0 or x % 3==0]
print(num)

d=[1,2,3,4,5,6]
e={k:k*k for k in d}
print(e)

with open('text.txt','w') as f:
    f.write('hello world')

with open('text.txt','r') as f:
    print(f.read())
num2=list(map(lambda x:x*2,[1,2,3,4]))
print(num2)
double =list(map(lambda x: x*2,[1,2,3,4,5,6,7,7] ))
result=list(filter(lambda x:x<5 ,double))
print(result)





