import random

cargill_bls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

empire_bls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

mccormick_bls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

hivee_bls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def cargill_cycle():
    car_rand = random.sample(cargill_bls, 5)
    print(car_rand)

def empire_cycle():
    emp_rand = random.sample(empire_bls, 5)
    print(emp_rand)

def mcc_cycle():
    mcc_rand = random.sample(mccormick_bls, 5)
    print(mcc_rand)

def hivee_cycle():
    hivee_rand = random.sample(hivee_bls, 5)
    print(hivee_rand)

while True:
    counts = input("What Customer Would You Like To Cycle Count For?").lower()

    if counts == "cargill":
        cargill_cycle()
        break
    elif counts == "empire":
        empire_cycle()
        break
    elif counts == "mccormick":
        mcc_cycle()
        break
    elif counts == "hivee":
        hivee_cycle()
        break
    else:
        print("Please choose a Customer!")
        continue



