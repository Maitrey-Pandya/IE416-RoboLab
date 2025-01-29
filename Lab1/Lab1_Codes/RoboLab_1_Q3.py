def keep_only_1st_occ(l):    
    s=set()
    for i in range(len(l)):
        s.add(l[i])
    l.clear()
    for i in s:
        l.append(i)
def main():
    l=list(map(int,input("Please enter elements of array in space separated manner (Eg: 1 2 3) :").split()))
    print("The initial array given as input: ",l)
    keep_only_1st_occ(l)
    print("The final array after removing extra occurences : ",l)
main()