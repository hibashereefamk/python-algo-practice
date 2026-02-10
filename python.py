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



