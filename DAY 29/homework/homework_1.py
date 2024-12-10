# 2. შექმენით ფუნქცია სახელად threeproduct, რომელიც არგუმენტათ იღებს 3 რიცხვს და პრინტავს მათ ნამრავლს.
# 3. შექმენით ფუნქცია სახელად greet, რომელიც არგუმენტად იღებს სახელს და პრინტავს მისალმების მესიჯს.
# 4. შექმენით ფუნქცია სახელად comparison, რომელიც არგუმენტად იღებს 2 რიცხვს და პრინტავს მათ შორის ჩატარებული 4 არითმეტიკული ოპერაციის შედეგს: <,>,<=,>=.
# 5. შექმენით ფუნქცია სახელად agecalc, რომელსაც არგუმენტად გადაეცემა მომხმარებლის ასაკი და პრინტავს, თუ რომელ წელს დაიბადა იგი.

#2
def threeproduct(num,num1,num2):
    print(num*num1*num2)

threeproduct(4,7,31)

#3
def greet(name):
    print(f'hello {name}')

greet('achiko')

#4
def comparison(num,num1):
    print( num < num1)
    print( num > num1)
    print( num <= num1)
    print( num >= num1)

comparison(34,4)

#5
def age(age1):
    print(2024 - age1)

nam = int(input('enter your age :'))
age(nam)