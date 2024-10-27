song = "The rain in Spain . . ."
wds = song.split()
print(wds)

wds = song.split('ai')
print(wds)

wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))

ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)

l = ['w', '7', 0, 9]
m = l[1]
print(type(m))

b = "My, what a lovely day"
x = b.split(',')
print(type(x))

b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
print(type(a))