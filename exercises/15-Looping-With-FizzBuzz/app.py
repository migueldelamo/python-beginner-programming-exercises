def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    for i in range(1,100):
        if(i%3 == 0 or i%5 == 0):
            if(i%3== 0 and i%5 == 0):
                print("FizzBuzz")
            else:
                if(i%3 == 0):
                    print("Fizz")
                if(i%5 == 0):
                    print("Buzz")
        else:
            print(i)
        

# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
