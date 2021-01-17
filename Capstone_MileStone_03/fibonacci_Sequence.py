
# 0 1 1 2 3 5 8 13 21

def get_user_input():
    '''
    This will ask the user for a number
    Make sure the user gives a number
    Number has to be greater than 0
    return the number to the program
    '''
    user_number = 0
    while True:
        try:
            user_number = int(input("Please enter a number greater than 0: "))
        except:
            print("You did not enter a number greater than 0")
        else:
            if user_number > 0:
                break
            else:
                print("The number has to be greater than 0.  Try again.")
    return user_number


if __name__ == "__main__":
    print("Welcome to the Fibonacci Sequence Generator.  It will take a number you enter and calculate the sequence "
          "to that number.")
    seq_number = get_user_input()
    counter = 0
    a = 0
    b = 1
    if seq_number <= 1:
        print(a)
    elif seq_number <= 2:
        print(str(a) + " " + str(b))
    else:
        print(str(a) + " " + str(b), end=" ")
        while counter <= seq_number:
            c = a + b
            print(c, end=" ")
            counter += 1
            a = b
            b = c
