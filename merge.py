#Author: Melika Salehi
#Date: January 14, 2021
#This is in Python3

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

    print(lstSorted)
 
main()




