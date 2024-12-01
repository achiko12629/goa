
num1 = float(input("სეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))
operator = input("შეიყვანე ოპერატორი (+, -, *, /): ")


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "რავი აბა რაღაც არასწორათ გააკეთე"

print(result)
