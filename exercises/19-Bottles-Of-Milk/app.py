# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range(99,0, -1):
        print(f"{i} bottles of milk on the wall, {i} bottles of milk. ")
        print(f"Take one down and pass it around, {i-1} bottles of milk on the wall.")
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.")
number_of_bottles()