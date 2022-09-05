import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 next time.")
        quit()
else:
    print("please type a number next time.")
    quit()

random_number = random.randint(-1, 11)

while True:
    print("mike")
    break
