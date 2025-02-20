
# 1
def positive_sum(arr):
    total = 0
    for idk in arr:
        if idk > 0:
            total += idk
    return total

# 2
def multiply(a, b):
    return a * b

# 3
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

#4
la_liga_goals=43
champions_league_goals=10
copa_del_rey_goals=5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

#5
def solution(string, ending):
    return string.endswith(ending)

#1
numbers = [10, 20, 30, 40, 50]
print(sum(numbers))  # 10 + 20 + 30 + 40 + 50 = 150

#2
numbers = [10, 20, 30, 40, 50]
print(max(numbers))  # 50

#3
numbers = [10, 20, 30, 40, 50]
print(min(numbers))  # 10

#4
numbers = [10, 20, 30, 40, 50]
print(len(numbers))  # 5

#5
words = ["apple", "banana", "cherry", "date", "elderberry"]
words.append("fig")  
print(words)  # ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

#6
words = ["apple", "banana", "cherry", "date", "elderberry"]
words.insert(2, "grape")  # 2-ე ინდექსზე ჩასვავს "grape"-ს
print(words)  # ['apple', 'banana', 'grape', 'cherry', 'date', 'elderberry']

#7
words = ["apple", "banana", "cherry", "date", "elderberry"]
words.pop(3)  # წაშლის 3-ე ინდექსზე მდგომ "date"-ს
print(words)  # ['apple', 'banana', 'cherry', 'elderberry']
