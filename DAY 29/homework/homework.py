# 1. შექმენით BMI-ის გამომთვლელი ფუნქცია, რომელიც არამარტო ქულას უპრინტავს მომხმარებელს, არამედ ტექსტურად ეუბნება, 
# თუ რომელ წონით კატეგორიაში არის ის,
# დავალების შესასრულებლად გამოიყენეთ შემდეგი ფორმულა:

def bmi(weight,hight):
   idk = weight / hight **2
   return idk
  

num1 = int(input('enter your weight:'))
num2 = float(input('enter your hight:'))
omg = bmi(num1,num2)



if omg <= 18.5:
    print(  'your underweight' )
elif 18.5 < omg  < 24.9:
    print('your normal')
elif 25 < omg < 29.9:
    print('your owerweight')
elif 30 < omg < 34.9:
    print('your obese')
elif 35 < omg :
    print('your extremely obese')
else:
    print('something went wronge')





















