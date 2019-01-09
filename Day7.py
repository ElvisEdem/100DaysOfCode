def main():
    userInput = int(input("Enter a number here: "))
    for i in range(1,13):
        product = userInput * i
        print(userInput, "*", i, "=", product)
main()
