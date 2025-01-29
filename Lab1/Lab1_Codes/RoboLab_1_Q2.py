def freq_of_alpha(string):
    d={}
    for i in string:
        if i in d:
            d[i]+=1
        else:
            d[i]=1 
    print(d)
def main():
    string=str(input("Enter Your String :"))
    freq_of_alpha(string)
main()