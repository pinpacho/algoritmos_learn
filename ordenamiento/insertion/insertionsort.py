def insertionSort(arr,n):
    for i in range(1,n):
        currentVal = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > currentVal:
            arr [j+1] = arr[j]
            j = j - 1

        arr [j+1] = currentVal
    
    return arr

if __name__ == '__main__':
    array=[6,4,3,11,10,-2]
    tamano=len(array)
    print(array)
    arreglado=insertionSort(array,tamano)
    print(arreglado)