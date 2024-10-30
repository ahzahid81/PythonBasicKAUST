sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sentence2 = sentence.split()

same_letter_count = 0

for item in sentence2:
    if item[0] == item[-1]:
        same_letter_count +=1
        
print(same_letter_count)