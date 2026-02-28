from datetime import datetime
import os 

today =datetime.now()
formatted_data =today.strftime("%d-%m-%y")
print(formatted_data)


print(os.getcwd())

num=[1,2,3,4,5,6,7]
result =list(map(lambda x:x**3,num))
print(result)

students = [("Ani", 22), ("Binu", 18), ("Zayn", 25)]
n=len(students)
for i in range(n):
    for j in range(0,n-i-1):
        if students[i][1]< students[j][1]:
            students[j],students[j+1]=students[j+1],students[j]
print(students)
num2=[43,56,87,98,90]
result =list(filter(lambda x:x>50,num2))
print(result)

num=[1,2,3,4,5]
result =list(map(lambda x:'even' if  x%2==0 else 'odd' ,num))
print(result)
maping=['apple', 'banana', 'cherry']
result =list(map(lambda x:x.upper(),maping))
print(result)

import statistics

data = [10, 20, 20, 50, 100]

mean_value =statistics.mean(data)
media_value =statistics.media(data)


print("Mean:", mean_value)
print("Median:", median_value)
