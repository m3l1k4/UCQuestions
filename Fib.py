#Author: Melika Salehi
#Date: January 14, 2021
#This is in Python3

def fib(NUM):
    if NUM <= 1:
        return NUM
    return fib(NUM-1) + fib(NUM-2)

def main():
    NUM=1
    fibNum=fib(NUM)
    print("nth Fib number is: ", fibNum)


main()

