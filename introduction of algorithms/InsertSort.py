a=[2,6,4,6,8,0,9,-1]
for  i in range(1,len(a)):
    key=a[i]
    print("i:",i)
    print("key:",key)

    for j in range(i-1,-1,-1):
        print('j',j)
        if a[j]>=key:
            a[j+1]=a[j]

        else:
            a[j+1]=key
            break
        if j==0:
            a[j]=key
    print('a',a)
