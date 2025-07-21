def fibonacci_series():
    a=0
    b=0
    s=int(input("Enter the range of the fibonacci series: " ))
    for x in range(a,s):
        print(a)
        c=a+b
        a=b
        b=c
        a+=1
fibonacci_series()    
