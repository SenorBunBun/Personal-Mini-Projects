#Task 1
numbers = list(range(5,21))
print(numbers)
print('\n '.join(list(map(str,numbers))))

#Task 2
names = ["aon", "bon", "pam", "don", "pam"]
print(names[2])

#Task 3
numbers = list(range(0,11))
print(numbers[3]+numbers[7])

#Task 4
x = 0
for i in range(len(numbers)):
    x += numbers[i]

#Task 5
print(numbers.count("pam"))

#Task 6
numbers = list(range(0,21))
print(list(filter(lambda a: a % 2 != 0, numbers)))

#Task 7
colors = ["nacho cheese yellow", "watermelon red", "orange orange", "banana yellow", "blueberry blue", "grey", "brown", "aquamarine"]
print(colors[0:3])

#Task 8
print(colors[0:2] + colors[5:8])

#Task 9
numbers = list(range(0,13))
print(sum(numbers)/len(numbers))

#Task 10
print(max(numbers))
