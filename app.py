# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [n ** 2 for n in numbers]

print(result)


# 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

result = [n for n in numbers if n % 2 == 0]

print(result)


# 3
numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

result = [n for n in numbers if n % 2 !=0]

print(result)


# 4
fruits =  ["apple", "banana", "pear"]

result = [f"Uzunligi: {len(f)}" for f in fruits]

print(result)


# 5
word = "So'z"

result = [w for w in word]

print(result)
