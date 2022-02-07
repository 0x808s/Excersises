bike = 200
jog = 475
swim = 275

biking = int(input("How long did you bike: "))
if biking.isalpha():
    print("you entered a string. restart please.")
    exit()


jogging = int(input("How long did you jog: "))
if jogging.isalpha():
    print("you entered a string. restart please.")
    exit()

swimming = int(input("How long did you swim: "))
if swimming.isalpha():
    print("you entered a string. restart please.")
    exit()


weightloss = biking * bike + jogging * jog + swimming * swim

result = weightloss / 3500 * 0.454
print("You lost ", result, " kg's")



