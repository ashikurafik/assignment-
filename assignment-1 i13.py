# Task 1
def name_age():
    name, age = "Ashikur rhaman", 24
    print("My Name is {} and i am {} years old".format(name, age))

name_age()


# Task 2
num1 = 7
num2 = 56.07
num1_float = float(num1)
num2_int = int(num2)
print("num1:", num1, "is of type:", type(num1))
print("num2:", num2, "is of type:", type(num2))
print("num1_float:", num1_float, "is of type:", type(num1_float))
print("num2_int:", num2_int, "is of type:", type(num2_int))

# Task 3
sentence = "Python Programming is fun!"
print("Length of the string:", len(sentence))
print("8th character:", sentence[7])
substring = sentence[0:6]
result = substring + " I enjoy it!"
print(result)

# Task 4
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("grape")
fruits.remove("banana")
print("Length of the list:", len(fruits))
sliced_fruits = fruits[1:3]
extra_fruits = ["kiwi", "lemon"]
combined_list = sliced_fruits + extra_fruits
print("Combined list:", combined_list)

# Task 5
num = 7
if num % 2 == 0:
    print(num, "is even number.")
else:
    print(num, "is odd number.")

# Task 6
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)
sum = 0
for i in range(1, 101):
    sum += i
print("Sum of numbers from 1 to 100:", sum)

# Task 7
def calculate_square(num):
    return num ** 2
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
number = 7
square_of_number = calculate_square(number)
print("Square of", number, "is:", square_of_number)
number2 = 29
if is_prime(number2):
    print(number2, "is a prime number.")
else:
    print(number2, "is not a prime number.")

# Task 8
student = {
    "name": "Ashikur rhaman",
    "age": 24,
    "grade": "A+"
}
student["course"] = "Computer Science & Engineering"
print("Keys in the dictionary:", student.keys())
print("Key-value pairs in the dictionary:")
for key, value in student.items():
    print(key, ":", value)