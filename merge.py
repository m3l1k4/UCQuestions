
# Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)

# Inputs
# - Original list of strings
# - List of strings to be added
# - List of strings to be removed

OriginalList = ["one", "two", "three","seven"]
ListAdd = ["one", "two", "five", "six"]
DeleteList = ["two", "five"]


def Compare(lsta,lstb):
# compare and removes common value between 2 lists
    new_lsta= list(set(lsta) - set(lstb))
    new_lstb=list(set(lstb)- set(lsta))
    return new_lsta,new_lstb



def Sorting(lst):

    #List shall only contain unique values
    lst=list(set(lst))

   # --- In the event of a tie, reverse alphabetical
    lst.sort(reverse=True)
    
    # --- Most character count to least character count
    lstSorted= sorted(lst, key=len, reverse=True)

    
    print(lstSorted)
    
    return lstSorted


def main():
 
    #passing to remove shared values between the original list and delete list.
    UpdatedOrginialList,a = Compare(OriginalList,DeleteList)
    #passing to remove shared values between the add list and delete list.
    AddListNew,DeleteListNew=Compare(ListAdd, DeleteList)
    #merge original and new  
    mergedLists= UpdatedOrginialList+AddListNew
    #send to be sorted and duplicates removed
    lstSorted=Sorting(mergedLists)


 


main()



# Return

# - List shall be ordered as follows



# Other Notes
# - You can use any programming language you like
# - The function you submit shall be runnable

# For example:

# Original List = ['one', 'two', 'three',]
# Add List = ['one', 'two', 'five', 'six]
# Delete List = ['two', 'five']
#Result List = ['three', 'six', 'one'] 


