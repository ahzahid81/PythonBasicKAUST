sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sentence2 = sentence.split()

num_a_or_e = 0

for i in sentence2:
    if 'e' in i or 'a' in i:
        num_a_or_e +=1
        
print(num_a_or_e)