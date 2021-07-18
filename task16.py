#task1
list = ['a','b','c']
start = 2
def enumerate2_0(en_list, start):
 emptylist = []
 for i in range(len(en_list)):
    emptylist.append((i + start, en_list[i]))
 return emptylist
print(enumerate2_0(list, start))

#task2

def in_range(start,stop,step):
     print(start)
     while start + step < stop:
        start += step
        print(start)
in_range(17,80,7)
#task3
def counter(low, high):
    current = low
    while current < high:
        yield current
        current += 1

for c in iter(counter(3, 9)):
    print(c)

