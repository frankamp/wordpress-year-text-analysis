import os
full = set(range(1,365))
numbers = set()
for f in os.listdir('poems'):
    if f.endswith('.txt'):
        name, _, ext = f.partition('.')
        ordinal, _, number = name.partition('_')
        numbers.add(int(number))
print 'missing', full - numbers
print 'count', len(numbers)