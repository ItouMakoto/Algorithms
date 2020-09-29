def findMaxSubArray(array,star,end):
    if star==end:
        return (array,star,end,array[star])
    else:
        mid=int((star+end)/2)
        array,star_max_left,star_max_right,star_sum=findMaxSubArray(array,star,mid)
        array,end_max_left,end_max_right,end_sum=findMaxSubArray(array,mid+1,end)
        array,cross_max_left,cross_max_right,cross_sum=findCrossSubArray(array,star,mid,end)
        if star_sum>=end_sum and star_sum>=cross_sum:
            return (array,star_max_left,star_max_right,star_sum)
        if end_sum>=star_sum and end_sum>=cross_sum:
            return (array,end_max_left,end_max_right,end_sum)
        else:
            return (array,cross_max_left,cross_max_right,cross_sum)



def findCrossSubArray(array,star,mid,end):
    left_sum=min(array)-1
    right_sum =min(array)-1
    sum=0
    max_left=0
    max_right=0
    for i in range(mid,star-1,-1):
        sum+=array[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i
    sum=0
    for i in range(mid+1,end+1):
        sum +=array[i]
        if sum>right_sum:
            right_sum=sum
            max_right=i
    return (array,max_left,max_right,right_sum+left_sum)

if __name__ == '__main__':
    a=[1,2,-1,-7,10,5,4,2,-10,-3,-5]
    mid=int((0+len(a)-1)/2)
    array,max_left,max_right,value=findMaxSubArray(a,0,len(a)-1)
    print(array[max_left:max_right+1])
    # array,max_left,max_right,value=findCrossSubArray(a,0,mid,len(a)-1)
    # print(array[max_left:max_right+1])