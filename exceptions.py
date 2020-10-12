try:

    input1 = input("Please enter a first number: ")
    input2 = input("Please enter a second number: ")

    c = int(input1) + int(input2)

    print(c)
except:
    print("Incorrect data")
finally:
    print("Execute code is always perform")