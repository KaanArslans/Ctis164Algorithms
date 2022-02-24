import time
start=time.time()
def selection_sort(list):
    for i in range(len(list)):
        min=i
        for j in range(i+1,len(list)):
            if list[j]<list[min]:
                min=j
        list[i],list[min]=list[min],list[i]
        # selectionSort

list1=[13,37,7,6,1,87,45,56,78,90,3543,6789,1223,34,4546,5675,67,676,687,787,565,45,45,4556,454,667,343,34343,4545,3434,34353445353534,345545,454,545,45,454545,4545,56,67,5677,67676]
selection_sort(list1)
print(list1)
end=time.time()
print("--- %s seconds ---" % (end - start))
#bruteforce
#o(n2) time complexity(quadratic)




















