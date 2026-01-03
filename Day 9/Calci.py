import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

operations = { add:"+",
               sub:"-",
               multi:"*",
               div:"/"}

def calci():
    continue_cali = True
    n1 = float(input("Enter the First Number: \n"))
    while continue_cali:

        choice = input(f"\n +\n -\n *\n /\n What operation do you want to perform: ")

        n2 = float(input("Enter next Number: \n"))

        if choice == operations[add]:
            res = add(n1,n2)
            print(f"Addition is: {n1}+{n2}={res}")
        elif choice == operations[sub]:
            res = sub(n1,n2)
            print(f"Substraction is: {n1}-{n2}={res}")
        elif choice == operations[multi]:
            res = multi(n1,n2)
            print(f"Substraction is: {n1}*{n2}={res}")
        else:
            res = div(n1,n2)
            print(f"Substraction is: {n1}/{n2}={res}")
        new_calci = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation:\n").lower()
        if new_calci == "y":
            n1 = res
            continue_cali = True
        else:
            print("\n"*30)
            continue_cali = False
            print(art.logo)
            calci()

calci()







