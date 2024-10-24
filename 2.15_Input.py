n = input("Enter Your Name: ")
print("Hello", n)

str_seconds = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs%3600
mintues = secs_still_remaining//60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs", hours, "mins=", mintues, "secs=", secs_finally_remaining)

n = input("Please enter your age: ")
# user types in 18
print(type(n))