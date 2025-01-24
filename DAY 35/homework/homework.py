# 1. 
list1 = [10, 25, 35, 50, 5]
list2 = [100, 200, 300, 400, 500]
list3 = [7, 3, 8, 1, 6]
print( max(list1))
print( max(list2))
print( max(list3))

#2
print( min(list1))
print( min(list2))
print( min(list3))

#3
print( len(list1))
print(len(list2))
print( len(list3))

#4
print( sum(list1))
print( sum(list2))
print( sum(list3))

# 5. 
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list5 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list6 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list7 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


print(list4[:4])

for i in range(3, 8):  
    print(i, list5[i])


print( list6[8:5:-1])  


i = 0
while i < len(list7):
    print(f"List7 element at {i}: {list7[i]}")
    i += 1


def analyze_list(user_list):
    if len(user_list) < 5:
        print("5 numbers.")
        return
    print("Max:", max(user_list))
    print("Min:", min(user_list))
    print("Sum:", sum(user_list))
    print("Length:", len(user_list))

analyze_list([3, 1, 4, 1, 5, 9])
