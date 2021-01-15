# Write a function that calculates the 
# nth Fibonacci number in O(n) 
# time or better without using any "for"
#  or "while" loops. (Feel free to use the space 
#  below or submit a link to your work.)

def fib(NUM):
    if NUM <= 1:
        return NUM
    return fib(NUM-1) + fib(NUM-2)

def main():
    NUM=1
    fibNum=fib(NUM)
    print("nth Fib number is: ", fibNum)


main()

