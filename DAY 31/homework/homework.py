# 1. შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.

# 2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს

# 3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len(), ახალი მასალაა).

# 4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).

# 5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.

# 6. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. 
# (მაგალითად: input: "Hello World". output: "HELLO WORLD".



# 1. 
def add_five(number):
    return number + 5

print(add_five(10))

# 2. 
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(3, 4)) 
# 3. .
def string_length(string):
    return len(string)

print(string_length("Hello"))

# 4.
def strings_lengths(strings):
    return [len(s) for s in strings]

print(strings_lengths(["abc", "hello", "Python"]))

# 5. 
def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome("wow"))


# 6. 
def to_uppercase(string):
    return string.upper()


print(to_uppercase("Hello World")) 
