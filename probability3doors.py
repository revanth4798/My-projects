def func(s):
    arr= np.zeros(s)
    a=0
    b=0  
    arr[np.random.randint(0,s)]=1
    print(arr)
    for i in range(0,s):
        if(arr[i]==0):
            a+=1
        elif(arr[i]==1):
            b+=1

    print('With switching {} and without switching {}'.format((a/(a+b)),(b/(a+b))))
