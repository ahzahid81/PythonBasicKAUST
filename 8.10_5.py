words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []

for word in words:
    if word[-1]!='e':
        past_tense.append(word+'ed')
    else:
        past_tense.append(word + 'd')



print(past_tense)