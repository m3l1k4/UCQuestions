
# Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)

# Inputs
# - Original list of strings
# - List of strings to be added
# - List of strings to be removed

OriginalList = ["one", "two", "three", "two"]
ListAdd = ["one", "two", "five", "six"]
DeleteList = ["two", "five","three"]

def merger(OriginalList, ListAdd, DeleteList):
    print(OriginalList,ListAdd, DeleteList,)
    return

def Compare(lsta,lstb):
# compare and removes common value between the delete list and add list
    new_lsta= list(set(lsta) - set(lstb))
    new_lstb=list(set(lstb)- set(lsta))
    print(new_lsta,"new_lsta")
    print(new_lstb,"new_lstb")

    return new_lsta,new_lstb



def Sorting(lst):

    #List shall only contain unique values
    uniqueList=list(dict.fromkeys(lst))

   # --- In the event of a tie, reverse alphabetical
    lst.sort(reverse=True)
    
    # --- Most character count to least character count
    lstSorted= sorted(lst, key=len, reverse=True)
    
    return lstSorted


def main():
 
  AddListNew,DeleteListNew=Compare(ListAdd, DeleteList)
  print(AddListNew,"newaddlist")
  print(DeleteListNew,"newdeletelist")
  merger(OriginalList, ListAdd, DeleteList)

  lstSorted=Sorting(OriginalList)
 

  print(lstSorted)


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


