import time
start=time.time()

def bubblesort(list):

    n=len(list)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(list[j]>list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]



list1=[13,37,7,6,1,87,45,56,78,90,3543,6789,1223,34,4546,5675,67,676,687,787,565,45,45,4556,454,667,343,34343,4545,3434,34353445353534,345545,454,545,45,454545,4545,56,67,5677,67676]
bubblesort(list1)
print(list1)
end=time.time()
print("--- %s seconds ---" % (end - start))
