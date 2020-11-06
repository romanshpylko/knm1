while True:
    x = float(input("Перша цифра: "))
    y = float(input("Друга цифра: "))
    operation = input("Дія: ")

    result = None

    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    elif operation == "/":
        result = x / y
    else :
        print ("Дія не підтримується")
    if result is not None:
        print ("Результат:", result)

          
          
          

