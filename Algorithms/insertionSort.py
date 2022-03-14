
def insertionsort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1

        while j>=0 and key<list[j]:
            list[j+1]=list[j]
            j=j-1

        list[j+1]=key;

list=[10,9,8,7,6,5,4,3,2,1,0]
insertionsort(list)
print(list)

#best case= o(n) because it is adaptive meaning it detects whether it goes to inner loop or not. When array is already sorted(best case) it never goes to inner loop
#average and worst case=o(n2) there will be a nested loop.
#This algorithm is faster than bubble sort and selection sort and very effective on small data sets. But when it comes to larger data sets. it is not efficient compared to other sorting algorithms like merge sort, quick sort











