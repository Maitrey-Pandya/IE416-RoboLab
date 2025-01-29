def get_val_from_dict(d,key):
    try:
        return d[key]
    except KeyError:
        print("The key \'{0}\' you are looking for is unfortunately not found :( ".format(key))
        return None
def main():
    a=str(input("Enter a string : "))
    b=str(input("Enter a alphabet : "))
    d={}
    for i in a:
        if (i in d):
            d[i]+=1
        else:
            d[i]=1
    get_val_from_dict(d,b)
main()
 