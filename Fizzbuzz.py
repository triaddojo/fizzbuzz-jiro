def fizz_buzz(max_number=100):
    for i in range(1,max_number+1):
        if i%15==0: # 15 is GCM of 3 and 5
            print("Fizz Buzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)


