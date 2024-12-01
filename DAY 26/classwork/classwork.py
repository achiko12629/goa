# 1) შექმენით 5 ელემენტიანი სია და ამოაგდეთ მე-0-ე და მე-4-ე ინდექსზე მდგომი ელემენტები

# 2) შექმენით 5 ელემენტიანი სია და მე-2-ე და მე-3-ე ინდეხებზე დაამატეთ 2 ელემენტი

# 3) შექმენით 5 ელემენტიანი სია და მის ბოლოში დაამატეთ 3 ელემენტი. inspect-ი არ გამოიყენოთ
 
# 4) შექმენით დიდი სია და დაითვალეთ მასში რამდენი ელემენტია


#1
goa = ['grup 37','grup 88','grup 54','grup 63','grup 68']

goa.pop(0)
goa.pop(2)
print(goa)

#2
goa = ['grup 37','grup 88','grup 54','grup 63','grup 68']

goa.insert(2, 'idk')
goa.insert(3, 'soso')

#3
goa = ['grup 37','grup 88','grup 54','grup 63','grup 68']
goa.append('okey')
goa.append('omg')
goa.append('sooo')

#4
goa = ['grup 37','grup 88','grup 54','grup 63','grup 68',1,2,3,4,5,6,7,8,9,0,1,2,23]
print(len(goa))