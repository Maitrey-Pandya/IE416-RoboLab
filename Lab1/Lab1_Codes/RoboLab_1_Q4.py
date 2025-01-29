def sort_using_stack(l):
    lu=[]
    ll=[]
    lll=l
    while (l!=[]):
        if lu==[]:
            lu.append(l.pop())
        else:
            ele=l.pop()
            if (lu[-1]<=ele):
                lu.append(ele)
            else:
                while(lu!=[] and lu[-1]>ele):
                    ll.append(lu.pop())
                lu.append(ele)
                while (ll!=[]):
                    lu.append(ll.pop())
                    ''' 
                    1 2 3 5
                    
                    '''
    return lu
def main():
    l=list(map(int,input("Please enter elements of array in space separated manner (Eg: 1 2 3) :").split()))
    print("The initial array given as input: ",l)
    res=sort_using_stack(l)
    print("The final sorted array wil be : ",res)
main()