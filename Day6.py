def mult(num):
    product = 1
    for i in range(1,num+1):
        product *= i
    print(product)

def multconditional(num):
    product = 1
    for i in range(1,num+1):
        if i % 3 == 0 or i % 5 == 0:
            product *= i
    print(product)

def add(num):
    sum = 0
    for i in range(num+1):
        sum += i
    print(sum)

def addconditional(num):
    sum = 0
    for i in range(num+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)


def main():
    n = int(input("Enter a number here: "))
    endNow = False
    while endNow == False:
        userChoice = input("Enter m for multiplication from 1 to n or s for sum from 1 to n: ")
        endNow2 = False
        while endNow2 == False:
            if userChoice == "m":
                userChoice2 = input("Enter n for no condition and c for condition: ")
                if userChoice2 == "n":
                    mult(n)
                    endNow2 = True

                elif userChoice2 == "c":
                    multconditional(n)
                    endNow2 = True
                else:
                    userChoice2 = input("Enter n for no condition and c for condition: ")


        else:
            endNow3 = False
            while endNow3 == False:
                if userChoice == "s":
                    userChoice3 = input("Enter n for no condition and c for condition: ")
                    if userChoice3 == "n":
                        add(n)
                        endNow3 = True
                    elif userChoice3 == "c":
                        addconditional(n)
                        endNow3 = True
                    else:
                        userChoice3 = input('Enter n for no condition and c for condition')
    else:
        userChoice = input("Enter m for multiplication from 1 to n or s for sum from 1 to n: ")
main()
