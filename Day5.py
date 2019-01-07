def mult(num):
    product = 1
    for i in range(1,num+1):
        product *= i
    print(product)

def add(num):
    sum = 0
    for i in range(num+1):
        sum += i
    print(sum)

def main():
    n = int(input("Enter a number here: "))
    endNow = False
    while endNow == False:
        userChoice = input("Enter m for multiplication from 1 to n or s for sum from 1 to n: ")
        if userChoice == "m":
            mult(n)
            endNow = True
        elif userChoice == "s":
            add(n)
            endNow = True
        else:
            userChoice = input("Enter m for multiplication from 1 to n or s for sum from 1 to n: ")
main()
