
#1
def greet():
    return "hello world!"
#2
def add_five(num):
    total = num + 5
    return total
#3
def make_negative( number ):
    return -abs(number)
#4
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
#5
def check_alive(health):
    if health <= 0:
        return False
    else:
        return True