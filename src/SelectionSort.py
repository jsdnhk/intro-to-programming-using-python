# The function for sorting elements in ascending order
"""
def selectionSort(lst):
    for i in range(len(lst) - 1):
        # Find the minimum in the lst[i : len(lst)]
        currentMin, currentMinIndex = lst[i], i
  
        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin, currentMinIndex = lst[j], j

        # Swap lst[i] with lst[currentMinIndex] if necessary
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin

"""
def sort(list):
    print("sort(%s) start" % (str(list)))
    sortHelper(list, 0, len(list))  #sort the entire list
    print("sort(%s) end" % (str(list)))
    
def sortHelper(list, low, high): #low = 0, high = len(list) - 1
    print("sortHelper(%s, %s, %s) start" % (str(list), str(low), str(high)))
    if low < high:
        # Find the smallest element and its index in list[low..high]
        index_of_min = low
        min = list[low]
        for i in range(low + 1, high):
            if list[i] < min:
                min = list[i]
                index_of_min = i

        list[index_of_min], list[low] = list[low], min  #swap the values

        sortHelper(list, low + 1, high)    #all will into the function stack, and return None
        print("sortHelper(%s, %s, %s) end" % (str(list), str(low), str(high)))
    else:
        print("else: return None")
        return None

def main():
    list = [2, 3, 5, 1]
    sort(list)
    print(list)

main()