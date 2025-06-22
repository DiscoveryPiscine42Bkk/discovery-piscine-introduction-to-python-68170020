print("Enter a numbr less than 25")
num = int(input())
if num < 25:
    i = num
    while i <26:
        print("Inside the loop, my variable is", i)
        i +=1
if num >25:
    print("ERROR")
