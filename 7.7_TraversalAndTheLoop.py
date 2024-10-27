fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']

for n in range(5):
    print(n, fruits[n])
    
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']

for n in range(len(fruits)):
    print(n, fruits[n])
    
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']

for fruit in fruits:
    print(fruit)
    
s = "python"
for idx in range(len(s)):
   print(s[idx % 2])