def reverse(x):
    string = str(x)
    lst = list(string)
    newlst = []
    s = len(lst)-1
    while s>=0:
        for i in range(s+1):
            newlst.append(lst[s])
            s-=1
    return str(newlst)

def main():
    print(reverse(123))
main()
