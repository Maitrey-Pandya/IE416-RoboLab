# pascal.py
def factorial(n):
    fact=1
    if (n==0):
        return 1
    for i in range(1,n+1):
        fact*=i
    return fact
def C(n,r):
    if (n<0 or r<0 or n<r):
        return ValueError
    if (n==0):
        return 1
    nume=factorial(n)
    deno=factorial(n-r)*factorial(r)
    res=nume//deno
    return res
def pascalTriangle(noOfRows):
    for i in range(noOfRows):
        for k in range(((noOfRows-i))//2):
            if (noOfRows%2!=0):
                if (i%2!=0):
                    print(" ",end=" ")
                else:
                    print("  ",end=" ")
            else:
                if (i%2!=0):
                    print("  ",end=" ")
                else:
                    print(" ",end=" ")
        for j in range(i+1):
            print(C(i,j),end="  ")
        print()
    return 0
