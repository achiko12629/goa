# 1. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი indexing-ის მეშვეობით გამოიტანეთ მეორე ელემენტი.
# 2. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი შეცვალეთ მეორე ინდექსი სხვა მნიშვნელობით.
# 3. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (positive indexing).
# 4. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (negative indexing).
# 5. შექმენით სია, სადაც გექნებათ 6 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეოთხე ელემენტი (negative indexing & positive indexing).

#1

Name = ["achi",'levani',"dito","demetre"]
print(Name[1])

#2

men = ['ronaldo','neymar','mbape','messi']
men[2]='achi'
print(men)

#3

people = ["achi",'levani',"dito","demetre","idk"]
print(people[1:3])

#4
idk = ["achi",'levani',"dito","demetre","idk"]
print(idk[-4:-2])

#5
idk_1 =["achi",'levani',"dito","demetre","idk","guga"]
print(idk_1[0:-2])


