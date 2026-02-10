# q1-largest
number=[1,2,42,2]

def largest(num):
    large=0
    for x in num:
        if x >large:
            large =x
    return large
print(largest(number))

# q2 -second largest

def second_largest(num):
    large=0
    second=0
    for x in num:
        if x > large:
            second=large
            large = x
        elif x != large and second < x :
            second=x
    return second
number=[1,2,42,3]
print(second_largest(number))
#q3 remove duplicate

def duplicate(l):
    remove =[]
    for x in l:
        if x not in remove :
            remove.append(x)
    return remove
l=[2,2,2,3,4,5]
print(duplicate(l))

def dupli(l):
    i=0
    while i< len(l):
        j=i+1
        while j < len(l):
            
            if l[i] == l[j]:
                l.pop(j)
            else:
                j+=1
        i+=1
    return l
print(dupli(l))

#q3 -rotate list

def rotate(num,n):
    for x in  range(n):
        first=num.pop(0)
        num.append(first)
    return num

num = [1,2,3,4,5]    
print(rotate(num,2))
            
