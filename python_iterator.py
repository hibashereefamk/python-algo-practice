class Reverse:
    
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index >= 0:
            x = self.data[self.index]
            self.index -= 1
            return x
        else:
            raise StopIteration

r = Reverse([1,2,3,4])

for i in r:
    print(i)


class StrIter:
    
    def __init__(self, text):
        self.text = text
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index < len(self.text):
            ch = self.text[self.index]
            self.index += 1
            return ch
        else:
            raise StopIteration

s = StrIter("HIBA")

for i in s:
    print(i)

class Even:
    
    def __init__(self, n):
        self.current = 2
        self.n = n
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current <= self.n:
            x = self.current
            self.current += 2
            return x
        else:
            raise StopIteration

e = Even(10)

for i in e:
    print(i)

class reverse:
    def __init__(self,num):
        self.num =num
        self.reverse=0
        
    def __iter__(self):
        return self
    def __next__(self):
        digit=self.num % 10
        self.reverse=self.reverse*10+digit
        self.num=self.num//10
        return self.reverse
number=reverse(2132433)
for x in number:
    print(x)
    
