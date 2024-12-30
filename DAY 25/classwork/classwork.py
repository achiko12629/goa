
#1
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
#3
password = input("enter the password:")
name = "achiko"

while password != name:
    print("incorrect password try agen ")
    password = input("enter the password:")
print("correct")
