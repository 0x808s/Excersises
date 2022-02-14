time = 0
total_time = 0
fastest = 0
while time != -1:
    time = float(input("Enter User time: "))
    if time > 0:
        total_time += time
        time_list.append(time)
    else:
        break

fastest = sorted(time_list)[0]
average = total_time / len(time_list)
print(time_list)
print("Average time of runs were: {}".format(average))
print("The fastest time was: {} seconds".format(fastest))
