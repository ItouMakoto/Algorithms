
def mergeSort(array,star,end):
    mid = int((star + end) / 2)
    if star!=end-1:
        array=mergeSort(array, star, mid)
        array=mergeSort(array, mid, end)
    array = merge(array, star, mid, end)

    return array


def merge(array,star,mid,end):
    left=array[star:mid]
    right=array[mid:end]
    remain=array[end:]
    head=array[:star]
    l=len(left)
    r=len(right)
    result=[]
    i=0
    j=0
    while i<l and j<r:
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    result=result+left[i:] if i<l else result+right[j:]
    return  head+result+remain

if __name__ == '__main__':
    a=[7,5,4,7,3,2,1]
    result=mergeSort(a,0,len(a))
    print('result:',result)

