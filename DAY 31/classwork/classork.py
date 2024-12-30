#  1. შექმენით ფუნქცია, სადაც გამოიყენებთ return-ს, შემდეგ კი შექმენით იდენტური ფუნქცია, თუმცა print-ით.

# 2. შექმენით ფუნქცია, სადაც გექნებათ 5 ელემენტიანი სია, 

# ფუნქციაში შექმენით ცვლადი, სადაც შეინახავთ secret ინდექსის ციფრს,
# შემდეგ კი მომხმარებელმა სიიდან უნდა აირჩიოს რომელიმე ელემენტი, 
# თუ ელემენტის ინდექსი დაემთხვა secret_index-ს, 
# დაუბრუნეთ რომ მან მოიგო ჩელენჯი.


#1

def add(num1,num2):
    return num1*num2

print(add(61,55))

def add(num1,num2):
    return num1*num2

print(add(61,55))

#2

secret = 2

list=['soso','lana','bacho','achi','sandro']

print(list)

red = int(input("enter a nomber from 0-4 :"))


def idk():
 if red == secret:
    print("correct")
 elif red != secret:
    print("not correct")
 else:
     print("somthing went wrong")

idk()









