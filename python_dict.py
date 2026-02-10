# q-1
string='apple'
def count_value(num):
    dicti={}

    for x in num:
        if x in dicti:
            dicti[x]+=1
        else:
            dicti[x]=1
    return dicti
print(count_value(string))
# q2

        
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 5, 'c': 15, 'd': 40}

def dictionery_value(d1,d2):
    result={}
    for x in d1:
        if x in d2:
            result[x]=d1[x]+d2[x]
        else :
            result[x]=d1[x]
    for x in d2:
        if x not in result:
            result[key]=d2[key]
        return result
print(dictionery_value(d1,d2))

#q3
students = {
    "Hiba": 85,
    "Aisha": 92,
    "Zara": 88
}

def higher(data):
    max_sore=-1
    top_student=''
    for x in data:
        if data[x] > max_score:
            max_score=data[x]
            top_student=x
    return top_student 
    
print(higher(students))

students = {
    "Hiba": 85,
    "Aisha": 92,
    "Zara": 88
}

def higher(data):
    max_score= -1
    top_student=''
    for x in data:
        if data[x] > max_score:
            max_score=data[x]
            top_student=x
    return top_student 
    
print(higher(students))

        

        
        
        

            
