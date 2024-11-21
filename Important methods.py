# words = ["banana","apple" , "cherry"]
# print(min(words, key=len))  # Output: 'apple'
# print(max(words, key=len))  # Output: 'banana'

grades = {"Alice": 88, "Bob": 95, "Charlie": 78}
print(min(grades, key=grades.get))  # Output: 'Charlie'
print(max(grades, key=grades.get))  # Output: 'Bob'

