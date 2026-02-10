
def summary(num):
    if num > 50:
        return false
    if num % 5 == 0:
        return 'FIZZ'
    elif num%3==0:
        return  'bazz'
    elif num%3 ==0 and  num %5 ==0 :
        return 'fizzbuzz'
    else:
        'none'
        
print(summary(9))
