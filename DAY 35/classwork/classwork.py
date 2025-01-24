# 1. ფუნქცია უნდა პრინტავდეს დამარცვლილ სახელს, შებრუნებულად.


name = input("emter your name :")


def speller(name):
     omg = name[::-1]
     for i in omg:
          print(i)
    

speller(name)



# 2. შექმენით ფუნქცია, რომელსაც გადაეცემა 5 არგუმენტი, 5 ინფუთით მომხარებელს აარჩევინეთ ნებისმიერი რიცხვი, ბოლოს კი დაუპრინტეთ ამ რიცხვებისაგან შემდგარი სია.


def create(no ,yes ,meybi ,nigers , sigma):
    
    numbers = [no ,yes ,meybi ,nigers , sigma]
    print("თქვენი რიცხვების სია:", numbers)


nub = int(input(" პირველი : "))
boob = int(input("მეორე : "))
gluub = int(input(" მესამე : "))
soop = int(input(" მეოთხე : "))
omg = int(input(" მეხუთე : "))


create( nub, boob, gluub, soop, omg)

# 3. შექმენით ფუნქცია რომელიც არგუმენტად აიღებს თქვენს შექმნილ სიას, რომელშიც იქნება მინიმუმ 5 რიცხვი და დაპრინტავს ამ სიისის მაქსიმალურ რიცხვს, მინიმალურ რიცხვს, რიცხვების ჯამს და სიის სიგრძეს.

numbers = [1622, 4082, 400000, 29, 90]


def list(numbers):
    
    max = max(numbers)
    mi = min(numbers)
    to = sum(numbers)
    len = len(numbers)

    print("მაქსი", max)
    print("მინი:", mi)
    print(" ჯამი:", to)
    print(" სიგრძე:", len)



list(numbers)
