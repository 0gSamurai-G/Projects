lst1=["a","b","c"]
lst2=["a","d","e"]

def intersection(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return lst3

print(intersection(lst1,lst2))
   