nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

accum = 0

for w in nums:
    accum = accum + w
    
print(accum)

print("range(5): ")
for i in range(5):
    print(i)
    
print("range(0,5): ")
for i in range(0,5):
    print(i)
    
print(list(range(5)))
print(list(range(0,5)))

accum = 0

for w in range(11):
    accum = accum + w
print(accum)


sec_accum =0
for w in range(1,11):
    sec_accum = sec_accum + w

print(sec_accum)

nums = [1,2,3,4,5,6,7,8,9,10]

count = 0

for w in nums:
    count = count + 1
    
print(count)