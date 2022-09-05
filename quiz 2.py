playing = input("do you want to play?")
if playing != "yes":
    quit()
else:
    print("lets play!")
score = 0

answer = input("what does RAM stand for?")
    if answer == ("random access memory"):
        print("correct!")

    else:
        print("incorrect!")
        score += 1
        continue
print("Game Completed")
print(str(score))