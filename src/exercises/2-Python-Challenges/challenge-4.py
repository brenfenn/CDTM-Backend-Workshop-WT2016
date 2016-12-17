from random import randint
List_unsorted=range(0,100)
for i in range(0, 100):
    List_unsorted[i]=randint(0,9)
List_sorted = sorted(List_unsorted)

print(List_sorted)