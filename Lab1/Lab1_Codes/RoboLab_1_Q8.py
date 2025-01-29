def fibonacci_sum(n,a=0,b=1,s=0):
    if n==0:
        return s
    else:
        return fibonacci_sum(n-1,b,a+b,s+a)
def main():
    n=int(input("Enter the number of terms : "))
    res=fibonacci_sum(n)
    print("The sum of first {0} fibonacci terms is : {1}".format(n,res))
main()
