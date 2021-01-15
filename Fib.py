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







# Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)

# Inputs
# - Original list of strings
# - List of strings to be added
# - List of strings to be removed

# Return
# - List shall only contain unique values
# - List shall be ordered as follows
# --- Most character count to least character count
# --- In the event of a tie, reverse alphabetical

# Other Notes
# - You can use any programming language you like
# - The function you submit shall be runnable

# For example:

# Original List = ['one', 'two', 'three',]
# Add List = ['one', 'two', 'five', 'six]
# Delete List = ['two', 'five']