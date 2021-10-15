# Sean Walshe
# 15-oct-2021





def greet(name: str):
    print(f"hi {name}")
    print("you are a prick")

def add(x: int, y: int):
    return int(x) + int(y)

def substract(x: int, y: int):
    return int(x) - int(y)

def multiply(x: int, y: int):
    return int(x) * int(y)

def divide(x: int, y: int):
    try:
        return int(x) / int(y)
    except ZeroDivisionError:
        print("cannot divide by zero")



if __name__ == "__main__":

    # surname=input("what is your name ")

    # greet(surname)
    x = input("think of a number ")
    y = input("think of another number ")
    print("1-Add")
    print("2-Subtract")
    print("3-Multiple")
    print("4-Divide")
    opp = input("what operation do you want to perform? ")
    opp = int(opp)
    if opp == 1:
        z = add(x,y)
    elif opp == 2:
        z = substract(x,y)
    elif opp == 3:
        z = multiply(x,y)
    elif opp == 4:
        z = divide(x,y)
    else :
       z = "invalid number"

    print (z)



         
         

  
  
  
  
   
   



