# Task 1

for i in range(1, 11):
    print(i)

# Task 2


def sum(num_1, num_2, num_3):
    return num_1 + num_2 + num_3


print(sum(5, 6, 5))

# Task 3

lambda_sum = lambda num_1, num_2, num_3: num_1 + num_2 + num_3
result = lambda_sum(5, 6, 5)

print(result)

# Task 4

name = "Henry"
list_name = ["Jessica", "Paul", "George", "Henry", "Adam"]


for name in list_name:
    if name == "Henry":
        print(f"Congratulations {name}, you are in the list.")
    else:
        print(f"Sorry {name}, you are not in the list.")
