# q1 pallindrome 
s = "racecar"

def palindrome(s):
    result = ''
    
    for x in range(len(s)-1, -1, -1):
        result += s[x]
    
    if s == result:
        return 'is palindrome'
    return 'no, is not palindrome'

print(palindrome(s))
# q2 revrse capitailze
s = "Python"

def reverse(s):
    result = ''
    result += s[len(s)-1].upper()
    
    for x in range(len(s)-2, -1, -1):
        result += s[x].lower()
    
    return result

print(reverse(s))

#q3 -vowels count
senetence=''
def vowels_count(s):
    vowels={}
    for x in s:
        if x in 'aeiou':
            if x in vowels:
                vowels[x]+=1
            else:
                vowels[x]=1
    return vowels
    
print(vowels_count(senetence))
