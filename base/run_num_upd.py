with open("run_num.txt", "r") as file:
    number = int(file.read())

number += 1

with open("run_num.txt", "w") as file:
    file.write(str(number))