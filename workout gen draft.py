import random

pushcom = ['Bench Press', 'Overhead Press', 'Dips', 'DB Bench Press', 'DB Military']

pullcom = ['Pull Ups', 'BB Rows', 'Dead Lift', 'Back EXT', 'Underhand EZ Row', 'Cable Row']

push = ['Tricep EXT', 'Skull Crushers', 'Tricep Pulldown', 'Chest Press', 'Push Ups', 'DB Side Raises',
        'DB Front Raises']

legcom = ['Squat', 'Lunge', 'RDL', 'Leg Press', 'Front Squat']

pull = ['DB Row', 'Shrugs', 'Machine Row', 'Lat Pull Downs', 'Curls', '21', 'Preacher', 'Forearm Curl',
        'Forearm Cable']

legs = ['Split Squats', 'Thrusts', 'Seated Calf', 'Calf Raise', 'Ham Curl', 'Quad EXT']

def push_day():
    amount = 2
    random_ex = random.sample(pushcom, amount)
    rand_items1 = random_ex[0]
    rand_items2 = random_ex[1]
    print(rand_items2, '|', rand_items1)

    amount = 3
    random_ex = random.sample(push, amount)
    rand_items1 = random_ex[0]
    rand_items2 = random_ex[1]
    rand_items3 = random_ex[2]
    print(rand_items2, '|', rand_items1, '|', rand_items3)


def pull_day():
    amount = 2
    random_ex = random.sample(pullcom, amount)
    rand_items1 = random_ex[0]
    rand_items2 = random_ex[1]
    print(rand_items2, '|', rand_items1)

    amount = 3
    random_ex = random.sample(pull, amount)
    rand_items1 = random_ex[0]
    rand_items2 = random_ex[1]
    rand_items3 = random_ex[2]
    print(rand_items2, '|', rand_items1, '|', rand_items3)


def leg_day():
    amount = 2
    random_ex = random.sample(legcom, amount)
    rand_items1 = random_ex[0]
    rand_items2 = random_ex[1]
    print(rand_items2, '|', rand_items1)

    amount = 3
    random_ex = random.sample(legs, amount)
    rand_items1 = random_ex[0]
    rand_items2 = random_ex[1]
    rand_items3 = random_ex[2]
    print(rand_items2, '|', rand_items1, '|', rand_items3)



while True:
    day = input('Push, Pull or Legs?').lower()

    if day == 'push':
        print(push_day())
    elif day == 'pull':
        print(pull_day())
    elif day == 'legs':
        print(leg_day())
    else:
        print('Invalid Entry!')
